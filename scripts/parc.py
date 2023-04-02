import requests
from bs4 import BeautifulSoup as BS


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

def get_message(array):
    result = ''
    for i in array:
        result += f"[{i[0]}]({i[1]})" + "\n"

    return result

array = get_profile_themes("https://habr.com/ru/users/chellick/")

# print(get_message(array))

