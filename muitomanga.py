import requests
import os
from multiprocessing import Pool
from multiprocessing import Process

def get_chapter(manga_name, chapter_number):    
    for page in range(1, 30):
        p = Process(target=download_page, args=(manga_name, chapter_number, page))
        p.start()

def download_page(manga_name, chapter_number, page):
    url = f"https://imgs.muitomanga.com/imgs/{manga_name}/{chapter_number}/{page}.jpg"
    response = requests.get(url)
    
    ## Create folder if not exists
    folder = f"{manga_name}/{chapter_number}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if response.status_code == 200:
        print(f"Downloading {manga_name} {chapter_number} page {page}")
        with open(f"{folder}/{page}.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Page {page} not found")
        return

if __name__ == '__main__':
    manga_name = "naruto"
    chapter_number = 301
    print(f"Downloading {manga_name} chapter {chapter_number}")
    get_chapter(manga_name, chapter_number)
   
