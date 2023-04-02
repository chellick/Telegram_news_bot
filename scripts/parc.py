import requests
from bs4 import BeautifulSoup as BS


def get_theme(array):
    themes = []
    for el in array:     
        themes.append((el.span.text, "https://habr.com" + el["href"]))

    return themes


for i in range(1, 12):
    r = requests.get(f"https://habr.com/ru/hubs/page{i}")
    html = BS(r.content, "html.parser")
    arr = html.find_all("a", class_="tm-hub__title")
    print(get_theme(arr))

