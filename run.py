import requests 
from bs4 import BeautifulSoup
from requests.sessions import Request

#definindo url e uri livro 
def get_http(url, nome_livro):
    nome_livro = nome_livro.replace(' ', '%20')
    #print(nome_livro)
    url = "{0}{1}".format(url, nome_livro)
    #print(url)

    try :
        return requests.get(url)
    
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.exceptions.ConnectionError, requests.exceptions.Timeout ) as e :
        print(str(e))
        pass
    
    except Exception as e :
        raise 


def get_url_prod(conteudo):

    soup = BeautifulSoup(conteudo, 'lxml')
    prods = soup.find_all('div', {'class': 'product _prdv'})

    produtos = []
    for prod in prods :
        info_prod = [prod.a.get('href'), prod.h3.a.string]
        produtos.append(info_prod)
    
    return produtos




if __name__ == '__main__':

    url = 'https://www.saraiva.com.br/'
    nome_livro = input('Digite o nome do livro: ')

    request = get_http(url, nome_livro)

    if request :
        print(get_url_prod(request.text))

    #with open('results.html', 'w', encoding='utf-8') as f :
    #    f.write(r.text)




 