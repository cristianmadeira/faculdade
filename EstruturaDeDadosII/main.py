option = -1
while option != 0:
    
    title_option = 'Selecione qual exercício que você quer executar:'
    message_option = '\n0-Sair\n1-Pilhas\n2-Fila\n'
    option = int(input('{} \n {} :'.format(title_option,message_option)))
    
    if option == 0:
        print('Bye!')
        
    elif option == 1:
        from stack.views import view
        view()
        
    elif option == 2:
        from queue.views import view
        view()
        
    