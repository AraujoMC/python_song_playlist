import os
class PlaylistCreatorView:
    def playlist_creator_success(self, controller_response) -> None:
        self.__clear()
        print("Playlist criada com sucesso!!\n\n")
        for musics in controller_response["playlist"]:
            message = f'''
                    Titulo da Musica: {musics.title}
                    Arista compositor: {musics.artist}
                    Ano de publicacao: {musics.year}
            '''
            print(message)
    def playlist_creator_fail(self, controller_response) -> None:
        self.__clear()
        message = f'''
                * Erro na criacao da Playlist: {controller_response["error"]}
        '''
        print(message)
    def __clear(self) -> None:
        os.system("cls||clear")
