import pandas as pd
import re

# 1. Ler o arquivo CSV em um DataFrame
df = pd.read_csv('servicos_2023e2024_limpo.csv')

# 2. Função para normalizar os campos do 'descritivo'
def normalizar_descritivo(descritivo):
    # Substituir variações dos campos para garantir que sigam o formato desejado

    # Substitui "Maps:-" ou "Maps:" para "Maps: "
    descritivo = re.sub(r'Maps:-', ' Maps: ', descritivo)  # "Maps:-" para "Maps: "
    descritivo = re.sub(r'Maps:', ' Maps: ', descritivo)   # "Maps:" para "Maps: "

    # Substitui "Referência:-" ou "Referência:" para "Referência: "
    descritivo = re.sub(r'Referência:-', ' Referência: ', descritivo)  # "Referência:-" para "Referência: "
    descritivo = re.sub(r'Referência:', ' Referência: ', descritivo)   # "Referência:" para "Referência: "

    # Substitui "Detalhes/Obs:-" ou "Detalhes/Obs:" para "Detalhes/Obs: "
    descritivo = re.sub(r'Detalhes/Obs:-', ' Detalhes/Obs: ', descritivo)  # "Detalhes/Obs:-" para "Detalhes/Obs: "
    descritivo = re.sub(r'Detalhes/Obs:', ' Detalhes/Obs: ', descritivo)   # "Detalhes/Obs:" para "Detalhes/Obs: "

    # Substitui "Morada:-" ou "Morada:" para "Morada: "
    descritivo = re.sub(r'Morada:-', ' Morada: ', descritivo)  # "Morada:-" para "Morada: "
    descritivo = re.sub(r'Morada:', ' Morada: ', descritivo)   # "Morada:" para "Morada: "

    # Substitui "Contacto:-" ou "Contacto:" para "Contacto: "
    descritivo = re.sub(r'Contacto:-', ' Contacto: ', descritivo)  # "Contacto:-" para "Contacto: "
    descritivo = re.sub(r'Contacto:', ' Contacto: ', descritivo)   # "Contacto:" para "Contacto: "

    # Substitui "Serviço:-" ou "Serviço:" para "Serviço: "
    descritivo = re.sub(r'Serviço:-', ' Serviço: ', descritivo)  # "Serviço:-" para "Serviço: "
    descritivo = re.sub(r'Serviço:', ' Serviço: ', descritivo)   # "Serviço:" para "Serviço: "

    # Substitui "Valor:-" ou "Valor:" para "Valor: "
    descritivo = re.sub(r'Valor:-', ' Valor: ', descritivo)  # "Valor:-" para "Valor: "
    descritivo = re.sub(r'Valor:', ' Valor: ', descritivo)   # "Valor:" para "Valor: "

    # Substitui "Descritivo:-" ou "Descritivo:" para "Descritivo: "
    descritivo = re.sub(r'Descritivo:-', ' Descritivo: ', descritivo)  # "Descritivo:-" para "Descritivo: "
    descritivo = re.sub(r'Descritivo:', ' Descritivo: ', descritivo)   # "Descritivo:" para "Descritivo: "

    # Substitui "Medidas:-" ou "Medidas:" para "Medidas: "
    descritivo = re.sub(r'Medidas:-', ' Medidas: ', descritivo)  # "Medidas:-" para "Medidas: "
    descritivo = re.sub(r'Medidas:', ' Medidas: ', descritivo)   # "Medidas:" para "Medidas: "

    # Retornar o descritivo normalizado
    return descritivo

# 3. Aplicar a função de normalização no campo 'Descritivo'
df['Descritivo'] = df['Descritivo'].apply(normalizar_descritivo)

# 4. Salvar o DataFrame normalizado em um novo arquivo CSV
df.to_csv('servicos_2023e2024_normalizado.csv', index=False)

print("Arquivo normalizado com sucesso!")