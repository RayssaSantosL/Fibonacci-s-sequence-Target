import json

def carregar_faturamento(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return [dado["valor"] for dado in dados]

def menor_valor(faturamento_diario):
    return min(faturamento_diario)

def maior_valor(faturamento_diario):
    return max(faturamento_diario)

def media_mensal(faturamento_diario):
    dias_faturados = [faturamento for faturamento in faturamento_diario if faturamento > 0]
    return sum(dias_faturados) / len(dias_faturados)

def dias_acima_da_media(faturamento_diario):
    media = media_mensal(faturamento_diario)
    return sum(1 for faturamento in faturamento_diario if faturamento > media)

# Especificando o nome do arquivo
nome_arquivo = 'dados.json'

faturamento_diario = carregar_faturamento(nome_arquivo)

menor = menor_valor(faturamento_diario)
maior = maior_valor(faturamento_diario)
dias_acima_media = dias_acima_da_media(faturamento_diario)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Numero de dias com faturamento acima da media: {dias_acima_media}")

