import os
from slackclient import SlackClient

"""
Returns the id of the movie slackbot

"""


SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
BOT_NAME = 'moebot'

bot_found = False

try:
	slack_client = SlackClient(SLACK_BOT_TOKEN)
except:
	print "Connection error"

	#calling the api to get a list of all users in your Slack team
api_call = slack_client.api_call("users.list")

if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        if 'name' in user and user.get('name') == BOT_NAME:
            bot_found = True
            break
        else:
        	continue

if bot_found:
	print "Bot ID for '" + user['name'] + "' is " + user.get('id')
	#return str(user.get('id'))
else:
	print "could not find bot user with the name " + BOT_NAME
	#return ""


