import math
import requests


class LocationAPI:

    def __init__(self):

        self.user_agent = "house-price-prediction-project"


    def get_coordinates_from_address(self, address):

        url = "https://nominatim.openstreetmap.org/search"


        params = {

            "q": address,

            "format": "json",

            "limit": 1

        }


        headers = {

            "User-Agent": self.user_agent

        }


        try:

            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=10
            )


            response.raise_for_status()


            results = response.json()


            if not results:

                return None, None


            latitude = float(
                results[0]["lat"]
            )


            longitude = float(
                results[0]["lon"]
            )


            return latitude, longitude


        except Exception as e:

            print(
                "Geocoding error:",
                e
            )

            return None, None


    def get_distance_to_city_center(
        self,
        latitude,
        longitude
    ):

        # Seattle city center
        center_lat = 47.6062

        center_lon = -122.3321


        return self.haversine_distance(

            latitude,

            longitude,

            center_lat,

            center_lon

        )


    def haversine_distance(
        self,
        lat1,
        lon1,
        lat2,
        lon2
    ):

        radius = 3958.8

        lat1 = math.radians(lat1)

        lat2 = math.radians(lat2)

        delta_lat = math.radians(
            lat2 - lat1
        )

        delta_lon = math.radians(
            lon2 - lon1
        )


        a = (

            math.sin(delta_lat / 2) ** 2

            +

            math.cos(lat1)

            * math.cos(lat2)

            * math.sin(delta_lon / 2) ** 2

        )


        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )


        return radius * c


    def get_amenities_score(
        self,
        latitude,
        longitude
    ):

        # Simple placeholder score.
        # Can later be replaced by a real
        # nearby-amenities API.

        distance = self.get_distance_to_city_center(
            latitude,
            longitude
        )


        if distance <= 3:

            return 10

        elif distance <= 7:

            return 8

        elif distance <= 15:

            return 6

        elif distance <= 25:

            return 4

        else:

            return 2