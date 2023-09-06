import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests

# xoxb token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

#currently, a dummy endpoint 
#to be replaced later
url = "https://reqres.in/api/users"

#handle_mention is called when app is mentioned in a channel it is a part of
@app.event("app_mention")
def handle_mention(body, say, logger):
    #data will be a json object with the channel name, and all other information necessary to get a summary of the channel
    data = {}
    response = requests.post(url, json=data)
    try:
        json_response = response.json()
        dict_response = json_response.dumps()
        #continue to parse the json the way you need it and then send appropriate emessage using the say function
    except ValueError:
        print("Invalid JSON response")
    #can replace hi with some other response using the dict_response summary values    
    say(f"Hi.")

if __name__ == "__main__":

    #xapp token
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
