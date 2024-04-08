import openai
import os 
import pprint

'''Pass secret key'''
openai.api_key = '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'


'''setting model expectations and response'''

response = openai.chat.completions.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role':'system','content' : 'You are an AI assistant that can help with studying'},
    {'role':'user','content':'I want to learn about biology'},
    {'role':'assistant','content':'Hello, that is great. What would you like to know about biology'}
  ]
)

messages = response['choices'][0]['message']['content']

'''Creating chatbot'''

def chatbot():
 
  global messages
 
  while True:
    pprint.pprint(messages)
    user_input = input(str('User:'))
    messages = chat_update(messages,'user',user_input)
    messages = chat_update(messages,'assistant',query_response(messages))
  
    if user_input == 'exit':
      break


'''function to store and update chat'''

def chat_update(messages,role,content):
  messages.append({'role':role,'contents':content})
  return messages

def query_response(messages):
  response = openai.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = messages 
  )

  return response['choices'][0]['message']['content']



if __name__ == '__main__':
  print('Please talk to your chatbot','enter exit to stop')
  chatbot()


