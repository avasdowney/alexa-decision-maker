# -*- coding: utf-8 -*-

import logging
import six
import random

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type

from typing import Union, Dict, Any, List
from ask_sdk_model.dialog import (
    ElicitSlotDirective, DelegateDirective)
from ask_sdk_model import (
    Response, IntentRequest, DialogState, SlotConfirmationStatus, Slot)
from ask_sdk_model.slu.entityresolution import StatusCode

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ACTIVITIES = {
    'inside': {'cheap': ['Bake cookies.', 'Make macaroni art.', 'Play video games.', 'Listen to music.', 'Take a nap.',
                         'Go through old pictures.', 'Make a video for YouTube.',
                         'Go to the grocery store and eat the free samples.', 'Make an Alexa skill.'],
               'expensive': ['Go shopping.', 'Go bowling.', 'Go to the movies.', 'Go out to eat at a restaurant.']},
    'outside': {'cheap': ['Go for a drive.', 'Go swimming.', 'Go ice skating.', 'Have a photo shoot.', 'Go on a hike.',
                          'Go on a walk.', 'Go get ice cream.', 'Do a backflip.'],
                'expensive': ['Go mini golfing.']}
}

# Request Handler classes
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")
        speech = ('Welcome to activity decider.  I can help you decide on an activity '
                  'for you. What cost and location are you looking for?')
        reprompt = "What cost and location are you looking for in an activity?"
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class MythicalCreaturesHandler(AbstractRequestHandler):
    """Handler for MythicalCreatures."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        if not is_intent_name("ActivityMatchIntent")(handler_input):
            return False

        is_mythical_creature = False
        resolved_value = get_resolved_value(
            handler_input.request_envelope.request, "activity")
        if (resolved_value is not None and
                resolved_value == "mythical_creatures"):
            is_mythical_creature = True
            handler_input.attributes_manager.session_attributes["mythical_creature"] = handler_input.request_envelope.request.intent.slots["activity"].value
        return is_mythical_creature

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In MythicalCreaturesHandler")
        session_attr = handler_input.attributes_manager.session_attributes
        speech = random_phrase(slots_meta["activity"]["invalid_responses"]).format(
            session_attr["mythical_creature"])

        return handler_input.response_builder.speak(speech).response


class InProgressActivityMatchIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("ActivityMatchIntent")(handler_input)
                and handler_input.request_envelope.request.dialog_state != DialogState.COMPLETED)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In InProgressActivityMatchIntent")
        current_intent = handler_input.request_envelope.request.intent
        prompt = ""

        for slot_name, current_slot in six.iteritems(
                current_intent.slots):
            if slot_name not in ["article", "at_the", "I_Want"]:
                if (current_slot.confirmation_status != SlotConfirmationStatus.CONFIRMED
                        and current_slot.resolutions
                        and current_slot.resolutions.resolutions_per_authority[0]):
                    if current_slot.resolutions.resolutions_per_authority[0].status.code == StatusCode.ER_SUCCESS_MATCH:
                        if len(current_slot.resolutions.resolutions_per_authority[0].values) > 1:
                            prompt = "Which would you like "

                            values = " or ".join([e.value.name for e in current_slot.resolutions.resolutions_per_authority[0].values])
                            prompt += values + " ?"
                            return handler_input.response_builder.speak(
                                prompt).ask(prompt).add_directive(
                                ElicitSlotDirective(slot_to_elicit=current_slot.name)
                            ).response
                    elif current_slot.resolutions.resolutions_per_authority[0].status.code == StatusCode.ER_SUCCESS_NO_MATCH:
                        if current_slot.name in required_slots:
                            prompt = "What {} are you looking for?".format(current_slot.name)

                            return handler_input.response_builder.speak(
                                prompt).ask(prompt).add_directive(
                                    ElicitSlotDirective(
                                        slot_to_elicit=current_slot.name
                                    )).response

        return handler_input.response_builder.add_directive(
            DelegateDirective(
                updated_intent=current_intent
            )).response


class CompletedActivityMatchIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("ActivityMatchIntent")(handler_input)
            and handler_input.request_envelope.request.dialog_state == DialogState.COMPLETED)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CompletedActivityMatchIntent")
        filled_slots = handler_input.request_envelope.request.intent.slots
        slot_values = get_slot_values(filled_slots)

        #
        # Given the filled slot values with cost and location, figure out a match.
        #
        # slot_values holds what the user selected, use it to look up based on our
        # map of choices
        #

        resolved_location = slot_values["location"]["resolved"]
        resolved_cost = slot_values["cost"]["resolved"]

        # Narrow it in to the possible choices
        possible_choices = ACTIVITIES[resolved_location][resolved_cost]

        if possible_choices:
            # Finally, pick one at random
            the_choice = random.choice(possible_choices)

            speech = ("So a {} "
                      "{} "
                      "activity good for you. Consider a "
                      "{}".format(
                resolved_location,
                resolved_cost,
                the_choice)
            )
        else:
            speech = ("I am sorry I could not find a match for a "
                      "{} "
                      "{} activity".format(
                resolved_location,
                resolved_cost)
            )

        return handler_input.response_builder.speak(speech).response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for handling fallback intent.
     2018-May-01: AMAZON.FallackIntent is only currently available in
     en-US locale. This handler will not be triggered except in that
     locale, so it can be safely deployed for any locale."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = ("I'm sorry Activity Decider can't help you with that. I can help "
                  "find the perfect activity for you. What are two things you're "
                  "looking for in an activity?")
        reprompt = "What cost and location are you looking for in an activity?"
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for help intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        speech = ("This is activity decider. I can help you find the perfect activity "
                  "for you. You can say, I want an activity.")
        reprompt = "What cost and location are you looking for in an activity?"

        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class ExitIntentHandler(AbstractRequestHandler):
    """Single Handler for Cancel, Stop and Pause intents."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ExitIntentHandler")
        handler_input.response_builder.speak("Bye").set_should_end_session(
            True)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response

# Exception Handler classes
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch All Exception handler.
    This handler catches all kinds of exceptions and prints
    the stack trace on AWS Cloudwatch with the request envelope."""
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Sorry, I can't understand the command. Please say again."
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


# Request and Response Loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the request envelope."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.info("Request Envelope: {}".format(
            handler_input.request_envelope))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the response envelope."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.info("Response: {}".format(response))


# Data
required_slots = ["cost", "location"]

slots_meta = {
    "activity": {
        "invalid_responses": [
            "I'm sorry, but I'm not qualified to match you with {}s.",
            "Ah yes, {}s are splendid creatures, but unfortunately owning one as a pet is outlawed.",
            "I'm sorry I can't match you with {}s."
        ]
    },
    "error_default": "I'm sorry I can't match you with {}s."
}

# Utility functions
def get_resolved_value(request, slot_name):
    """Resolve the slot name from the request using resolutions."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return (request.intent.slots[slot_name].resolutions.
                resolutions_per_authority[0].values[0].value.name)
    except (AttributeError, ValueError, KeyError, IndexError, TypeError) as e:
        logger.info("Couldn't resolve {} for request: {}".format(slot_name, request))
        logger.info(str(e))
        return None

def get_slot_values(filled_slots):
    """Return slot values with additional info."""
    # type: (Dict[str, Slot]) -> Dict[str, Any]
    slot_values = {}
    logger.info("Filled slots: {}".format(filled_slots))

    for key, slot_item in six.iteritems(filled_slots):
        name = slot_item.name
        try:
            status_code = slot_item.resolutions.resolutions_per_authority[0].status.code

            if status_code == StatusCode.ER_SUCCESS_MATCH:
                slot_values[name] = {
                    "synonym": slot_item.value,
                    "resolved": slot_item.resolutions.resolutions_per_authority[0].values[0].value.name,
                    "is_validated": True,
                }
            elif status_code == StatusCode.ER_SUCCESS_NO_MATCH:
                slot_values[name] = {
                    "synonym": slot_item.value,
                    "resolved": slot_item.value,
                    "is_validated": False,
                }
            else:
                pass
        except (AttributeError, ValueError, KeyError, IndexError, TypeError) as e:
            logger.info("Couldn't resolve status_code for slot item: {}".format(slot_item))
            logger.info(e)
            slot_values[name] = {
                "synonym": slot_item.value,
                "resolved": slot_item.value,
                "is_validated": False,
            }
    return slot_values

def random_phrase(str_list):
    """Return random element from list."""
    # type: List[str] -> str
    return random.choice(str_list)

# Skill Builder object
sb = SkillBuilder()

# Add all request handlers to the skill.
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(MythicalCreaturesHandler())
sb.add_request_handler(InProgressActivityMatchIntent())
sb.add_request_handler(CompletedActivityMatchIntent())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(ExitIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Add exception handler to the skill.
sb.add_exception_handler(CatchAllExceptionHandler())

# Add response interceptor to the skill.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Expose the lambda handler to register in AWS Lambda.
lambda_handler = sb.lambda_handler()