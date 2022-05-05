from fiap_m3v4 import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Localizando")
localizarInventario(minhaLista)

print("Depreciando")
depreciacaoInventario(minhaLista, 20)

print("Excluindo")
excluirInventario(minhaLista)

print("Relatando")
relatorioValores(minhaLista)
