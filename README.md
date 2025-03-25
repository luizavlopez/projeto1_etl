# Conversor de arquivo .ics para arquivo .csv

## Objetivo principal do projeto
Organizar os clientes e os serviços de uma empresa de limpeza de estofos

## Objetivos específicos
1) Converter o ficheiro .ics exportado pelo Google Agenda para um ficheiro .csv
2) Limpar os dados exportados (remover códigos de html)
3) Segmentar o campo de 'descritivo' dos eventos exportados
4) Criar uma planilha com os clientes, contendo as principais informações como: nome, contacto, localidade e número de serviços realizados

## Requisitos do projeto
- Python version 3.13.2
- Instalar o pacote Pandas
- Instalar o pacote ics

### Detalhes do projeto
- Foi criado um ambiente virtual para instalar os pacotes e definir a versão do Python
- Alguns ficheiro presente nos códigos não foram adicionados ao GitHub por conterem dados sensíveis
- Esse projeto faz parte do início dos meus estudos na área de Engenharia de Dados

## Descrição das etapas do ETL com a explicação dos códigos
1) **Importação de Bibliotecas:** O pacote 'pandas' é usado para manipulação de dados em DataFrame, 're' para expressões regulares que vão segmentar o conteúdo do campo 'descritivo' e 'datetime' para manipulação de datas (não foi necessário, mas pode ser útil caso precise de conversões de data/hora).

2) **Extração dos Dados:** Simulamos a leitura dos dados extraídos de um ficheiro .ics e os transformamos em um DataFrame para facilitar o processamento. Na prática, você utilizaria bibliotecas específicas para ler arquivos .ics e converter para uma estrutura manipulável.

3) **Transformação dos Dados:** A função 'tratar_descritivo' é responsável por limpar o HTML usando uma expressão regular (re.sub(r'<[^>]+>', '', descritivo)) e depois segmentar as partes importantes do descritivo, como o link do Google Maps, o ponto de referência, telefone, valor, etc., utilizando outras expressões regulares.

4) **Exportação dos Dados:** A exportação dos dados pode ser feita automaticamente para um arquivo CSV usando df_final.to_csv(). Para exportação manual, o comando df_final.to_clipboard() permite copiar os dados para a área de transferência, permitindo colá-los em outra aplicação, como uma planilha do Excel.

**Considerações Finais:**
Este pipeline pode ser adaptado para lidar com dados maiores, complexos e outras fontes de dados.

A parte de "segmentação" do campo 'descritivo' pode precisar de ajustes dependendo da variação dos dados presentes no seu ficheiro .ics.

As exportações podem ser configuradas de acordo com a necessidade, seja para banco de dados, APIs ou outros sistemas.
