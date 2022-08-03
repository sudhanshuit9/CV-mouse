import re

import long_responses as long

def message_probability(user_message, recognised_words,  single_response=false,  required_words=[]):
    message_certainly = 0
    has_required_words = True

def get_response(user_input):
  split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
  response = check_all_messages(split_message)
  return  response

# Testing the response system
while True:

       print('Bot:' + get_response(input('You:')))
