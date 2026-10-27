def minimo_moedas(moedas, valor):
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0

    for i in range(1, valor + 1):
        for moeda in moedas:
            if moeda <= i:
                dp[i] = min(dp[i], dp[i - moeda] + 1)

    return dp[valor]


moedas = list(map(int, input("Digite os valores das moedas separados por espaço: ").split()))
valor = int(input("Digite o valor do troco: "))

resultado = minimo_moedas(moedas, valor)

print("Número mínimo de moedas:", resultado)
