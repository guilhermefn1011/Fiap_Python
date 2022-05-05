equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite \"S\" para continuar: ").upper()


# # ----MOSTRAR LISTA INSERIDA-----
for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])


#-------BUSCAR ITEM ESPECÍFICO------
busca = input("Digite o nome do equipamento de busca: ")
for i in range (0,len(equipamentos)):
    if busca==equipamentos[i]:
        print("Valor:", valores[i])
        print("Serial:",seriais[i])


