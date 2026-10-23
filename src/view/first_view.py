def introduction_page():
    message = '''
    Sistema Musical

    = Cadastrar Musica - 1
    = Criar Playlist - 2
    = Sair - 5
    '''
    print(message)
    command = input("Digite o comando: ")
    return command