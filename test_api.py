import urllib.request
import json

url = 'http://localhost:9696/predict'

lead = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
}

data = json.dumps(lead).encode('utf-8')
l
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode('utf-8'))

print("API response:", result)
print(f"Rounded probability: {round(result['conversion_probability'], 3)}")