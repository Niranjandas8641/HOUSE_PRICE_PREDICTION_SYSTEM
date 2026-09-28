from src.predict import predict_single


house = {
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 1800,
    "sqft_lot": 6000,
    "floors": 1,
    "waterfront": 0,
    "view": 0,
    "condition": 3,
    "grade": 3,
    "sqft_above": 1800,
    "sqft_basement": 0,
    "yr_built": 2000,
    "yr_renovated": 0,
    "zipcode": 98125,
    "lat": 47.72,
    "long": -122.32
}


price = predict_single(house)

print("Predicted house price:", price)