import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# This sample slack application uses SocketMode
# For the companion getting started setup guide,
# see: https://docs.slack.dev/tools/bolt-python/getting-started

# Initializes your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/helloworld")
def message_hello_world(ack,say):
    ack()
    response = "hello world this is rehan this side with the help of app"
    say(f"{response}!")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
