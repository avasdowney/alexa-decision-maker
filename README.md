# How I Created my Amazon Alexa Skill

By: Ava Downey
 
#### Introduction:

For my senior project, I studied how to create an Amazon Alexa skill. Specifically, How can I create an Amazon Alexa skill? I created a skill, but as I am Ava, I went on tangents not specifically related to my original goal of making a complex skill. I decided to focus more on the general program aspects of creating a program, but under the guise of Amazon Alexa, as it was something I had never done before and I loved the idea of my friends being able to use what I created. I also had a cool idea for a skill to decide on activities for me to do because I am a super indecisive person, and I know a lot of people who struggle with making decisions as well. It also seemed fun to have something lighthearted to code. 

Since I ended up focusing on a lot of the backend of coding, I decided to make this how to article better by specifying the work I did as my experiential learning. I ended up reading a lot of seperate how to guides in my process, but they all only covered one specific topic, and I wanted to be able to encapsulate my entire process in one place, making it easier for others to create their own skill. 
Before I got started, I learned what an Alexa skill is, and what I was getting myself into.. Alexa is “Amazon’s cloud-based voice service and the brain behind tens of millions of devices including the Echo family of devices, FireTV, Fire Tablet, and third-party devices with Alexa built-in”. The devices I will be focusing on for my senior project will be the Amazon Echo, and its little brother, the Amazon Echo Dot. They are voice controlled speakers with Amazon Alexa hardware within that makes it able to accomplish what it is able to accomplish. This is the Alexa that often comes to mind when thinking about Amazon Alexa. It is simply a speaker and microphone combination that acts as a vessel for Amazon Alexa skills. It is activated by saying “Alexa {skill I want to open.}” An Amazon Alexa Skill is a type of app made for an Amazon Alexa. There am hundreds of built in commands as varied as media controls, time and date, calls and messaging, purchasing, to-do and shopping lists, news and weather, entertainment, food and businesses, math, definitions and spelling, sports, smart home, search, and even easter eggs. It is capable of doing almost anything I can imagine. Many other skills can be downloaded. Many of the popular ones, such as Spotify, are automatically downloaded when I mention the skills name. I can download any skill from the skill store by going into the app on my phone, and downloading and enabling the skill.

An Amazon Alexa device is able to process language by sending it to the cloud where Alexa Voice Services will interpret what is being said and send a response back to my Alexa. Alexa has a small computer inside that makes it able to do this, but it needs to have an internet connection to be able to actually achieve anything. Alexa is also an example of what machine learning is because it learns new things every time somebody talks to it. It learns new words, mannerisms, accents, and much more to make it smarter and more useful for the user. The longer smart devices like Amazon Alexa are around, the smarter and more natural they become.

Generally stated, creating an Alexa skill takes a lot of steps. First, I needed to come up with a plan on what I want to create my skill on, as it is very hard to create a skill without knowing what to create. Next, I created a draft of what I want to do and collect feedback on it. This feedback was used to better my skill. Next, I needed to set up a few accounts to be able to create my skill. My Amazon Developer account and my Amazon Web Services account are required as they are what allows Amazon to deploy my skill. my GitHub account and Travis CI accounts made my life 100x easier when it came to actually testing and making changes to my skill. I also installed GitBash to my computer so I can more easily use GitHub and Travis CI. Once I had my accounts set up, I needed to actually code my skill. I found a template online that I was able to use to help me create my skill. I changed the general code to better fit my needs. Then, later on, I plan on publishing my skill to the Amazon Alexa store so that my friends and family will be able to use it as well. I have not done this yet, but I plan on doing so over the summer when I have more time to work on it.


#### Step 1: Come up with a plan

*Come up with a goal

I first had to come up with an idea for my skill. It is very hard to develop a skill if you do not know what you want it to do. 
There are many different examples of skills I could have created. The most popular skills are games, kid-friendly skills, content skills, music skills, and habit-forming skills. A game skill includes interactive adventures, quizzes, Jeopardy and The Spongebob Challenge. They are not much different than other video games I might see, but they are controlled exclusively by my voice. A kid-friendly skill is meant to engage kids to help them be creative and smarter thinkers. A content skill is a skill created to deliver content to people whether this be the weather or the news. Music skills play music for their customer. An example of a music skill would be Spotify or Sirius radio.  A habit forming skill is meant to help the user develop a routine, so it might remind the user daily to do something such as water the plants.

*Make an outline

First, I made flowcharts to show different utterances and their outcomes. I came up with several outcomes for more popular tasks and think of different ways people might ask to perform a certain task. Then I layed out everything I wanted my skill to be able to accomplish without worrying too much about how it all falls together. 

If you wanted  to include screens and visuals in your skill, it would be necessary to map out what I wanted on each screen as well. This includes the general visual elements as well as the functionality of each screen. This is not something I included in my product as my Alexa dot does not have a screen.

		ALEXA DECISION MAKER SKILL

		Invocations / Utterances:
		(All invocations do the same thing) Alexa...
		Give me an activity
		Tell me something to do
		Tell me an activity
		Outcomes:
		(Randomly chosen after Alexa says ‘Here is your activity: ‘)
		Go shopping
		Go bowling
		Go mini golfing
		Go to the movies
		Bake cookies
		Go for a drive
		Listen to music
		Go on a hike
		Go get ice cream ...

Since my skill is more simple in nature, it does not require a lot of forethought on what happens. It is fairly straightforward and explanatory through the name. The image above shows my original thought process when I first started developing my skill. 

#### Step 2: Solidify what I want to do

*Gather feedback

An important part of creating an Amazon Alexa skill is to gather feedback from its potential users.  This helped me minimize time I wasted while creating my skill, where I might be implementing something unnecessary, and I can use that time to implement something cool that the user may find more necessary. This is also a place to think about user functionality and ease of access in my skill. The main idea of this step is to avoid having to backstep and doing more work later on in my development process. It is easier to part with work and think about new ways to do things before I spend six hours working on it. It overall makes for a more cohesive and interactive skill as my final product. 

Since I created my skill for myself, I talked to people around me to get feedback on my skill. Since I was not making my skill for a client, I did not have to listen to their feedback with as much weight, but it is still a good idea to think about their feedback and incorporate it into my skill. 

*Incorporate feedback

Next, I had to use the feedback I got from the previous step to make changes to my flowchart. Depending on who I am creating the skill for, I can take more or less of the feedback into consideration depending on where I want to bring the skill. The table below shows my updated flowchart.

		ALEXA DECISION MAKER SKILL

		Invocations / Utterances:
		(All invocations do the same thing) Alexa...
		Give me an activity
		Tell me something to do
		Tell me an activity
		Question 1:
		(Are you willing to spend money?)
		     Answer 1:
		     (yes)
			  Question 2:
			  (Do you want to be inside or outside?)
			       Answer 1:
			       (inside)
				    Outcomes:
				    (Randomly selected and recited)
		Go shopping
		Go to a restaurant
			       Answer 2:
			       (outside)
				    Outcomes:
				    (Randomly selected and recited)
		Go mini golfing
		Go get ice cream
		     Answer 2:
		     (no)
			  Question 2:
			  (Do I want to be inside or outside?)
			       Answer 1:
			       (inside)
				    Outcomes:
				    (Randomly selected and recited)
		Make macaroni art
		Make a music video
			       Answer 2:
			       (outside)
				    Outcomes:
				    (Randomly selected and recited)
		Go on a hike
		Go swimming

#### Step 3: Set up my Developer Console

*Create my account

In order to create an Amazon Alexa skill, I needed to create an Amazon Developer account. 
In the top right corner of my screen will be a button that says sign in. Click this button, and since I did not have an account, I clicked Create my Amazon Developer account. I filled in my information under the Profile Information tab, and accepted and agreed to the terms and conditions on the App Distribution Agreement tab. Once I got to the Payments tab, I made sure that I had selected no for both of the options. I am agreeing by doing this that I will not be making any money through my skill, but I can always change this later. After I completed this step I had set up my developer account! It brought me to my Amazon Developer dashboard.
Set up my portal

Once I am in my portal, I am wanted to start creating my skill. I clicked the Skill Builders tab in the top left, and then the blue Start a Skill button. This brought me to the page where all of my skills are stored, so if I ever wanted to get back to a skill, I can access it in here.

I am going to create a new skill, so I clicked the create a skill button on the right. Here I decided my skill name. I called my skill alexa-decision-maker so it was easy to remember.

I also set my default language to be English (US) for the sake of this skill, as it is the language we will be programming the skill for.  It is important to note that this is the language I am coding my skill for now, but I can always add more language variances in the future. For skills I may create in the future, I am going to want to change the language to best suit the audience I am aiming my skill to be for, and I should have a good grasp of the language and its mannerisms to make sure that it makes sense to the user when they use my skill.

Next up, I chose a model to create my skill from. I decided to create my skill from a custom model. This gave me more control and variance from the beginning, however, the other models can be useful for other skills if I know that they cater well to what I am trying to accomplish.

The more specific models fill in some of the blanks for me by making my skill writing process mainly fill in the blank through the portal.

Lastly, I chose how I will be hosting my code. I selected the Provision my Own option. This means that I will be hosting my own code, rather than having Amazon do it for me. I will be making a Lambda function later that will fulfill this requirement for me. A Lambda function is the code I write that fulfills the backend of my skill. It is like the skeleton of the skill. Once I was confident that everything was correctly filled out, I scrolled back up to the top of the page and pressed the blue create skill button. 
Navigating the portal
The Amazon Developer Portal is where all of my code will be uploaded for my Alexa skill. This brought me to my home page, where a Skill builder checklist was shown to tell me what I have integrated into my skill so far. I did not have any checks yet, as I had not yet started creating the actual skill.

The next tab down is the Invocation tab. Here, I declared my skills invocation name.  In simpler terms, this is where I stated what my skill is called. Alexa listens for these phrases after her name, which she then encrypts and sends to Amazon before they take my skill and its response and send I my answer through Alexa.

Below the Invocation tab is the Intents tab. This is where my intents are stored. At this point, I had 5 intents that are required by Amazon. They each relate my custom skill back to Alexa's basic functionalities. Simply, and intent is an action my Alexa will take to fulfill the users request.
The AMAZON.CancelIntent lets the user cancel an intent or exit the skill entirely. The AMAZON.HelpIntent is an intent that gives the user help in general Amazon Alexa scope. The AMAZON.StopIntent allows the user to stop either the intent they invoked, or the skill in total. The AMAZON.FallbackIntent is an intent that gives the user an error message, when there is no code in the skill that responds to the users command. The AMAZON.NavigateHomeIntent brings the user back to the home screen on an Amazon Alexa with a screen. 
One example of an intent I added later is the GetNewActivityIntent. This is an intent I created to grab out invocations and start my skill. It is crucial for its functionality, but I added later with my code.
Here, I also saw my slots. A slot is added when choice is added to my skill. They are like variables I created. I did not have any slots at this point in my skill creation. They were added through the code for the skill. They made my skill work when I added more variables to my code.

#### Step 4: Set up my Amazon Web Services account

*Create my account

I needed an Amazon Web Services (AWS) account to be able to make my Lambda functions, which allows my Alexa skill to function. This is where I put the backend of my code. 

First, I filled in my email address, password, and account name.

Then, I filled out my account type, address, and phone number. My account type is a personal account. This means that I am not using my account through my company, educational institution, or any similar organization.

Next, I put in a payment plan. I did not use anything to require payment, but I still needed to input a form of payment. I then went on to verify my phone number and the create my account. I got a text with a code within a couple of minutes, which I then entered into the captcha, confirming I was real.

Once this was completed, I chose an AWS support plan. I am a true believer in all things simple, so I chose the free basic plan, as it is all any simple developer like me needs. Once this was completed, I got a confirmation email and I was ready to start coding!
Navigate to AWS Lambda

Once I signed in, I was greeted with the AWS management console. From here, in the top left corner of my screen, I selected the services drop down menu. I then found the Lambda service, which can be found under the compute section of services, or can be searched for at the top of the screen. This brought me to all of my AWS Lambda functions. 

At this step, I selected my AWS region to best fit the users of my skill. Since I live in North America, this was the US East (N. Virginia) option. There are other options that may be closer, but not all of the locations support Lambda. 
Once my region was properly selected, I created my first Lambda function! I pressed the orange Create Function button in the top right of my screen to start creating my function.

*Setup my Lambda function

I chose to author my function from scratch, and filled in the function name and runtime boxes. I made sure to use a meaningful function name, so I knew what my function would do. I chose to call my function activityDecider, because my skill decides on activities for me. It is commonplace for coders to leave the first letter of a variable as a lowercase, and capitalize the first letter of each subsequent word to make them easier to read.

I was also given a drop down list of options for possible runtimes I could choose from for my Lambda function. (A runtime is the language I will write my skill in). I chose to write my function in Python 3.6, so I chose that from the drop down menu. 
Under permissions, I chose to create a new role with basic Lambda permissions. Then, I created my function. Once I created my function, I saw a page that looked like this.

I scrolled down to the bottom of the page, where I saw a section called Execution Role. The first dropdown menu here asked me to choose a role that defines the permissions of my function. I chose to Use an existing role, and then chose service-role/lambda_basic_execution. I chose this role because it is pre-coded, and it works well for what I am trying to do. After I did this, I scrolled back up to the top of the screen and saved my changes. Then, I had the basis to lay my Lambda function.

#### Step 5: Set up my GitHub and Gitbash

*Create my GitHub account

GitHub is extremely useful for any developer, with any project. It is an online tool that makes it easier to collaborate with other people, have a system of version control, and in my case, push my code up into Amazon’s cloud. 

Creating a GitHub account is easy. In the top right corner of the GitHub screen, there is an option to Sign Up. I filled in my account name, email, and password on the first page, then continued to create my account.

On the second page, I chose the Free subscription, as it is perfect for an amatuer developer like me. I also chose to get updates from GitHub sent to my email, so I could stay up to date. Then, I pressed continue at the bottom of the page to proceed to the last step.
The last step of setting up my account relied totally off of my comfort in programming, and what I intend to use my GitHub account to do. When I created my account I filled it in as follows.

After I submitted this step, I verified my email, and then I had a GitHub account!

*Create a repository

Once I created my account, I was able to create a repository to hold my code for this particular project. A repository (repo for short) is like a folder or a library that will hold my code. It lets me see all the aspects of my project, as well as all the different versions of my project I committed. 

In the top right there was a drop down menu that has an option called my repositories. Clicking on that option brought me to my repositories. Alternatively, there was a tab I could click labeled Repositories near the top of my screen. Once at the repository page, I clicked the green new button, to create a new repository which brought me to a page that looked like this

I named my repository something memorable and short so I could remember what it does. I named my repository alexa-decision-maker because I created an Alexa decision maker. I then added a description about what my code does, not only for myself but also for anyone else who may stumble across my code. 

Below the description is the option to make my repository private or public. I decided to make my repo public for a couple of reasons. This not only allows me to call myself a open source contributor (fun name), but it also means I don’t have to pay for any of the software I used to create my skill.

I then had the option to have a README file generated with my repository. A README file lets anyone who might see my code know generally what it does and what is needed to get it to work. It is possible to add this later on, but I added it then, but did not type anything into it initially. 

Lastly, I needed to set the language for my .gitignore file, and add a license for my code. I chose python as my .gitignore language and the MIT License as my license. I chose python as my language because I am coding the rest of my skill in python. The MIT one works well for what we want. The MIT License works well because not only is it free to use, but it also has very few restrictions on reuse. I could then create my repository.

*Install GitBash

GitHub goes hand in hand with GitBash. GitBash is a downloadable tool that lets you easily push code up to github, as well as pull it down. It simulates a Linux environment as it has much of the same commands and nuances. It is what allows me to use GitHub.

I downloaded GitBash from the link above. Once it downloaded, I double clicked the download so I could open it. It asked me what license I would like to use, and I selected the GNU General Public License. Next, it asked me for a destination location, where it would install the program. I kept it as is, and continued. The next part was fun, because I got to select my components, or the frilly things to make my life easier in using GitBash. The following is what I chose to install based off the tutorial I was following.

I kept the Select Start Menu as is, and selected to Use Git from GitBash only as my path. I then chose to use Use the native Windows Secure Channel library as my Choosing HTTPS transport backend. To configure my window, I decided to select Checkout Windows as is, commit Unix-line endings as my configuration because I am used both windows and linux. I chose Use MinTTY (the default terminal or MSYS2) as my terminal emulator, and configured it to Enable file system caching. Once I run through this exhaustive checklist, I can then install and subsequently uncheck Launch Git Bash and View Release Notes and finish the installation. Half the reason I decided to go with these settings is because it is what the tutorial told me to do.

Once I had GitBash downloaded, I clicked on the desktop icon and typed
	git version 
which told me the version I was using. 

Once the correct version installed, I configured it to connect to my GitHub account. I typed the following commands to connect it to my account, filling in my information in place of the red text. 
	git config --global user.name "my Name"
	git config --global user.email "I@email.com"
I checked to see if I filled this in correctly using the following command.
	git config --global --list

#### Step 6: Start to code

*Install Pycharm

Pycharm is a program I used to write my programs. The main language supported by Pycharm is Python, but I can still write in different languages in it. It just may not catch any errors or be able to run, depending on the language.

Out of all the things I had to setup and install, Pycharm was the easiest. I downloaded the community file and double clicked on it to open it. I also pinned the program to my taskbar so it is easy to access. I also made sure I was using Python 3, as that is what my code is written in.

*Start my code

Once I had my GitHub and GitBash configured, it was time to start coding. Alexa apps are cool as in they accept many different languages of code. I chose to program my program in Python as it is the language I was most comfortable in, and out of all the programming languages I find it the easiest to follow, read, and explain. 

I did not create my code from scratch though, and I used somebody else's code to get me where I am. Since I did not focus on the code alone, it was the only way I would have actually gotten a working skill since there's so much to learn from the code alone. I used this tutorial to help me create my code originally. I went in and commented the code, and modified it to do what I needed it to do. I decided that I wanted to make my code more complicated later though, so I found more code on GitHub that I was able to use to help create my code. I was able to build my code off of these codes by forking their code, or taking a copy for myself.  I did this by clicking the fork button in the top right of the page. This created a new repository in my GitHub, including everything in my Alexa-Decision-Maker repository at that time. I could then make changes and modify this repository however I want without affecting the repository I forked from.

*How to pull code from GitHub

Pushing and pulling code is essential to using GitHub. I had forked the repository, but I had not yet pulled it down onto my computer to edit it. 

First, I needed a place to put the code I pulled. I went to my files on my computer and created a new folder called git as part of my quick access. This folder is where I store all of my GitHub projects, mainly for ease of access. In this folder, I created another folder called alexa-decision-maker. This is where all the files pertaining to the skill I forked went. 

Once I had created my folders, I opened up GitBash. I needed to pull the code from GitHub. The first step, was to clone the code. I was able to do this by pressing the green Clone or download button in my repository. This gave me a link which I copied to my clipboard.

Next, I went back to GitBash and navigated to the folder where I wanted to put the code. I did this by using cd and ls. cd on its own brings me back to my main desktop location and is useful when I need to get out of a folder and back to the start. I can also use cd {path} to navigate through my folders. The first command I did was cd git to navigate to the git folder I created. Next, I checked to see what folders I had in that section by saying ls. I saw that I had a folder called alexa-decision-maker, which I wanted to navigate to by saying cd alexa-decision-maker. This can be seen generally below.

Next I wanted to clone the repository onto my computer. I did this by typing
	git clone {link I copied}
This cloned the repository to my computer, but did not download it. To download it, I typed
	git pull origin master
	
To pull the code down. After this was done, the files in the repository were stored on my computer. I navigated back to the alexa-decision-maker folder I created to see the files. I opened them one by one there using Pycharm, or I could have gone to Pycharm and opened them all at once. I opened the folder itself, so I did not have to individually open every file, because that would have taken forever.

*How to push code to Github

Once I got the code from GitHub, I was able to modify it however I wanted. I went to the file called lamda_function.py and added an activity. This can be found around line 24 which can be seen in the sidebar.

The code shown below is a dictionary of all my activities, a dictionary being a group of answers or options the code will randomly draw from and refer back to. The activities are in the lists in brackets and are separated by commas and defined in quotations.

I made sure it corresponded to the category I added it to. Pycharm is nice and it autosaves as I am working, so I can just push my code to GitHub when I am ready to.

I navigated back to the folder where I put my code, alexa-decision-maker and typed 
	git status

This tells me the status of what is in the folder. It tells me what stayed the same and what changed. I saw that the alexa/lambda_funciton.py had been modified since it is in red.

Next, I added my changes to my ‘clipboard,’ so that they could be pushed up into my repository. To do this I typed
	git add .
It is important to include the . because it signifies to add all of the files that were changed. Next, I wanted to commit the files by typing
	git commit -am “message about change”
It is important to add a helpful change message so people looking at my repository can see the changes, as well as if I need to ever revert back to another version of my code. To finally push my code up to GitHub, I typed
	git push origin master
I am the origin master, because I am the one in charge of my repository. It is like my signature at the end of my work. To finish pushing my code, I needed to log into my GitHub account on GitBash to prove that I am the origin master.

Then, if I looked at my GitHub repository it will show that I modified some files.

I could see that the Alexa folder was modified because that is where the python file I modified is located. Putting my code on GitHub alone did not help me much in terms of publishing my skill though, because I needed to loop it back into my Amazon Developer account.

#### Step 7: Set up my Travis CI account

*Create Travis CI account

Travis CI helps to continually integrate software. In my case, I used it to push my code to Amazon Developer through GitHub. It is the middleman of these two accounts, and once it was working, all I had to do to put my skill on the developer portal was push it to GitHub.
I created a Travis CI account here. In the top right corner of the webpage is an option to sign in with GitHub, which I oh so conveniently have. I signed in with my GitHub and then I had a Travis CI account!

*Connect Travis CI account to my skill

I then went back to Pycharm, and opened a file called travis.yml, which looks like this.

I opened up my Amazon Developer Portal and navigated the endpoint tab of the portal, found near the bottom of the page. It should look like this.

Here, I found my Default Region. This tells Amazon that the code I am publishing belongs with my skill. I copied my default region and pasted it the default region or role found in the 25th line of code.

#### Step 8: Test my code

*Testing in Amazon Developer Console

Once I had my Travis CI connected to everything, I pushed my code again to get the process to happen. I could see if it worked in the Travis CI page. If it correctly works, once I pushed the skill I should see this.

If my skill is successfully pushed, it will turn green once it is done, but if it does not work, it will turn red meaning I have an error in my code. Once it is up, I was able to go back to the Amazon Developer Portal to test it.
At the top of the Amazon Developer Portal page, there is an option to Test my code. It brings me to a page that looks like this when I click on it.

In the bar, I could either type my invocation, or I could click on the microphone to the right to speak it. I typed, “Alexa, open activity decider” to open the skill and answered the questions she prompted me with. I didn't speak it because I’m self conscious and didn’t want my mom to judge me for talking to my computer. I was then given an activity to participate in from the list in my Python program.

#### Step 9: Refine my skill

*Gather more feedback

Once I had my skill up and running, it went through another round of feedback. This was where people would tell me minor modifications to add such as new activities, or another question to ask. The changes I made in this round were minor, as the bulk of my skill was already built, and I was just beautifying it. I also had bugs pointed out for me to fix in my code.

One way people gave me feedback was through my GitHub page. Next to the code tab, there is a tab called Issues. In this tab, people could leave suggestions or bugs that they thought should be fixed or implemented. I later was able to go in and sort the comments into things that needed to be done immediately and things that could be done over a longer span of time. I could also was able to sort them by what the comment was asking me to do, such as by bug, question, enhancement, etc. 

*Incorporate feedback

I then took the new feedback I acquired and took it into account. I went through the fixes and additions in an order that I thought made sense, and fixed the most pressing matters first. 

Since I made the program for myself, it was not as important that I incorporate everything in a timely manner, like I would have if I were making the program for someone else. The only thing I had to be aware of is my ever-approaching exhibition date.

#### Step 10: Publish my skill

I have not yet published my skill, but in the future, like possibly over the summer, this is something I will do. It just did not make sense for me to publish it before exhibitions with how much I still needed to get done at that point.
Skill guidelines

Amazon has guidelines that they like all the skills on their store to follow, so it is important that my skill will follow these guidelines. There are a lot of different subsets of guidelines, and I would not be able to publish my skill if it violated any of them.
Sending my skill to Amazon

To publish my skill to the Alexa store, I first will navigate to the Alexa Developer Console. In the top bar, there is a tab called Distribution which lets you publish and distribute your skill.

I will fill in the subsections relating to the nature of my skill, and go through the checklist as it prompts I to. Once I have done this I will  have sent my skill to be reviewed.

My skill will be reviewed by a team at Amazon to make sure it follows the guidelines, and assuming it does, it will be live in just 1.5 to 2 weeks! If it does not follow the guidelines, it will be rejected, and I will have to modify it to fit the guidelines. 

#### Reflection:

There are a lot of different types of Amazon Alexa skills, and I only hit on one in this tutorial, because it is the type of skill I focused on for my project. I made a decision tree skill because my skill takes input from the user, but I also could have made a quiz game, trivia game, kid friendly skill, content skill, music skill, or a habit forming skill. I chose to do a decision tree because I thought it would challenge me to have more than one interaction with Alexa, and also because I thought it would be cool to create a skill that would help me make decisions. The fact that it took me four months to come up with my skill idea can attest to that.

I got to use the general app development process in the general creation of my skill because I tried to follow it when I was creating my skill. I went through the process of gathering input from others and drafting out my skill, as well as taking the feedback I got from Mobiquity and ADP about good coding practices. I ended up using blueprints for my Alexa app like Mobiquity suggested because I did not have a lot of time to create my skill, as creating a skill and learning all the language needed to create a skill like mine would have taken me at least a year doing it without a team. I was able to learn from the blueprints because I would go back and comment them so I knew what each part did, and I was able to save a lot of time there. 

I also really realized that programming is really just knowing how to google things effectively. My dad had been telling me this for years, and the Galactica team at ADP told me even they google things constantly throughout the work day. Being a good programmer is not as much about knowing the most code, but it is about knowing how to effectively solve problems, of which one way is googling and looking at other people's code.

As far as my skill itself goes, I tried to keep it sounding as natural as possible because that helps to increase engagement. I would say things out loud and make sure that it did not sound like I was writing a paper with the things I was having Alexa iterate. I tried to make her talk like any normal human would talk, often incorporating “slang” and cultural syntaxes to make it sound natural.
My original plan definitely got completely flipped upside down, but I am excited with what I have done. I think it is super cool and useful to be able to use the tools I used in my development for any type of coding in particular, and I know I will find them useful later on in my life and in my career.
