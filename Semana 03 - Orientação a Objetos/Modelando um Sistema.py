from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome=nome
        self._telefone=telefone
        self.__renda_mensal=renda_mensal

    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome (self,novo_nome):
        if type(novo_nome)!=str:
            raise TypeError("Tipo da variável deve ser str")
        self._nome=novo_nome

    @property
    def telefone(self):
        return self.telefone
    
    @telefone.setter
    def telefone(self,novo_tel):
        if type(novo_tel)!=str:
            raise TypeError("Tipo da variável deve ser str")
        self._telefone=novo_tel

    @property
    def renda_mensal(self):
        return self.__renda_mensal
    
    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self,nome,telefone,renda_mensal):
        super().__init__(nome,telefone,renda_mensal)

    def tem_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def __init__(self,nome,telefone,renda_mensal):
        super().__init__(nome,telefone,renda_mensal)

    def tem_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self,titular):
        self.__saldo=0.0
        self.__operacoes=[]
        self.__titulares=[]
        self.adicionar_titular(titular)

    def adicionar_titular(self,titular):
        self.__titulares.append(titular)

    def depositar(self,valor:float):
        self.__saldo+=valor
        self.__operacoes.append(f"Depósito de R$ {valor:.2f}")

    def sacar(self,valor:float):
        titular = self.__titulares[0]
        if titular.tem_cheque_especial()==False:
            if valor <= self.__saldo:
                self.__saldo-=valor
                self.__operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo insuficiente")
        else:
            if valor <= self.__saldo or (self.__saldo) <= titular.renda_mensal:
                self.__saldo -= valor
                self.__operacoes.append (f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
            
    @property
    def saldo(self):
        return self.__saldo        

cliente_mulher = ClienteMulher("Vitória Macedo","776677",30000)
cliente_homem = ClienteHomem("Paulo","33333",1000)

conta1=ContaCorrente(cliente_mulher)
conta2=ContaCorrente(cliente_homem)

try:
    conta1.depositar(5000.0)
    conta2.sacar(500.0)
except ValueError as e:
    print(f'Erro durante a execução: {e}')


print(conta1.saldo)
print(conta2.saldo)