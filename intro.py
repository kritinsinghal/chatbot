import random

name = "Naem-of-Chatbot"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": [
  	"my name is {0}".format(name), #Response1
  	"People call me by {0}".format(name),
  	"I go by {0}".format(name) ],
  "what's today's weather?": [
  	"the weather is {0}".format(weather), #Response2
  	"It's {0} today".format(weather) ],
  "default": [ "default message" ] # default response
}


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message
