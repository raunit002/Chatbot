import requests

# Set the base URL for the Flask app
base_url = 'http://127.0.0.1:5000/'

# Define the message to send to the chatbot
message = 'I have blood cancer 2th stage.'

# Create the payload as a dictionary
payload = {'message': message}

# Send a POST request to the chat endpoint
response = requests.post(f'{base_url}/chat', json=payload)

# Get the response data as JSON
response_data = response.json()

# Print the chatbot's response
print('ChatGPT:', response_data['message'])
