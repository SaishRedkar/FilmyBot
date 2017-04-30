import time,json,requests
import os
from slackclient import SlackClient

# get the Slack API token as an environment variable
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
# this is the bot id obtained from running the get_botid.py script
BOT_ID = "U53TE8XSS"

SLACK_BOT_NAME = "<@" + BOT_ID + ">"

def main():
    sc = SlackClient(SLACK_BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():
       while True:
            # Listen for any latest events
            for slack_event in sc.rtm_read():

                message = slack_event.get("text")
                user = slack_event.get("user")
                channel = slack_event.get("channel")

                if(message and user):
                    if(SLACK_BOT_NAME in message):
                       
                        movieName = message[13:]
                        if(len(movieName.strip()) == 0):
                            sc.rtm_send_message(channel, "I need a movie name to work with.")
                        else:
                            try:
                                url = "http://www.omdbapi.com/?t="+message[13:]
                                response = requests.get(url)
                                if response.status_code==200:
                                    data = response.json()
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
                                                                        },
                                                                        {
                                                                            "title": "IMDB Rating",
                                                                            "value": data["Ratings"][0]["Value"],
                                                                            "short": True
                                                                        },
                                                                         {
                                                                            "title": "Rotten Tomatoes Rating",
                                                                            "value": data["Ratings"][1]["Value"],
                                                                            "short": True
                                                                        }
                                                                    ],
                                                        "image_url": data["Poster"]
                                                        }])
                                    sc.api_call("chat.postMessage", channel=channel, text= "Hey "+"<@"+user+"> !" + "Here is some information about "+message[13:], attachments=intro_msg, as_user=True)
                            except:
                                sc.rtm_send_message(channel, "Hey "+"<@"+user+"> !"+" I couldn't find this movie. Try some other movie.")

                    else:
                        sc.rtm_send_message(channel, "")


if __name__ == '__main__':
    main()
