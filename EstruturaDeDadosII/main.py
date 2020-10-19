choice = 's'

while choice == 's':
    
    title_option = 'Selecione qual exercício que você quer executar:'
    message_option = '\n1-Pilhas\n2-Fila\n0-Sair\n'
    option = int(input('{} \n {} :'.format(title_option,message_option)))
    
    if option == 0:
        print('Bye!')
        
    elif option == 1:
        from stack.views import view
        view()

    choice = input('Deseja continuar (s/n) ?')