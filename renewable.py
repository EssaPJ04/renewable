from astral import LocationInfo
from astral.sun import sun
import pytz
from datetime import datetime

def get_sun_times():
    # User input
    name = input("Enter Location : ")
    region = input("Enter Country or Region (e.g., India): ")
    latitude = float(input("Enter latitude : "))
    longitude = float(input("Enter longitude : "))
    date_str = input("Enter date (eg : 20 July 2025): ")

    # Convert string date to date object
    date = datetime.strptime(date_str, "%d %B %Y").date()

    # Fixed timezone
    timezone = "Asia/Kolkata"  

    # Create location object
    city = LocationInfo(name, region, timezone, latitude, longitude)

    # Get sun times
    s = sun(city.observer, date=date, tzinfo=pytz.timezone(timezone))

    # Format and output
    sunrise = s['sunrise'].strftime("%I:%M %p")
    sunset = s['sunset'].strftime("%I:%M %p")
    day_length = s['sunset'] - s['sunrise']

    print("\n\tSolar Information\n")
    print("----------------------------------------\n")
    print(f"Location: {name}, {region}")
    print(f"Date: {date.strftime('%d %B %Y')}")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")
    print(f"Day Length: {day_length}")

# Run it
get_sun_times()
