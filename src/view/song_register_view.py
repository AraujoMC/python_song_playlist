import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        print("Implementar nova musica \n\n")
        self.__clear()
        title = input("Digite o nome da musica: ")
        artist = input("Digite o nome do artista: ")
        year = input("Digite o ano de publicacao: ")

        new_song_info = {
            "title": title,
            "artist": artist,
            "year": year
        }
        return new_song_info

    def __clear(self) -> None:
        os.system("cls||clear")