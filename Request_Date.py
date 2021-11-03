import requests

url = "https://apigw.singaporeair.com/api/v1/commercial/flightavailability/get"

def searchSite(payload):
#  payload = "{\r\n\t\"clientUUID\":\"SQ-API-Booking-Aggregator\",\r\n\t\"request\":{\r\n   \t  \t\"itineraryDetails\":[  \r\n   \t  \t\t{  \r\n\t            \"originAirportCode\":\"SIN\",\r\n\t            \"destinationAirportCode\":\"PER\",\r\n\t\t        \"departureDate\":\"2020-10-04\",\r\n\t\t        \"returnDate\":\"2020-10-04\"\r\n\t         }\r\n\t    ],\r\n\t    \"cabinClass\":\"Y\",\r\n\t    \"adultCount\":1,\r\n\t    \"childCount\":0,\r\n\t    \"infantCount\":0\r\n\t}\r\n,\r\n\t    \"flexibleDates\":\"false\"}"
  headers = {
    'Content-Type': 'application/json',
    'apikey': '<insert own API here>'
  }

  response = requests.request("POST", url, headers=headers, data = payload)

  response_dict = response.json()

  #print(json.dumps(response_dict, indent = 4, sort_keys=True))

  return response_dict