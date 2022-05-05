
departamento=[]
modelo=[]
usuario=[]
patrimonio=[] 
valor=[]
resposta="S"

#Inserir Item
while resposta == "S":
    departamento.append(input("Insira o Departamento: "))
    modelo.append(input("Insira o Modelo: "))
    usuario.append(input("Insira o Usuario: "))
    patrimonio.append(int(input("Insira o Patrimonio: ")))
    valor.append(float(input("Insira o Valor: ")))
    
    resposta = input("Gostaria de adicioanar mais equipamentos?").upper()

#Depreciacao
for i in range(0, len(departamento)):
    depreciacao =input("Qual item deve ser depreciado? ")
    if depreciacao == modelo[i]:
        print("Valor antigo: ", valor[i])  
        valor[i] = valor[i] * 0.9
        print("Novo Valor: ", valor[i])  

#remover item
removePatrimonio = int(input("Qual patrimonio deseja remover? "))
for i in range(0, len(departamento)):
    if removePatrimonio == patrimonio[i]:
        del patrimonio[i] 
        del modelo[i] 
        del usuario[i]
        del departamento[i]
        del valor[i]
        break

    
   

