import time,json,requests
import os
from slackclient import SlackClient

# get the Slack API token as an environment variable
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_NAME = "test2"
BOT_ID = "U53TE8XSS"

SLACK_BOT_NAME = "<@" + BOT_ID + ">"

def main():
    print(SLACK_BOT_NAME)
    # Create the slackclient instance
    sc = SlackClient(SLACK_BOT_TOKEN)

    response = requests.get("http://www.omdbapi.com/?t=The+Dark+Knight&plot=full")

    data = response.json()

    # Connect to slack
    if sc.rtm_connect():
        # Send first message
        #sc.rtm_send_message(CHANNEL_NAME, "I'm ALIVE!!!")

       while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                print(message, user)

                if(message and user):
                    if(SLACK_BOT_NAME in message):
                        print("done!")
                        sc.rtm_send_message(CHANNEL_NAME, data["Plot"])
                        sc.rtm_send_message(CHANNEL_NAME, sc.api_call("users.list"))
                    else:
                        sc.rtm_send_message(CHANNEL_NAME, "")
                        

if __name__ == '__main__':
    main()