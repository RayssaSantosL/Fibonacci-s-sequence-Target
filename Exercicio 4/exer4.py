def calcular_percentual_faturamento(faturamento_por_estado):
    total_faturamento = sum(faturamento_por_estado.values())
    percentuais = {}

    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / total_faturamento) * 100
        percentuais[estado] = percentual

    return percentuais

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais = calcular_percentual_faturamento(faturamento_por_estado)

print("Percentual de representação do faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
