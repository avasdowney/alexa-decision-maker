# -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# =========================================================================================================================================
# TODO: The items below this comment need your attention.
# =========================================================================================================================================
SKILL_NAME = "Activity Decider"
GET_FACT_MESSAGE = "Here's your activity: "
HELP_MESSAGE = "You can say give me an activity, or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "The Activity Decider skill can't help you with that.  It can help you decide on an activity if you say What should I do. What can I help you with?"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."

# =========================================================================================================================================
# TODO: Replace this data with your own.  You can find translations of this data at http://github.com/alexa/skill-sample-python-fact/lambda/data
# =========================================================================================================================================

free_activities = [
  'Bake cookies.',
  'Make macaroni art.',
  'Play video games.',
  'Go for a drive.',
  'Listen to music.',
  'Take a nap.',
  'Go through old pictures.',
  'Have a photo shoot.',
  'Go on a hike.',
  'Go on a walk.',
  'Make a video for YouTube.',
  'Go to the grocery store and eat the free samples.',
  'Do a backflip.',
  'Make an Alexa skill.',
  'Cry.'
]

indoor_activities = [
  'Go shopping.',
  'Go bowling.',
  'Go to the movies.',
  'Bake cookies.',
  'Make macaroni art.',
  'Play video games.',
  'Listen to music.',
  'Take a nap.',
  'Go through old pictures.',
  'Have a photo shoot.',
  'Make a video for YouTube.',
  'Go out to eat at a restaurant.',
  'Cry.'
]

exhibition_activities = [
  'Snap your fingers once.',
  'Snap your fingers twice.',
  'Snap your fingers thrice.'
]

# =========================================================================================================================================
# Editing anything below this line might break your skill.
# =========================================================================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
class GetNewActivityHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFreeActivity Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_request_type("IntentRequest")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewActivityIntentHandler")

        speech = ""
        # Collect some debug information either way
        # object_type = handler_input.request_envelope.request.object_type
        # speech = "Object type is " + object_type
        # if is_request_type("IntentRequest")(handler_input):
        #    intent = handler_input.request_envelope.request.intent.name
        #    speech = speech + " and intent is " + intent + ". "

        # Next, based on the type of intent, find the right activity
        if is_intent_name("GetNewFreeActivityIntent")(handler_input):
            random_fact = random.choice(free_activities)
            speech = speech + ("Here's your free activity: ") + random_fact
        elif is_intent_name("GetNewIndoorActivityIntent")(handler_input):
            random_fact = random.choice(indoor_activities)
            speech = speech + ("Here's your indoor activity: ") + random_fact
        elif is_intent_name("GetNewExhibitionActivityIntent")(handler_input):
            random_fact = random.choice(exhibition_activities)
            speech = speech + ("Here's your exhibition activity: ") + random_fact
        else:
            speech = speech + "Try asking for something more specific like 'Give me something free from activity decider'"

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, speech)).set_should_end_session(
            True)

        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(GetNewActivityHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
