import ollama

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Please generate poem about blue sky?',
  },
])
print(response['message']['content'])
