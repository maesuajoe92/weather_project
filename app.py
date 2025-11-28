import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()


    temp = data["current_condition"][0]["temp_C"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]


    return temp, condition



def main():
    city = input("Enter city name: ")
    temp, condition = get_weather(city)
    print(f"The current temperature in {city} is {temp}°C\nCondition: {condition}.")


if __name__ == "__main__":
    main()
    