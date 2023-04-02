import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://habr.com/ru/hubs/")
html = BS(r.content, "html.parser")
arr = html.find_all("a", class_="tm-hub__title")


def get_theme(array):
    arr = []
    for el in array:
        arr.append(el.span.text)

    return arr


    
# for el in html.select("#app > div.tm-layout__wrapper > div.tm-layout > main > div > div > div > div.tm-page__main.tm-page__main_has-sidebar > div > div:nth-child(3) > div.tm-hubs-list"):
#     for i in range(1, 10):

#         title = el.select(f"#app > div.tm-layout__wrapper > div.tm-layout > main > div > div > div > div.tm-page__main.tm-page__main_has-sidebar > div > div:nth-child(3) > div.tm-hubs-list > div:nth-child({i}) > div > div.tm-hub > div > div:nth-child(1) > a > span")
#         print(title)
