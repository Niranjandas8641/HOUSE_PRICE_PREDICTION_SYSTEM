from flask import Flask, request, jsonify, render_template
from src.predict import predict_single
from src.location_api import LocationAPI

app = Flask(__name__)

location_api = LocationAPI()


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# PREDICTION API
# =========================
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get data from webpage
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        # ---------------------------------
        # Default coordinates
        # ---------------------------------
        lat = 47.72
        lon = -122.32

        # ---------------------------------
        # Get address from webpage
        # ---------------------------------
        address = data.get("address")

        if address:

            try:
                result = location_api.get_coordinates_from_address(address)

                if result:
                    result_lat, result_lon = result

                    # Only use coordinates if they are valid
                    if result_lat is not None and result_lon is not None:

                        lat = float(result_lat)
                        lon = float(result_lon)

                        print("Latitude:", lat)
                        print("Longitude:", lon)

                        try:
                            distance = location_api.get_distance_to_city_center(
                                lat,
                                lon
                            )

                            print(
                                "Distance from city center:",
                                distance
                            )

                        except Exception as distance_error:
                            print(
                                "Distance calculation error:",
                                distance_error
                            )

            except Exception as location_error:

                print(
                    "Location API error:",
                    location_error
                )

                print(
                    "Using default coordinates."
                )

        # ---------------------------------
        # Create house data
        # ---------------------------------
        house = {

            "bedrooms": float(
                data.get("bedrooms", 3)
            ),

            "bathrooms": float(
                data.get("bathrooms", 2)
            ),

            "sqft_living": float(
                data.get("sqft_living", 1800)
            ),

            "sqft_lot": float(
                data.get("sqft_lot", 6000)
            ),

            "floors": float(
                data.get("floors", 1)
            ),

            "waterfront": int(
                data.get("waterfront", 0)
            ),

            "view": int(
                data.get("view", 0)
            ),

            "condition": int(
                data.get("condition", 3)
            ),

            "grade": int(
                data.get("grade", 3)
            ),

            "sqft_above": float(
                data.get("sqft_above", 1800)
            ),

            "sqft_basement": float(
                data.get("sqft_basement", 0)
            ),

            "yr_built": int(
                data.get("yr_built", 2000)
            ),

            "yr_renovated": int(
                data.get("yr_renovated", 0)
            ),

            "zipcode": int(
                data.get("zipcode", 98125)
            ),

            "lat": float(lat),

            "long": float(lon)
        }

        print("House data:")
        print(house)

        # ---------------------------------
        # Make prediction
        # ---------------------------------
        prediction = predict_single(house)

        print(
            "Predicted house price:",
            prediction
        )

        # ---------------------------------
        # Send result to webpage
        # ---------------------------------
        return jsonify({

            "prediction": round(
                float(prediction),
                2
            )

        })

    except ValueError as e:

        print(
            "VALUE ERROR:",
            e
        )

        return jsonify({

            "error": "Please enter valid numeric values."

        }), 400

    except Exception as e:

        print(
            "ERROR:",
            e
        )

        return jsonify({

            "error": str(e)

        }), 400


# =====================================
# START FLASK SERVER
# =====================================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )