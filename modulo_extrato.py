def altera_extrato(arquivo,numero_linha,alteração): #crio essa função para auxiliar na escrito do extrato final do cliente
  file = open(arquivo,"r")#abro o arquivo de acordo com o nome recebido
  armazenar = []
  for linha in file.readlines(): #atravesso o arquivo 
    var=linha.split("\n")#armazeno a linha em uma variavel e retiro a quebra de linha
    armazenar.append(var[0])#guardo a variavel dentro da minha lista armazenar
  file.close()#fecho o arquivo para não ocorrer problemas 
  armazenar[numero_linha]=alteração#altero a linha desejada com o parametro alteração, que no caso será a string "-cancelado"
  file=open(arquivo,"w")#e por fim abro o arquivo e reescrevo com a alteração no final do arquivo
  for x in range(len(armazenar)):
    file.write("%s\n"%(armazenar[x]))
  file.close()
  