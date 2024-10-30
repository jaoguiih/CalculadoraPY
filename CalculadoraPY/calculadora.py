def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Pode dividir por Zero não, BURRO!"
    else:
        return "Operação Invalida fih, faz direito."

def main():
    print("Se liga nessa -> Calculadora <-")
    num1 = float(input("Digita o primeiro número: "))
    num2 = float(input("Digita o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /):").lower()

    resultado = calcular(num1, num2, operacao)
    print("Receba a inteligencia")
    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
