from src.Models.entities.music import Music

class __MusicRepository:
    def __init__(self):
        self.__music_list = []

    def insert_music(self, music: Music) -> None:
        self.__music_list.append(music)

    def find_music(self, music_tittle: str) -> Music:
        for music in self.__music_list:
            if music.title == music_tittle:
                return music

    def get_all_songs(self) -> list:
        return self.__music_list

#Design Pattern chamado Singleton
music_repository = __MusicRepository()