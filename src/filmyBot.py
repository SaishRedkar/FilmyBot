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

    error_msg  = json.dumps([{
                            "color":"#e74c3c",
                            "attachment_type": "default",
                            "text": "",
                            "image_url":"http://i2.kym-cdn.com/photos/images/original/000/329/784/bd6.jpg"                            
                            }])

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
                            sc.api_call("chat.postMessage", channel=channel, text="", attachments=error_msg, as_user=True)
                        else:
                            try:
                                url = "http://www.omdbapi.com/?t="+message[13:]
                                response = requests.get(url)                                
                                if response.status_code==200:
                                    data = response.json()
                                    print "Calling "+url
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
                                                                            "title": "IMDB Ratings",
                                                                            "value": data["Ratings"][0]["Value"],
                                                                            "short": True
                                                                        }                                                                
                                                                    ],
                                                        "image_url": data["Poster"]
                                                        }])
                                    sc.api_call("chat.postMessage", channel=channel, text="Here is some information about "+message[13:], attachments=intro_msg, as_user=True)
                            except:
                                sc.rtm_send_message(channel, "Hey "+"<@"+user+"> !"+" I couldn't find this movie")
        
                    else:
                        sc.rtm_send_message(channel, "")


if __name__ == '__main__':
    main()
