from bs4 import BeautifulSoup as bs
import requests

baseurl="https://zlibrary.to/"



def searchbook(query:str):
    query=query.lower()
    query=query.replace(" ","-")
    query=query.replace("(","")
    query=query.replace(")","")
    query=query.replace(".","")
    search=baseurl+"top-"+query+"-books"
    url = requests.get(search)
    url=url.text
    soup=bs(url,"html.parser")
    texts = soup.find_all('a')
    searchresults=[]
    for text in texts:
        names=(text.get_text())
        searchresults.append(names)
    del searchresults[0:8]
    del searchresults[-8:-1]
    for i in range(0,10):
        number=i+1
        number=str(number)
        print(number+"."+searchresults[i])
    return searchresults

def selectbook(query:str,selection:int):
    query=query.lower()
    query=query.replace(" ","-")
    query=query.replace("(","")
    query=query.replace(")","")
    query=query.replace(".","")
    search=baseurl+"top-"+query+"-books"
    url = requests.get(search)
    url=url.text
    soup=bs(url,"html.parser")
    texts = soup.find_all('a')
    searchresults=[]
    for text in texts:
        names=(text.get_text())
        searchresults.append(names)
    del searchresults[0:8]
    del searchresults[-8:-1]
    book=searchresults[selection-1]
    book=book.lower()
    book=book.replace("(","")
    book=book.replace(" - ","-")
    book=book.replace(" ","-")
    book=book.replace(")","")
    book=book.replace(".","")
    url="https://zlibrary.to/pdfs/"+book
    print(url)
