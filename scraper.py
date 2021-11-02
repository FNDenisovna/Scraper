# This is a sample Python script.
import random
import requests
from datetime import datetime
from bs4 import BeautifulSoup

#costants
reqLogFile = 'logs.txt'
testLogFile = 'test_logs.txt'
defLink = 'https://www.kinopoisk.ru'

def reqLogger(data):
    now = datetime.now()
    #"{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    try:
        fStream = open(reqLogFile, 'a', encoding='utf-8')
        if type(data) is requests.models.Response:
            text = ('   ').join(now, data.status_code, data.reason, data.url )
        try:
            fStream.write(text)
        except Exception as e:
            print(e)
        finally:
            fStream.close()
    except Exception as ex:
        print(ex)

def reqLink(wlink):
    response = requests.get(wlink)
    #print(f'Результат подключения к сайту:\n{response}')
    if response.status_code == 200:
        #print(type(response))
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        testLogger(soup.prettify())
        return soup
    else:
        reqLogger(response)
        return ''

def testLogger(data):
    now = datetime.now()
    try:
        fStream = open(testLogFile, 'w',  encoding='utf-8')
        try:
            fStream.write(data)
        except Exception as e:
            print(e)
        finally:
            fStream.close()
    except Exception as ex:
        print(ex)

def getFilm():
    wlink = 'https://www.kinopoisk.ru/lists/top250/'
    rowContent = reqLink(wlink)
    positionFilms = rowContent.findAll(lambda tag: tag.name == 'span' and tag.get('class') == ['film-item-rating-position__position'])
    positionFilms = [link.get_text() for link in positionFilms]
    filmNames = rowContent.findAll(lambda tag: tag.name == 'p' and tag.get('class') == ['selection-film-item-meta__name'])
    filmNames = [link.get_text() for link in filmNames]
    filmLinks = rowContent.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['selection-film-item-meta__link'])
    filmLinks = [link.attrs['href'] for link in filmLinks]

    random.seed()
    i = random.randint(0,len(positionFilms))
    return '\n'.join(['Место в рейтинге: ' + positionFilms[i], filmNames[i], defLink + filmLinks[i]])

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #wlink = 'http://knowyourmeme.com/memes/all/page/1'
    #chatcod.


