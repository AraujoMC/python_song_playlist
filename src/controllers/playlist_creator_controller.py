import random
from src.Models.repositories.music_repository import music_repository

class PlaylistCreatorController:
     def create_playlist(self) -> dict:
          try:
               musics = self.__get_all_musics_and_verify()
               playlist = self.__create_playlist(musics)
               return self.__format_response(playlist)
          except Exception as e:
               return self.__format_error_response(e)

     def __get_all_musics_and_verify(self) -> list:
          musics = music_repository.get_all_songs()
          if not musics:
               raise Exception("Nenhuma musica registada!")
          return musics

     def __create_playlist(self, musics: list) -> list:
          random.shuffle(musics)
          return musics

     def __format_response(self, playlist: list) -> dict:
          return {
               "success": True,
               "playlist": playlist
          }

     def __format_error_response(self, error_message: Exception) -> dict:
          return {
               "success": False,
               "error": str(error_message)
          }