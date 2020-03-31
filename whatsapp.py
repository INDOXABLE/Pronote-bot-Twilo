import flask
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)

@app.route('/bot’, methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    