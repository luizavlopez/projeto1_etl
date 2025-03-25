# Python version 3.13.2
# install pandas
# install ics

import pandas as pd
from ics import Calendar

# Passo 1: Ler o arquivo .ics
# 'with open' - Abre o arquivo .ics no modo leitura ("r") com suporte a caracteres especiais (utf-8)
# 'calendar' - Lê o conteúdo do arquivo e cria um objeto Calendar, que contém todos os eventos do calendário
with open("servicos_agenda.ics", "r", encoding="utf-8") as file:
    calendar = Calendar(file.read())

# Passo 2: Extrair eventos do arquivo .ics
eventos = []
for event in calendar.events:
    eventos.append({
        "Data": event.begin.strftime("%Y-%m-%d %H:%M"),
        "Nome": event.name,
        "Local": event.location,
        "Descritivo": event.description,
    })

# Passo 3: Criar um DataFrame do pandas e salvar como CSV
df = pd.DataFrame(eventos)
df.to_csv("eventos.csv", index=False, encoding="utf-8")

print("Conversão concluída! O arquivo 'eventos.csv' foi gerado.")
