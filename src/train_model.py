import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


data = pd.read_csv("data/cleaned_house_data.csv")


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


X = data[features]

y = data["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


models = {

    "Linear Regression":
        LinearRegression(),

    "Decision Tree":
        DecisionTreeRegressor(
            random_state=42
        ),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )
}


results = []

best_model = None

best_score = float("-inf")


for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)


    r2 = r2_score(
        y_test,
        predictions
    )


    mae = mean_absolute_error(
        y_test,
        predictions
    )


    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5


    print("\nModel:", name)

    print("R2:", r2)

    print("MAE:", mae)

    print("RMSE:", rmse)


    results.append({

        "Model": name,

        "R2": r2,

        "MAE": mae,

        "RMSE": rmse

    })


    if r2 > best_score:

        best_score = r2

        best_model = model


results_df = pd.DataFrame(results)


results_df.to_csv(
    "model_results.csv",
    index=False
)


joblib.dump(
    best_model,
    "models/house_price_model.pkl"
)


print("\n==============================")

print("Best model saved!")

print("Best R2:", best_score)

print("==============================")