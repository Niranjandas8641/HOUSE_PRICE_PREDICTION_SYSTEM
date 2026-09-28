import joblib
import pandas as pd


MODEL_PATH = "models/house_price_model.pkl"


model = joblib.load(MODEL_PATH)


FEATURES = [
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


def predict_single(data):

    input_data = pd.DataFrame(
        [data],
        columns=FEATURES
    )

    prediction = model.predict(input_data)

    return prediction[0]