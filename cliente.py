#Criando a classe Cliente
class Cliente:
    #Criando Construtor com um atriburo 'nome'
    def __init__(self, nome):
        self.__nome = nome

    #Esse metodo recebe essa anotacao substituindo o get retornando a funcionalidade nome
    #com o metodo title() onde a duncionalidade é na hora de retornar o nome do cliente a primeira letra
    # fica maiuscula
    @property
    def nome(self):
        return self.__nome.title()
    #Este metodo substitui um nome quando chamado o metodo alem de substituir a funcao SET
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
