# ----------------------------
# author: Thiago Almeida
# e-mail: thiagodons@gmail.com
# year: 2021
# ----------------------------
import requests 
from bs4 import BeautifulSoup
from requests.sessions import Request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_http(url, nome_livro):
    nome_livro = nome_livro.replace(' ', '%20')
    print(nome_livro)
    url = "{0}{1}".format(url, nome_livro)
    print(url)
    try :
        return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.exceptions.ConnectionError, requests.exceptions.Timeout ) as e :
        print(str(e))
        pass
    except Exception as e :
        raise 

def get_detalhes(produto_url):
    try :     
        browser = webdriver.Chrome('./chromedriver')
        browser.get(produto_url)
        time.sleep(5)
        browser.refresh()
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()
        descricao = soup.select('#descricao')[0].text
        preco = soup.select('.price-destaque')[0].text
        ano_ed = soup.find(id='receba').div.table.tbody.tr.find_next_sibling('tr').td.find_next_sibling('td').string
        return [descricao, preco, ano_ed]
    except Exception as e :
        print(f"erro aqui {e}")

def get_url_prod(conteudo):
    soup = BeautifulSoup(conteudo, 'lxml')
    prods = soup.find_all('div', {'class': 'product _prdv'})
    produtos = []
    for prod in prods :
        info_prod = [prod.a.get('href'), prod.h3.a.string]
        detalhes = get_detalhes(info_prod[0])
        produtos.append(info_prod + detalhes)
    return produtos

if __name__ == '__main__':
    url = 'https://www.saraiva.com.br/'
    nome_livro = input('Digite o nome do livro: ')
    request = get_http(url, nome_livro)
    if request :
        lista_produtos = get_url_prod(request.text)
        for produto in lista_produtos:
            print('-------------------------------------------------------------------------------')
            print(f'Livro: {produto[1]} ')
            print(f'Descrição: {produto[2]} ')
            print(f'Preço: {produto[3]} ')
            print(f'Ano de publicação: {produto[4]}')
            print(f'link para compra: {produto[0]}')
            print('-------------------------------------------------------------------------------')



 