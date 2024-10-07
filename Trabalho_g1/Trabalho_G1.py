import requests
from bs4 import BeautifulSoup
import re

# Função para converter o preço para um formato numérico
def parse_price(price_str):
    # Remove o símbolo 'R$', espaços e converte a vírgula em ponto
    cleaned_price = re.sub(r'[^\d,]', '', price_str)  # Remove todos os caracteres que não são dígitos ou vírgulas
    cleaned_price = cleaned_price.replace(',', '.')  # Converte a vírgula em ponto para a conversão a float
    try:
        return float(cleaned_price)  # Tenta converter a string limpa para float
    except ValueError:
        return float('inf')  # Se o preço não for convertível, trata como infinito

# URL da página de jogos mais vendidos da Steam
url = 'https://store.steampowered.com/search/?filter=topsellers'

# Enviar uma requisição HTTP para a URL
response = requests.get(url)  # Faz a requisição para a URL
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida; levanta um erro se não foi


soup = BeautifulSoup(response.text, 'html.parser')  # Cria um objeto BeautifulSoup para manipular o HTML


games = []  


for game_div in soup.find_all('div', class_='responsive_search_name_combined'):  # Encontra todos os divs que contêm informações de jogos
    # Extrair o nome do jogo
    name = game_div.find('span', class_='title')  
    if name:
        name = name.text.strip()  # Se encontrado, remove espaços em branco
    else:
        continue  

    # Extrair o preço do jogo
    price_div = game_div.find('div', class_='discount_final_price')  
    if price_div:
        price = price_div.get_text(strip=True)  
    else:
        price = 'Preço não disponível'  # Se não houver preço, define como não disponível

    # Extrair a data de lançamento do jogo
    data = game_div.find('div', class_='col search_released responsive_secondrow')  
    if data:
        data_lancamento = data.text.strip()  
    else:
        data_lancamento = 'Não disponível'  

   
    games.append({'name': name, 'price': price, 'date': data_lancamento})  # Adiciona um dicionário com os dados do jogo à lista

# Adicionar uma chave de preço numérico para ordenação
for game in games:
    game['numeric_price'] = parse_price(game['price'])  # Converte o preço para um valor numérico para ordenação


def quick_sort(games, inicio, fim, chave):
    if inicio < fim:
        pivo = particiona(games, inicio, fim, chave)  # Particiona a lista
        quick_sort(games, inicio, pivo - 1, chave)  # Recursão na parte esquerda
        quick_sort(games, pivo + 1, fim, chave)  # Recursão na parte direita

def particiona(games, inicio, fim, chave):
    pivo = games[fim][chave]  # Define o valor do pivô com base na chave
    esquerda = inicio  # Inicializa a variável esquerda
    for direita in range(inicio, fim):  # Percorre a lista
        if games[direita][chave] <= pivo:  # Para ordenar do menor para o maior
            games[esquerda], games[direita] = games[direita], games[esquerda]  
            esquerda += 1  # Move o índice da esquerda para a direita
    games[esquerda], games[fim] = games[fim], games[esquerda]  # Coloca o pivô na posição correta
    return esquerda  # Retorna o índice do pivô


quick_sort(games, 0, len(games) - 1, 'numeric_price')  

for game in games:
    print(f"\033[96mNome: {game['name']} \nPreço: {game['price']} \nData Lançamento: {game['date']}\033[m \n")  
