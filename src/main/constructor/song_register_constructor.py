from src.view.song_register_view import SongRegisterView

# SongRegisterView -> Pascal Case (Usado em padrão para nome de classes)
# song_register_view -> Snake Case (Usado em padrão para nome de variáveis e funções)

def song_register_process() -> None:
    song_register_view = SongRegisterView()

    new_song_info = song_register_view.registry_song_initial()