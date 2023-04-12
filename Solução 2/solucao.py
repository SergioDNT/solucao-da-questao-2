import json

with open(r'C:\Users\Sergio\Projeto\Solu--o-quest-o-2\Solucao 2\dados.json') as f:
    dados = json.load(f)

# menor valor de faturamento
valores_faturamento = [dado['valor'] for dado in dados if dado['valor'] > 0.0]
menor = min(valores_faturamento)
print(f"menor valor de faturamento: {menor}")

# maior valor de faturamento
maior = max(valores_faturamento)
print(f"maior valor de faturamento: {maior}")

# média mensal
media = sum(valores_faturamento) / len(valores_faturamento)
print(f"média mensal: {media}")

# dias com faturamento superior à média
dias_acima_da_media = len([valor for valor in valores_faturamento if valor > media])

# Imprime o resultado
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
