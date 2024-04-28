from os import remove #Nas primeiras linhas eu declaro algumas variaveis globais que possam me ajudar, algumas sendo listas outras contadores
from modulo_extrato import altera_extrato
from datetime import datetime #Aqui eu importa uma função de um modulo criado por mim e depois importo do modulo datetime a função datetime
produtos = []
cont = 0
Total = 0
cont2 = 0
def novo_pedido(): #Agora eu defino a função para criar um novo pedido 
  global Total
  global cont2
  global cont # Declaro algumas variaveis globais definidas anteriormente
  preços = open("tabela.txt","r") # A tabela de presos foi criada em um arquivo txt e sempre que é preciso eu apenas abro como leitura e leio as linhas
  for linha in preços:
    print(linha)
  preços.close() #Após printar a tabela para o usuário eu fecho o arquivo
  cont2 = 0 
  while cont2 != 1: # Faço um while para repetir enquanto a variavel cont2 for diferente de 1, assim sempre aparecera na tela do usuario um print com instruções e um input de codigo e quantidade
    print("Selecione o codigo do produto e a quantidade desejada")
    codigo = int(input("Digite o código do produto desejado: "))
    quantidade = int(input("Digite a quantidade desejada: "))
    if codigo == 1: # Agora conforme a escolha do usuario eu multiplico o preço inicial do produto com a quantidade desejada
      Total = 10.00 * quantidade
      produtos.append(Total) #Guardo o valor em uma lista para me auxiliar depois
      historico = open(str(Cpf),"a+",encoding="UTF-8") #Agora eu abro um arquivo em modo append +, assim caso ja tenha sido feito um pedido antes no arquivo, este produto ira ser escrito no final, pois como veremos posteriormente já teremos alguns dados escritos no arquivo.
      historico.write("%d-X salada-Preço unitário: 10.00  Valor: %2.2f -\n" % (quantidade,Total)) #Escrevo as informações do pedido
      historico.close() #Sempre fecho o arquivo no final de cada if para que não ocorra problemas durante a escrita 
    elif codigo == 2: # O mesmo processo se repetira, a unica diferença é que os valores e informações irão variar de acordo com o produto desejado 
      Total = 10.00 * quantidade
      produtos.append(Total)
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-X burger-Preço unitário: 10.00  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo == 3:
      Total = 7.50 * quantidade
      produtos.append(Total)
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-Cachorro quente-Preço unitário: 7.50  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo == 4:
      Total = 8.00 * quantidade
      produtos.append(Total)
      print("0 seu pedido total ficou: R$%.2f reais" % (sum(produtos)))
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-Misto Quente-Preço unitário: 8.00  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo == 5:
      Total = 5.00 * quantidade
      produtos.append(Total)
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-Salada de Frutas- Preço unitário: 5.00  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo == 6:
      Total = 4.50 * quantidade
      produtos.append(Total)
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-Refrigerante-Preço unitário: 4.50  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo == 7:
      Total = 6.25 * quantidade
      produtos.append(Total)
      historico = open(str(Cpf),"a+",encoding="UTF-8")
      historico.write("%d-Suco Natural-Preço unitário: 6.25  Valor: %2.2f -\n" % (quantidade,Total))
      historico.close()
    elif codigo <= 0 or codigo > 7:
      print("Codigo invalido!") #Como não temos opções maiores que 7 ou menores que 0, eu printo esta mensagem, repare que o while continuara, pois cont2 continua diferente de 1.
    pedido2 = input("Deseja adicionar outro produto?") #Pergunto para o cliente se ele deseja adicionar outro produto
    if pedido2 == "Sim" or pedido2 == "sim" or pedido2 == "SIM":#No caso de sim, eu leio a tabela de preços novamente e o while continua.
      preços = open("tabela.txt","r")
      for linha in preços:
        print(linha)
      preços.close()
    elif pedido2 == "nao" or pedido2 == "não" or pedido2 == "NAO" or pedido2 == "Não" or pedido2 == "NÃO":#No caso de não, atribuo o valor de 1 para cont2 e o laço é quebrado
      historico = open(str(Cpf),'r')#Abro o arquivo com o Cpf digitado em modo leitura
      ler = historico.readlines()#Coloco as linhas em listas
      historico.close()#Fecho o arquivo
      ler1 = ler[3].split(" ")#Defino ler1 como a linha de indice 3, que no caso contém o valor total do pedido 
      valor_extrato = float(ler1[0])#Após pegar o valor escrito no arquivo eu transformo em float e guardo em variavel
      valor_final = sum(produtos) + valor_extrato#Defino valor_final como a soma dos elementos da minha lista produtos + o valor_extrato que peguei no arquivo 
      valor_string = str(valor_final)#Transformo em string
      altera_extrato(str(Cpf),3,valor_string)#Coloco como parametro da minha função importada e ela reescreve no arquivo com a alteração
      produtos.clear()#Limpo a lista produtos para que não ocorra alterações quando inserir outros produtos
      cont2 = 1
def cancelar():#Defino a função cancelar  
  Senha2 = input("Digite sua senha: ") #Guardo a senha digitada pelo usuario em uma variavel e depois faço o mesmo com o Cpf
  Cpf = int(input("Digite o seu CPF: "))
  try: #Utilizo a função try para que o programa tente abrir um arquivo texto com a variavel Cpf
    historico = open(str(Cpf), 'r') #Caso isso ocorra eu guardo as linhas em listas e verifico a senha e Cpf digitados com os que estão escritos no arquivo 
    ler = historico.readlines()
    lerCpf = ler[2].strip().split(" ")
    lerSenha = ler[1].strip().split(" ")
    if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha2:
      print("Login Correto")# Caso sejam iguais e o len(ler) for menor do que 3, o que significa que no arquivo tem apenas as informações do usuario eu informo que não tem nenhum pedido cadastrado ainda, caso o len seja igual ou maior que 4 isso quer dizer que tem pedidos cadastrados no arquivo e então eu o deleto com a função remove importada anteriormente.
      historico.close()
      if len(ler) < 3:
        print("Você ainda não tem nenhum pedido cadastrado!")
      if len(ler) >= 4:
        remove(str(Cpf))
        print("Pedido cancelado!")
    else:
      print("Login incorreto")#Caso o cpf e a senha não sejam iguai eu não deleto a o programa e o menu de opções volta  
  except FileNotFoundError:#Caso a função try não consiga abrir o arquivo com a variavel cpf isso significa que não foi criado um pedido com o Cpf digitado
    print("Você Não possui nenhum pedido cadastrado")
def inserir():#Agora eu defino a função inserir 
  global Cpf
  global cont2
  Cpf = int(input("Digite seu CPF: ")) #Peço para o usuario digitar o Cpf e a senha 
  Senha3 = input("Digite sua Senha: ")
  try: #Uso o mesmo metodo de verificação com try e except
    historico = open(str(Cpf), 'r') #abro o arquivo em modo leitura e comparo o cpf e senha do arquivo com os que foram digitados
    ler = historico.readlines()
    lerCpf = ler[2].strip().split(" ")
    lerSenha = ler[1].strip().split(" ")
    if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha3:
      print("Login Correto")#Caso as informações estejam corretas eu chamo a função de novo_pedido para inserir mais produtos
      novo_pedido()
    else:
      print("login errado")#Caso estejam erradas o menu volta a aparecer
  
  except FileNotFoundError: #Caso não exista um arquivo com o cpf digitado o menu volta a aparecer
    print("Você ainda não criou um pedido")
    
  cont2 = 0
def cancela_produto():#Defino a função de cancela_produto
  Cpf = int(input("Digite seu CPF: "))
  Senha4 = input("Digite sua Senha: ")
  try:#Utilizo o mesmo metodo de verificação que foi usado nas outras funções
    historico = open(str(Cpf),'r')
    ler = historico.readlines()
    lerCpf = ler[2].strip().split(" ")
    lerSenha = ler[1].strip().split(" ")
    if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha4:
      print("Login Correto")
      preços = open(str(Cpf),"r",encoding="UTF-8")
      for linha in preços.readlines(): #Caso o login esteja correto eu printo o extrato do usuario em questão e peço para ele digitar o codigo do produto e a quantidade existente no pedido
        print(linha)
      preços.close()
      retirar = int(input("Digite o codigo do produto que deseja retirar: "))
      retirar1 = input("Digite a quantidade do produto que deseja retirar: ")
      if retirar == 1: #Agora utilizando IF eu defino a variavel "a" de acordo com o codigo
        a = "X salada"
      elif retirar == 2:
        a = "X burger"
      elif retirar == 3:
        a = "Cachorro quente"
      elif retirar == 4:
        a = "Misto Quente"
      elif retirar == 5:
        a = "Salada de Frutas"
      elif retirar == 6:
        a = "Refrigerante"
      elif retirar == 7:
        a = "Suco Natural"
      arquivo=open(str(Cpf),"r+")#Após isso abro o arquivo em modo leitura+
      linhas = arquivo.readlines() #guardo as linhas em lista
      for x in linhas:#Agora com o for eu separo as palavras pelo hífen
        lista=x.split("-") 
        if a in lista: #E a cada iteração eu verifico se a variavel que guarda o nome do produto está na lista
          listacomopcao=lista #Caso esteja eu guardo em outra variavel
          if retirar1 in listacomopcao:#Agora verifico se a quantidade certa
            produto_desejado=listacomopcao #Caso o produto e a quantidade estejam certas eu guardo em outra variavel
            separar = produto_desejado[2].split(" ")#Com esta variavel eu a separo de acordo com o espaço, após isso eu transformo em float e subtraio com o valor presente no arquivo e depois tranformo em string para adicionar 
            valor = float(separar[5])
            valor_extrato =float(linhas[3])
            altera_extrato(str(Cpf),3,valor_extrato-valor)
            if not "cancelado" in produto_desejado:
              arquivo.write("%s-%s-%s- cancelado\n"%(listacomopcao[0],listacomopcao[1],listacomopcao[2]))
              print("Produto cancelado!")
      arquivo.close()
    else:
      print("login incorreto")
  except FileNotFoundError:
    print("Você ainda não criou um pedido") 
def valorfinal():#Agora eu defino a função valorfinal
  global Cpf
  Senha5 = input("Digite sua senha: ")
  Cpf = int(input("Digite o seu CPF: "))
  try:#Faço o mesmo metodo de verificação que utilizo para as outras funções
    historico = open(str(Cpf), 'r')
    ler = historico.readlines()
    lerCpf = ler[2].strip().split(" ")
    lerSenha = ler[1].strip().split(" ")
    if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha5:
      print("Login Correto")
      historico.close()
      ler1 = ler[3].strip("\n")#Caso login esteja certo apenas leio a linha 3 do arquivo e printo 
      print("O seu pedido ficou: R$%s Reais" % ler1)
    else:
      print("Login incorreto")
  except FileNotFoundError:
    print("Você ainda não tem um pedido!")
    
  
def extrato():#Agora defino a função extrato 
  global Cpf
  Senha6 = input("Digite sua senha: ")
  Cpf = int(input("Digite o seu CPF: "))
  try:#Faço o mesmo metodo de verificação que utilizo para as outras funções
    historico = open(str(Cpf), 'r')
    ler = historico.readlines()
    lerCpf = ler[2].strip().split(" ")
    lerSenha = ler[1].strip().split(" ")
    if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha6:
      print("Login Correto")
      preços = open(str(Cpf),"r",encoding="UTF-8")
      ler = preços.readlines()#Caso o login esteja correto eu apenas leio o arquivo e printo com algumas informações que faltam no extrato que no caso são data e hora e algumas strings para complementar as informações
      preços.close()
      ler[3] = "Total: R$" + ler[3]
      ler.insert(4,datetime.today().strftime('%Y-%m-%d %H:%M \n'))
      ler.insert(5,"Itens do pedido: \n")
      for elemento in ler:
        print(elemento)
    else:
      print("login errado")
  except FileNotFoundError:
      print("Você ainda não tem um pedido!") 
print("            Seja bem vindo a BurguerFei") #Após definir as funções eu prino o cabeçalho de boas vindas
print("Para prosseguir precisamos que informe algumas informações: ")
print(" ")
while True: #Defino um while True para sempre fornecer o menu de opções
  menu = ["0 - Sair","1 - Novo Pedido","2 - Cancela Pedido","3 - Insere Produto","4 - Cancela Produto","5 - Valor do Pedido","6 - Extrato do pedido",] # guardo o menu em uma lista e depois leio com um for 
  for elemento in menu:
    print("%4s" % (elemento))
  opção = int(input("Para prosseguir selecione uma das opções:"))
  if opção >= 8 or opção < 0: #Agora defino o caminho logico das opções do menu, caso a opção seja maior ou igual a 8 eu printo "opção invalida" caso seja menor que 0 o mesmo irá ocorrer
    print("0pção Invalida")
  elif opção == 1: #Para a opção 1 eu verifico o login fora da função para não ocorrer conflito com a função inserir
    Nome = input("Digite o seu Nome: ")
    Senha1 = input("Digite a senha: ")
    Cpf = int(input("Digite o seu CPF: "))
    def verificador():
      global Senha
      try:#Faço o mesmo metodo de verificação que utilizo para as outras funções
        historico = open(str(Cpf), 'r')
        ler = historico.readlines()
        lerNome = ler[0].strip().split(" ")
        lerCpf = ler[2].strip().split(" ")
        lerSenha = ler[1].strip().split(" ")
        if lerCpf[1] == str(Cpf) and lerSenha[1] == Senha1 and Nome == lerNome[1]:
          print("Login Correto") 
          if len(ler) > 3:#Se o len do meu arquivo for maior que 3, isso significa que possui um pedido já registrado
            print("Apenas um pedido por CPF!") 
          else:
            novo_pedido()#Caso não seja eu chamo a função novo_pedido
        else:
          print("Login incorreto")
      except FileNotFoundError:
        historico = open(str(Cpf), 'w') #Caso não abra um arquivo com o cpf eu uso o except para criar um, e após isso eu chamo a função novo_pedido
        historico.write("Nome: %s\nSenha: %s\nCpf: %s\n0 \n" % (Nome, Senha1, Cpf))
        historico.close()     
        novo_pedido()
    verificador()
  elif opção == 2: #E agora vou chamando as funções de acordo com a opção do menu     
    cancelar()  
  elif opção == 3:
    inserir()
  elif opção == 4:
    cancela_produto()
  elif opção == 5:
    valorfinal()
  elif opção == 6:
    extrato()
  elif opção == 0:
    print("        Saindo...")
    break
          
          
     
    
    

        
    
