import pickle

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41
}

with open('pipeline.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

X = dv.transform([lead])

y_pred = model.predict_proba(X)[:, 1]

prob_conversion = y_pred[0]
rounded_prob = round(prob_conversion, 3)

print(f"Conversion probability: {rounded_prob}")
