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
    
    def registry_song_success(self, controller_response: dict) -> None:
        self.__clear()
        message = f'''
        Musica cadastrada com sucesso!
        * Titulo: {controller_response["attributes"]["title"]}
        * Artista: {controller_response["attributes"]["artist"]}
        *Quantidade de musicas cadastradas: {controller_response["count"]}
        '''
        print(message)

    def registry_song_error(self, controller_response: dict) -> None:
        self.__clear()
        message = f'''
        Erro ao cadastrar musica!
        * Erro: {controller_response["error"]}
        '''
        print(message)

    
    def __clear(self) -> None:
        os.system("cls||clear")
