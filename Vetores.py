n = int(input("Quantos números você vai digitar: "))

vet = [0.0] * n

for i in range(n):
    vet[i] = float(input("Digite um número: "))

print("\nNúmeros Digitados:")
for i in range(n):
    print(f"{vet[i]:.1f}")
