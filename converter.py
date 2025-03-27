# Python version 3.13.2
# install pandas
# install ics
# import Calendar
# import csv

import pandas as pd
import csv
from ics import Calendar

# Passo 1: Ler o arquivo .ics
# 'with open' - Abre o arquivo .ics no modo leitura ("r") com suporte a caracteres especiais (utf-8)
# 'calendar' - Lê o conteúdo do arquivo e cria um objeto Calendar, que contém todos os eventos do calendário
with open("servicos_agenda.ics", "r", encoding="utf-8") as file:
    calendar = Calendar(file.read())

# Passo 2: Extrair eventos do arquivo .ics
# O campo "descritivo" contém quebras de linha (\n). 
# Ao exportar para CSV, essas quebras são interpretadas como separadores de registros.
# Dessa forma, são criadas linhas adicionais no arquivo final.
eventos : list = []
for event in calendar.events:
    eventos.append({
        "Nome": event.name,
        "Data": event.begin.strftime("%Y-%m-%d"),
        "Hora": event.begin.strftime("%H:%M"),
        "Local": event.location,
        "Descritivo": (event.description.replace("\n", " ") if event.description else "Sem Descrição"),
    })

# Passo 3: Criar um DataFrame do pandas e salvar como CSV
df = pd.DataFrame(eventos)
df.to_csv("servicos_agenda_orig.csv", index=False, encoding="utf-8")

print("Conversão concluída! O arquivo 'eventos.csv' foi gerado.")
