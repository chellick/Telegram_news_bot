import requests
from bs4 import BeautifulSoup as BS
from botsql import *

def get_theme(array):
    themes = []
    for el in array:     
        themes.append((el.span.text, "https://habr.com" + el["href"]))

    return themes

def get_profile_themes(url):
    r = requests.get(url=url)
    soup = BS(r.content, "html.parser")
    arr = soup.find_all("a", class_= "tm-user-hubs__hub")
    result = get_theme(arr)

    return result

def get_message(array: list) -> str:
    result = ''
    for i in array:
        result += f"[{i[0]}]({i[1]})" + "\n" + '________________' + "\n"

    return result

def get_news(url):
    r = requests.get(url=url)
    soup = BS(r.content, "html.parser")
    arr = soup.find_all("a", class_ ="tm-title__link")
    result = get_theme(arr)[0]

    return result



# arr = get_profile_themes('https://habr.com/ru/users/chellick/')

# for i in range(len(arr)):
#     print(arr[i][1])

# array = get_news("https://habr.com/ru/hub/data_engineering/")
# print(array)
