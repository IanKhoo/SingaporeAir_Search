import Request_Date
import pprint
import datetime

flight_dates = []
#Search from Today
td = datetime.date.today()

#range(#): # = number of days in the future to search
for i in range(20):
    insert_date = td + datetime.timedelta(days=i)
    flight_dates.append(insert_date.isoformat())

#Change airport codes to search for flights from-to different destinations
originAirport = "SIN"
destinAirport = "PER"

flights_available = {}

for flight_date in flight_dates:
    departureDate = returnDate = flight_date

    payload = "{\r\n\t\"clientUUID\":\"SQ-API-Booking-Aggregator\",\r\n\t\"request\":{\r\n   \t  \t\"itineraryDetails\":[ " \
              " \r\n   \t  \t\t{  \r\n\t            \"originAirportCode\":\""+originAirport+"\",\r\n\t            " \
              "\"destinationAirportCode\":\""+destinAirport+"\",\r\n\t\t        \"departureDate\":\""+departureDate+"\"\r\n\t\t        }" \
              "\r\n\t    ],\r\n\t    \"cabinClass\":\"Y\",\r\n\t    " \
              "\"adultCount\":1,\r\n\t    \"childCount\":0,\r\n\t    \"infantCount\":0\r\n\t}\r\n,\r\n\t    " \
              "\"flexibleDates\":\"false\"} "

    response_dict = Request_Date.searchSite(payload=payload)

    flights_available.update({flight_date : {'date': flight_date, 'status':response_dict["status"] } })

#Output
pprint.pprint (flights_available)

