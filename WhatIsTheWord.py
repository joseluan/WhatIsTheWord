
import string
string.punctuation


texto = ""
with open("palavrasPT","r") as linhas:
    texto += linhas.read()
texto = texto.replace("-"," ")
texto = texto.lower()
texto = texto.split()
numero = 0
quanttexto = []
quantletra = input("Enter the number of words of his word :")
for palavra in texto:
    if len(palavra) == quantletra:
        if palavra not in quanttexto:
            quanttexto.append(palavra)
            numero += 1
            
print ""
print numero , "It was the amount of possible words for tamano"
print ""
print "Type exit to display the result"
print ""

filtros = []
cont = ""
resultado = []
contador = 0

while cont != "exit" or contador  != quantletra:
    indice = raw_input("Enter the indece: ")
    if indice.lower() == "exit":
        break
    letra = raw_input("type the letter: ")
    if letra.lower() == "exit":
        break

    indice = int(indice)
    filtros = quanttexto
    quanttexto = []
    #faz filtragem das palavras de acordo com o indice e as letras
    for palavra  in filtros:
        ipalavra =palavra[indice] 
        if ipalavra.lower()  == letra.lower():
            quanttexto.append(palavra)
            
    contador  += 1

print ""    
for palavra in quanttexto:
    print palavra.upper()

            
        

