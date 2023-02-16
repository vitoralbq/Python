class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
#title coloca a primeira letra em maiúsculo.
        print('chamando @property nome()')
        return self.__nome.title()
    @nome.setter
    def nome(self,nome):
        print('chamando setter nome()')
        self.__nome = nome
    