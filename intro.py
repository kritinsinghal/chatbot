name = "Naem-of-Chatbot"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name), #Response1
  "what's today's weather?": "the weather is {0}".format(weather), #Response2
  "default": "default message" # default response
}


def respond(message):
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]
    return bot_message
