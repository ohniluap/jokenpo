soma = 0
a = input('Digiteu um número de dois dígitos: ')
b = str(a) #Transformo em str para poder usar posição. Ex: "b[1] = 2"
for i in range(len(b)):
        soma += int(b[i])
print(soma)
