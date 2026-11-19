
# Example free API usage
# - AviationStack


# create api key
# https://aviationstack.com/ 
# pip install requests


    
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(source, destination, departure_date):

    if not API_KEY:
        return "Error: AVIATIONSTACK_API_KEY not found."

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        flights = []

        if "data" not in data or len(data["data"]) == 0:
            return (
                f"No flight data found.\n"
                f"Requested Route:\n"
                f"From: {source}\n"
                f"To: {destination}\n"
                f"Date: {departure_date}"
            )

        for flight in data["data"][:5]:

            airline = flight.get("airline", {}).get("name", "Unknown")

            departure = flight.get("departure", {}).get(
                "airport", "Unknown"
            )

            arrival = flight.get("arrival", {}).get(
                "airport", "Unknown"
            )

            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
Airline : {airline}
Departure Airport : {departure}
Arrival Airport : {arrival}
Status : {status}
"""
            )

        return "\n".join(flights)

    except Exception as e:
        return f"Flight API Error: {e}"