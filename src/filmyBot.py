import time,json,requests
import os
from slackclient import SlackClient

# get the Slack API token as an environment variable
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
BOT_ID = "U53TE8XSS"

SLACK_BOT_NAME = "<@" + BOT_ID + ">"

def main():
    # print(SLACK_BOT_NAME)
    # Create the slackclient instance
    sc = SlackClient(SLACK_BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():
        # Send first message
        #sc.rtm_send_message(CHANNEL_NAME, "I'm ALIVE!!!")

       while True:
            # Listen for any latest events
            for slack_event in sc.rtm_read():
                # message = slack_message.get("text")
                # user = slack_message.get("user")
                #print(message, user)

                message = slack_event.get("text")
                user = slack_event.get("user")
                channel = slack_event.get("channel")

                if(message and user):
                    if(SLACK_BOT_NAME in message):
                        #print("done!")
                       
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
                                    #print(data)
                                    # sc.rtm_send_message(channel, data["Title"])
                                    # sc.rtm_send_message(channel, data["Actors"])
                                    # sc.rtm_send_message(channel, data["Released"])
                                    intro_msg  = json.dumps([{
                                                        "fallback": "There seems to be some issue with displaying the data",
                                                        "title": message[13:],
                                                        "color":"#50e043",
                                                        "attachment_type": "default",
                                                        "text": data["Plot"],
                                                        "fields":[
                                                                        {
                                                                            "title": "Title",
                                                                            "value": data["Title"],
                                                                            "short": True
                                                                        },
                                                                        {
                                                                            "title": "Actors",
                                                                            "value": data["Actors"],
                                                                            "short": True
                                                                        },
                                                                        {
                                                                            "title": "Released",
                                                                            "value": data["Released"],
                                                                            "short": True
                                                                        },
                                                                        {
                                                                            "title": "Rated",
                                                                            "value": data["Rated"],
                                                                            "short": True
                                                                        }
                                                                    ],
                                                        }])
                                    sc.api_call("chat.postMessage", channel=channel, text="Here is some information about "+message[13:], attachments=intro_msg, as_user=True)
                            except:
                                print("api_call error")
                                sc.rtm_send_message(channel, "Hey "+"<@"+user+"> !"+" I couldn't find this movie")

                        # sc.rtm_send_message(CHANNEL_NAME, sc.api_call("users.list"))
                    else:
                        sc.rtm_send_message(channel, "")

                time.sleep(0.5)


if __name__ == '__main__':
    main()