import pandas as pd
import joblib


model = joblib.load(
    "models/house_price_model.pkl"
)


features = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "grade",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
    "zipcode",
    "lat",
    "long"
]


input_file = "data/housing.csv"


data = pd.read_csv(input_file)


predictions = model.predict(
    data[features]
)


data["predicted_price"] = predictions


data.to_csv(
    "batch_predictions.csv",
    index=False
)


print(
    "Batch predictions saved successfully!"
)

print(
    "File: batch_predictions.csv"
)