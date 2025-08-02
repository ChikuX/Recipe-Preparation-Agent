import requests

API_KEY = "<your API key>" # Example: API_KEY = 0hTzmyGnDje7lf0gd********OoCuOeIeCht6XAfKM
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token', 
    data={
        "apikey": API_KEY,
        "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
    }
)

mltoken = token_response.json()["access_token"]

header = {
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer ' + mltoken
}

payload_scoring = {
    "messages": [
        {
            "content": "I'm looking for a quick dinner idea using tomatoes and pasta. Can you suggest a few options?",
            "role": "user"
        }
    ]
}

response_scoring = requests.post(
    'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/30d7f88c-1477-40dc-a32f-68983665b4f3/ai_service_stream?version=2021-05-01',
    json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken}
)

print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
