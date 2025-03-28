import pandas as pd
import re

# 1. Ler o arquivo CSV em um DataFrame
df = pd.read_csv('servicos_agenda_orig.csv')

# 2. Função para limpar códigos HTML do campo 'descritivo'
def limpar_html(texto):
    if pd.isna(texto):
        return texto  # Retorna vazio se o valor for NaN
    # Expressão regular para remover qualquer tag HTML
    return re.sub(r'<[^>]+>', '', texto)

# 3. Aplicar a função de limpeza na coluna 'descritivo'
df['Descritivo'] = df['Descritivo'].apply(limpar_html)

# 4. Salvar o arquivo limpo no mesmo CSV ou em um novo arquivo
df.to_csv('servicos_agenda_limpo.csv', index=False)

print("Campo 'descritivo' limpo e arquivo salvo com sucesso!")