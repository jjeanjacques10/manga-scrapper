

from mangalivre import get_manga_from_mangalivre
from muitomanga import get_manga_from_muitomanga


if __name__ == "__main__":
    print("=================== Bem vindo ao Manga Scrapper ======================")
    print("1 - Mangalivre")
    print("2 - Muitomanga")
    option = input("Digite a opção: ")

    if option == "1":
        get_manga_from_mangalivre()
    elif option == "2":
        get_manga_from_muitomanga()
    else:
        print("Opção inválida")
