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

#definindo url e uri livro 
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
        time.sleep(10)
        browser.refresh()
        time.sleep(10)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()
        detalhes = soup.find_all('div', {'id':'descricao'})
        for detalhe in detalhes:
            print(detalhe)
        return requests.get(produto_url)
    except Exception as e :
        print(f"erro aqui {e}")

def get_url_prod(conteudo):
    soup = BeautifulSoup(conteudo, 'lxml')
    prods = soup.find_all('div', {'class': 'product _prdv'})
    produtos = []
    for prod in prods :
        info_prod = [prod.a.get('href'), prod.h3.a.string]
        produtos.append(info_prod)
        get_detalhes(info_prod[0])
        #if request:
        #    info_prod.append() 
    #return produtos


if __name__ == '__main__':
    url = 'https://www.saraiva.com.br/'
    nome_livro = input('Digite o nome do livro: ')
    request = get_http(url, nome_livro)
    if request :
        print(request.status_code)
        print(get_url_prod(request.text))

    #with open('results.html', 'w', encoding='utf-8') as f :
    #    f.write(r.text)




 