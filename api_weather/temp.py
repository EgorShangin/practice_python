import argparse
import requests
import sys

#city = sys.argv[1] #параметр запуска, позвляет ввести город непосредственно из консоли

def get(city): #Функция получения температуры
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=db14c0395ff0e7d8666a3f6fe4217e07"
    data = requests.get(url).json()
    forecast_data = data["main"]
    a = u'\N{DEGREE SIGN}'+'C' #знак цельсия
    t = str(round(forecast_data["temp"] - 273.15,1)) #Текущая температура
    f = str(round(forecast_data["feels_like"] - 273.15,1)) #Как ощущается
    print("Город :", city.capitalize(), \
          "\nТемпература :",t+a,\
          "\nОщущается как :",f+a)

def valid():
    url_2 = ["https://ru.wikipedia.org", "http://openweathermap.org", "https://data.gov.ru/opendata/7710349494-urals",\
             "http://urfu.ru"]
    status = []
    for i in url_2:
        status.append(requests.head(i).status_code)
    union_d = list(zip(status, url_2))
    valid_urls = range(100, 400)
    unvalid_urls = range(400, 527)
    for u, i in union_d:
        if u in valid_urls:
            print(f"Сайт: {i} доступен!")
        elif u in unvalid_urls:
            print(f"В данный момент {i} сайт не работает.")
        else:
            print("Wrong")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', help='Enter the City')
    parser.add_argument('--valid', action='store_true', help='Try to valid web-sites')

    args = parser.parse_args()


    if args.valid:
        valid()
    elif args.city:
        get(args.city)
    else:
        print('Wrong command')