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
               
                movieName = message[13:]
                        if(len(movieName.strip()) == 0):
                            sc.rtm_send_message(channel, "This won't work without a movie name!")
                        else:
                            try:
                                url = "http://www.omdbapi.com/?t="+message[13:]
                                response = requests.get(url)
                                print url
                                if response.status_code==200:
                                    data = response.json()
                                    sc.rtm_send_message(channel, data["Title"])
                                    sc.rtm_send_message(channel, data["Actors"])
                                    sc.rtm_send_message(channel, data["Released"])
                            except:
                                print("api_call error")
                                sc.rtm_send_message(channel, "Hey "+"<@"+user+"> !"+" I couldn't find this movie")

                        # sc.rtm_send_message(CHANNEL_NAME, sc.api_call("users.list"))
                    else:
                        sc.rtm_send_message(channel, "")


if __name__ == '__main__':
    main()