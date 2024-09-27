"""practice file"""


def get_weather_report() -> str:
    weather: str = input("What is the Weather?")
    if weather == "cold" or weather == "rainy":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I dont recognize this weather")
    return weather


get_weather_report()
