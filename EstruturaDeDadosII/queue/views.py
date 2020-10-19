from .queue import Queue
def view():
    queue = Queue()
    message_option='\n0-Sair\n1-Inserir\n2-Remover\n3-Listar\n:'
    option = int(input(message_option))
    if option  == 0 :
        print('Bye!')
    elif option == 1:
        element = input('Informe o elemento que quer inserir:')
        stack.insert(element)
        print('Item inserido com sucesso!')