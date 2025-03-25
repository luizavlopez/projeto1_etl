# 1. IMPORTAÇÃO DE BIBLIOTECAS NECESSÁRIAS
import pandas as pd
import re
from datetime import datetime

# 2. EXTRAÇÃO DOS DADOS (A PARTIR DO ARQUIVO .ICS)
# Aqui, o arquivo .ics é lido e seus dados são extraídos. Podemos usar uma biblioteca como 'ics' ou 'icalendar' para isso.
# Para este exemplo, o arquivo .ics já foi convertido em uma lista de eventos e transformado em um dataframe do pandas.

# Exemplo de dados extraídos (simulação do formato .ics convertido para um dataframe):
data = [
    {'nome_cliente': 'João Silva', 'data_hora_servico': '2025-03-25 10:00', 'local_servico': 'Rua das Flores, 123', 
     'descritivo': '<a href="https://goo.gl/maps/xyz">Google Maps</a> Perto do mercado. Telefone: 987654321. Serviço: Limpeza. Valor: 100.00. Observações: Chegar com 10 minutos de antecedência.'},
    {'nome_cliente': 'Maria Oliveira', 'data_hora_servico': '2025-03-26 14:30', 'local_servico': 'Av. Paulista, 456', 
     'descritivo': '<a href="https://goo.gl/maps/abc">Google Maps</a> Próximo ao shopping. Telefone: 123456789. Serviço: Consultoria. Valor: 200.00. Observações: Trazer documentos.'},
]
df = pd.DataFrame(data)

# 3. TRANSFORMAÇÃO DOS DADOS
# A função abaixo vai transformar o campo 'descritivo', segmentando as informações conforme o solicitado.

def tratar_descritivo(descritivo):
    # Eliminar as tags HTML
    descritivo_limpo = re.sub(r'<[^>]+>', '', descritivo)
    
    # Usar expressões regulares para segmentar o descritivo
    # Extração do link do Google Maps
    link_maps = re.search(r'(https?://[^\s]+)', descritivo_limpo)
    link_maps = link_maps.group(0) if link_maps else None
    
    # Extração do ponto de referência (geralmente vem antes de 'Telefone')
    ponto_referencia = re.search(r'Perto do (.*?)(?=\. Telefone)', descritivo_limpo)
    ponto_referencia = ponto_referencia.group(1) if ponto_referencia else None
    
    # Extração do número de telefone
    telefone = re.search(r'Telefone: (\d+)', descritivo_limpo)
    telefone = telefone.group(1) if telefone else None
    
    # Extração do serviço (palavra entre 'Serviço:' e o próximo ponto)
    servico = re.search(r'Serviço: ([\w\s]+)', descritivo_limpo)
    servico = servico.group(1) if servico else None
    
    # Extração do valor (valor após 'Valor:')
    valor = re.search(r'Valor: (\d+\.?\d*)', descritivo_limpo)
    valor = valor.group(1) if valor else None
    
    # Extração de observações
    observacoes = re.search(r'Observações: (.*)', descritivo_limpo)
    observacoes = observacoes.group(1) if observacoes else None
    
    # Segmentação do descritivo de valor (opcional, se houver descrição adicional)
    descritivo_valor = f"Valor: {valor}" if valor else None
    
    # Segmentação das medidas (caso existam no descritivo)
    medidas = re.search(r'Medidas: ([\w\s]+)', descritivo_limpo)
    medidas = medidas.group(1) if medidas else None

    # Retorno de um dicionário com todos os subcampos
    return {
        'link_google_maps': link_maps,
        'ponto_referencia': ponto_referencia,
        'telefone': telefone,
        'servico': servico,
        'valor': valor,
        'descritivo_valor': descritivo_valor,
        'observacoes': observacoes,
        'medidas': medidas
    }

# Aplicar a função de tratamento do descritivo para todos os registros no DataFrame
df_segmentado = df['descritivo'].apply(tratar_descritivo).apply(pd.Series)

# Concatenar os dados transformados com o DataFrame original (sem o descritivo original)
df_final = pd.concat([df.drop(columns=['descritivo']), df_segmentado], axis=1)

# 4. EXPORTAÇÃO DOS DADOS (AUTOMATIZADA E MANUAL)
# Para exportação automatizada, podemos salvar em um arquivo CSV ou para um banco de dados, dependendo da necessidade.

# Exportação para um arquivo CSV (automatizado)
df_final.to_csv('dados_exportados.csv', index=False)

# Caso o usuário prefira a exportação manual, ele pode acessar o arquivo do DataFrame e manipulá-lo diretamente.
# Ou usar a função 'to_clipboard()' para copiar os dados para a área de transferência e colar em uma planilha, por exemplo.
df_final.to_clipboard()  # Isso copiará os dados do DataFrame para a área de transferência

# 5. FIM DO PIPELINE
print("ETL concluído com sucesso!")