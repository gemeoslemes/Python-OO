
class Conta:

    # Este metodo é o construtor da nossa classe passando os atributos numero,titular, saldo, limite.
    # Para o encapsulamento do codigo colocamos "__" deixando assim os atributos privado
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
###########################################################################
    # Este metodo mostra o extrato de objeto criado da classe conta mostrando o saldo e o nome do titular
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))
###########################################################################
    # Este metodo pega a referencia do objeto e soma um valor passado entre ()
    def deposita(self, valor):
        self.__saldo += valor
###########################################################################
    # Esta metodo esta privada e esta recendo uma variavel somando o saldo com o limite
    # e retorna o valor_a_sacar se o valor_diponivel for <= ao valor que deseja sacar
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
###########################################################################
    # Este metodo pega o saldo do objeto criado, passando a referencia e retira o valor atraves dos ()
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite!".format(valor))
###########################################################################
    #Este metodo transfere recebe tres paramentros, o primeiro no caso self é a referencia do objeto
    # o segundo é o valor que atraves dos () chamado pelos metodos saca e deposita atribuido o valor que sera
    # enviado a outro objeto pela variavel destino
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
###########################################################################
    # Este metodo get_saldo retorna o saldo do objeto
    # O property substitui a funcionalidade do get_saldo trazendo o mesmo valor que a versao anterior do metodo
    @property
    def saldo(self):
        return self.__saldo
###########################################################################
    # Este medoto get_titular retorna o nome do titular do objeto
    # O property substitui a funcionalidade do get_titular trazendo o mesmo valor que a versao anterior do metodo
    @property
    def titular(self):
        return self.__titular
###########################################################################
    #Este metodo get_limite retorna o limite do objeto.
    #O property faz a mesma funcionalidade do get_limite substituindo o nome para
    #limite
    @property
    def limite(self):
        return self.__limite
    ###########################################################################
    # Este metodo set__limite nao retorna nada, mas ele atribui um novo valor para a variavel limite
    # passando no atributo self.limite
    #A anotacao @limite.setter faz a mesma funcionalidade do set__limite mudando o nome do metodo para
    # apenas limite no nome do metodo.
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    ###########################################################################
    # A anotacao staticmethod faz com que o metodo fique satico com essa fucao
    # voce pode chamar o medoto sem precisar instanciar um objeto
    @staticmethod
    def codigo_banco():
        return "001"
###########################################################################
    # A anotacao staticmethod faz com que o metodo fique satico com essa fucao
    # voce pode chamar o medoto sem precisar instanciar um objeto
    @staticmethod
    def codigos_bancos():
        return{'BB':'001', 'Caixa':'104', 'Bradesco':'237'}