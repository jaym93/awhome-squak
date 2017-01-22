# File: server.py
# Author: Jayanth M (jayanth6@gatech.edu)
# Created: 23-12-2016 12:48 PM
# Project: squak
# Description:  This file is a Flask server that recieves requests in JSON format and
#               posts to Slack as the Bot user 'Squak Event Logger'.
#               Sample messages format:
#                 messages = [{
#                     "title": "Sample danger message",
#                     "text": "This is a message that requires high priority",
#                     "pretext": "This is a message that requires high priority",
#                     "level": "danger",
#                     "desc": "This is the description of first sample event"
#                 }, {
#                     "title": "Sample warning message",
#                     "text": "This is a message that requires medium priority",
#                     "pretext": "This is a message that requires medium priority",
#                     "level": "warning",
#                     "desc": "This is the description of second sample event"
#                 }, {
#                     "title": "Sample success message",
#                     "text": "This is a message that requires low priority",
#                     "pretext": "This is a message that requires low priority",
#                     "level": "success",
#                     "desc": "This is the description of third sample event"
#                 }, {
#                     "title": "Sample info message",
#                     "text": "This is a message that requires no action",
#                     "pretext": "This is a message that requires no action",
#                     "level": "info",
#                     "desc": "This is the description of fourth sample event"
#                 }, {
#                     "title": "Sample other message",
#                     "text": "This is a message that is used for other notifications",
#                     "pretext": "This is a message that is used for other notifications",
#                     "level": "other",
#                     "desc": "This is the description of fifth sample event"
#                 }, {
#                     "title": "Sample default message",
#                     "text": "This is a message displayed by default",
#                     "pretext": "This is a message displayed by default",
#                     "level": "xyz",
#                     "desc": "This is the description of sixth sample event"
#                 }]


from flask import Flask, request
import http.client
import json

from tokens import *    # This file contains API tokens for Slack. Not synchronized to VCS.

app = Flask(__name__)

def decode_color(level):
    if level == 'danger':
        return '#ef4438'
    elif level == 'warning':
        return '#fec110'
    elif level == 'success':
        return '#49b050'
    elif level == 'info':
        return '#4690cd'
    elif level == 'other':
        return '#9C27B0'
    else:
        return '#9E9E9E'


@app.route('/api/post_message', methods=['POST'])
def post_message():
    #content = request.get_json(silent=True)
    messages = json.loads(request.data.decode("utf-8"))
    webhook_url = "https://hooks.slack.com/services/" + HOOK_ID
    headers = {'Content-Type': 'application/json'}
    for message in messages:
        payload = {
            'username': 'Squak Event Logger',
            'fallback': message['text'],
            'pretext': message['text'],
            'color': decode_color(message['level']),
            'channel': '#event_log',
            'fields': [
                {
                    'title': message['title'],
                    'value': message['desc'],
                    'short': False
                }
            ]
        }
        connection = http.client.HTTPSConnection('hooks.slack.com')
        connection.request('POST', webhook_url, json.dumps(payload), headers)
        # print(json.dumps(payload))
        response = connection.getresponse()
        # print(response.read().decode())
    return "Success" + response

    # print(uuid)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
