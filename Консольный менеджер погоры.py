from apikey import API_TOKEN #you need an api token
import requests

params = {
    'q': input("Введите ваш город: "),
    'appid': API_TOKEN,
    'units': 'metric',
    'lang': 'RU'
}

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    data = response.json()


    print(f"Температура в городе {params['q'].capitalize()} : {data['main']['temp']}°C , {data["weather"][0]['description']}.")
    print(f"Ощущается как : {data["main"]['feels_like']}°C")
    print(f"Минимальная температура сегодня : {data['main']['temp_min']}°C. Максимальная температура : {data['main']['temp_max']}°C")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе: {e}")
except KeyError as e:
    print(f"Ошибка в структуре данных: {e}")