from bs4 import BeautifulSoup
import requests
import os
from multiprocessing import Process


def search_manga(manga_name):
    url = f"https://muitomanga.com/buscar?q={manga_name}"

    headers = {
        'Cookie': 'PHPSESSID=pt9g3ip57qeearso69ocvvh2lv'
    }

    response = requests.get(url, headers=headers, data={})

    soup = BeautifulSoup(response.text, 'html.parser')
    mangas = []
    i = 0
    for manga in soup.find_all("div", {"class": "anime"}):
        i = i + 1
        mangas.append([
            i,
            manga.find("a").get("href").split("/")[-1]
        ])
    return mangas


def get_chapter(manga_name, chapter_number):
    # Try to get 30 pages (max)
    for page in range(1, 30):
        p = Process(target=download_page, args=(
            manga_name, chapter_number, page))
        p.start()


def download_page(manga_name, chapter_number, page):
    url = f"https://imgs.muitomanga.com/imgs/{manga_name}/{chapter_number}/{page}.jpg"
    response = requests.get(url)

    # Create folder if not exists
    folder = f"mangas/{manga_name}/{chapter_number}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    if response.status_code == 200:
        print(f"Downloading {manga_name} {chapter_number} page {page}")
        with open(f"{folder}/{page}.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Page {page} not found")
        return


def get_manga_from_muitomanga():
    name = input("Digite o nome do manga: ")
    mangas = search_manga(name.replace(" ", "+"))

    print("=================== Mangas Encontrados ======================")
    if(len(mangas) == 0):
        print("Nenhum manga encontrado")
        print("=============================================================")
        exit()
    for manga in mangas:
        print(f"{manga[0]} - {manga[1]}")
    print("=============================================================")

    id_manga = input("Digite o id do manga: ")

    manga_name = mangas[int(id_manga) - 1][1]
    chapter_number = input("Digite o capitulo: ")

    print(f"Downloading {manga_name} chapter {chapter_number}")
    get_chapter(manga_name, chapter_number)


if __name__ == '__main__':
    get_manga_from_muitomanga()
