import pandas as pd
import re

# 1. Ler o arquivo CSV em um DataFrame
df = pd.read_csv('servicos_2023e2024_normalizado.csv')

# 2. Função para extrair as informações de cada campo do 'Descritivo'
def fragmentar_descritivo(descritivo):
    # Criar um dicionário para armazenar os dados extraídos
    fragmentos = {
        'link_maps': None,
        'referencia': None,
        'detalhes_obs': None,
        'morada': None,
        'contacto': None,
        'servico': None,
        'valor': None,
        'descritivo_valor': None,
        'medidas': None
    }
    
    # Padrão para capturar cada campo, mesmo que esteja vazio
    padroes = {
        'link_maps': r'Maps:\s*(https?://[^\s]+)',
        'referencia': r'Referência:\s*(.*?)\s*(?=Detalhes/Obs:|Morada:|Contacto:|Serviço:|Valor:|Descritivo:|Medidas:|$)',
        'detalhes_obs': r'Detalhes/Obs:\s*(.*?)\s*(?=Morada:|Contacto:|Serviço:|Valor:|Descritivo:|Medidas:|$)',
        'morada': r'Morada:\s*(.*?)\s*(?=Contacto:|Serviço:|Valor:|Descritivo:|Medidas:|$)',
        'contacto': r'Contacto:\s*(\d{9,})',
        'servico': r'Serviço:\s*(.*?)\s*(?=Valor:|Descritivo:|Medidas:|$)',
        'valor': r'Valor:\s*(\d+(\.\d{1,2})?)',
        'descritivo_valor': r'Descritivo:\s*(.*?)\s*(?=Medidas:|$)',
        'medidas': r'Medidas:\s*(.*?)\s*$'
    }

    # Iterar sobre os padrões e extrair os campos
    for campo, padrao in padroes.items():
        match = re.search(padrao, descritivo, re.DOTALL)
        fragmentos[campo] = match.group(1) if match else None

    return fragmentos
    
# 3. Aplicar a função de fragmentação no campo 'Descritivo' e criar novas colunas
fragmentos_df = df['Descritivo'].apply(fragmentar_descritivo).apply(pd.Series)

# 4. Concatenar as novas colunas com o DataFrame original
df_final = pd.concat([df, fragmentos_df], axis=1)

# 5. Salvar o DataFrame final em um novo arquivo CSV
df_final.to_csv('arquivo_fragmentado.csv', index=False)

print("Campo 'Descritivo' fragmentado e arquivo salvo com sucesso!")