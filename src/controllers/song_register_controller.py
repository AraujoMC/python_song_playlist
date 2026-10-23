class SongRegisterController:
    
    def insert(self, new_song_info: dict) -> dict:
        #principio da responsabilidade unica, cada metodo tem uma responsabilidade unica
        try:
            self.__verify_song_info(new_song_info)
            self.__verify_if_song_already_registered(new_song_info)
            self.__insert_song(new_song_info)
            return self.__format_response(new_song_info)
        except Exception as e:
            return self.__format_error_response(e)

    def __verify_song_info(self, new_song_info: dict) -> None:
        if len(new_song_info["title"]) > 100:
            raise Exception("O nome da musica deve ter no maximo 100 caracteres")
        year = int(new_song_info["year"])
        if year >= 2027:
            raise Exception("O ano de publicacao invalido")
    
    def __verify_if_song_already_registered(self, new_song_info: dict) -> None:
       # Interacao com Models
        pass

    def __insert_song(self, new_song_info: dict) -> None:
       # Interacao com Models
        pass

    def __format_response(self, new_song_info: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_info["title"],
                "artist": new_song_info["artist"]
            }
        }

    def __format_error_response(self, error_message: Exception) -> dict:
        return {
            "success": False,
            "error": str(error_message)
        }