# FilmyBot
A Slack bot for getting movie information while communicating using Slack

# Tools
- Python 2 or 3
- pip and virtualenv
- [The Python slackclient](https://github.com/slackapi/python-slackclient)
- [A Slack account with an API token](https://api.slack.com/)

# Setting up the environment
First, [fork the main repo](https://github.com/SaishRedkar/FilmyBot). Then clone the forked repository on your local machine

    git clone https://github.com/YourName/FilmyBot.git
    
Navigate to the directory and create a new virtual environment
    
    virtualenv botvenv
    
Activate the virtual environment
    
    source botvenv/bin/activate

Then install the Python slackclient library with the pip command
    
    sudo pip install slackclient
    
The next step is to create a bot user for our Slack team and obtain the API access token.

Create a new bot user by following the [create a new bot user](https://my.slack.com/services/new/bot) instructions on the [Bot Users pages](https://api.slack.com/bot-users)

Copy the bot API access token and export is an environment variable named SLACK_BOT_TOKEN

        export SLACK_BOT_TOKEN='your Slack API token'

# Getting the bot ID
Run the get_botid.py script to get the bot ID. In the script, change the value of 'BOT_NAME' to the name of the bot that you created. 
    
    python get_botid.py

The id returned by this script is your bot ID which you'll be using in the filmyBot.py script to start the Slack bot.

# Running Filmybot in your Slack channel
After setting the bot id in the filmyBot.py script, run the following

        python filmyBot.py
 
Invite the Filmybot in your Slack channel

Run the Filmybot as follows

![](https://media.giphy.com/media/ATHbDClEEA1m8/giphy.gif)


