
class ContaBancaria():
   
    def __init__(self,titular,saldo=True,consultar_saldo=False,depositar=False,sacar=False):
        self.titular= titular
        
        self.saldo = saldo
        self.consultar_saldo= consultar_saldo
        self.depositar = depositar
        self.sacar = sacar
        
      
        if self.titular:
                print( f'seja bem vindo(a) {self.titular}.')
        if self.saldo >= 0:
             print(f'o seu saldo é de R$\033[34m{self.saldo}\033[m Reais')
        if self.saldo < 0:
             print(f'O seu Saldo é NEGATIVO de R$ \033[31m{self.saldo} Reais.\033[m')
       
      

        if self.depositar is True:
            consultar_saldo =True
            consultar_saldo= self.saldo + self.depositar
            total = consultar_saldo * 10 / 100
            try:
                dep = int(input('quanto deseja depositar?'))
            except:
                KeyboardInterrupt
                print('\033[31m\nERRO!!Usuário saiu Inesperadamente :(\033[m')
                return
                
            consultar_saldo = self.saldo + dep
            
            print(f'o seu saldo atual é de {consultar_saldo + total} ')
            if sacar is True:
                 consultar_saldo = saldo + depositar
                 sa = int(input(f'Quanto deseja Sacar? ({consultar_saldo}) :'))

                 retirar = sa- consultar_saldo 
                 print(f'Voce tem um saldo de {retirar} Reais')
            

class ContaCorrente(ContaBancaria):
    def __init__(self,titular,soma, saldo=0,consultar_saldo=True,depositar=False,sacar=False,cheque_especial=False):
            
            self.saldo = saldo
            self.depositar = depositar
            self.sacar= sacar
            self.consultar_saldo= consultar_saldo
            self.cheque_especial= cheque_especial
            # soma = self.saldo + depositar
            print('Lembrando que Você pode fazer um saque de até R$5.000')
            if cheque_especial is False:
                
                print('Encerrando O Sistema...')
                return
            if cheque_especial is  True:
                while True:
                    try:
                   
                        quant = float(input(f'Quanto deseja sacar ?(limite de 5.000 ): '))
                    except KeyboardInterrupt:
                        print('\033[31m\nHouve um ERRO, Usuario saiu inesperadamente :(\033[m')
                        return
                    except ValueError:
                         print( 'Digite apenas números...')
                         return
                    if quant > 5000 :
              
                        print('\033[31mVoce não pode sacar mais que o limite,tente novamente.\033[m')
                        # break
                    else:  
                   
                    
                        # break                           
                        print(f'Você já pode aproveitar os seus {quant} reais')
                        break


class NovaConta():
     def __init__(self,nome,cpf,senha,valor=False):
          self.nome = nome
          self.cpf = cpf
          self.senha =senha 
          self.valor = valor
          print(f'Seja Bem Vindo(a) {nome} cpf {cpf} e senha {senha}'.replace(',','.'))
          if valor ==True:
                valor= float(input('Quanto deseja depositar?'))
                print(f'Voce tem {valor} Disponivel')  