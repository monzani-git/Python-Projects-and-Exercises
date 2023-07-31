print("------Cadastro------")
nome = input("Digite seu nome completo: ")
id = int(input("Idade: "))
rg = (input("Um documento RG ou CPF: "))
sal = float(input("Salario: "))
print("------Resultado------")

print(nome)
print(id)
print(rg)
print("R$ {:.2f}".format(sal))

print("------Fim------")