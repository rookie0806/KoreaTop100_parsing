from bs4 import BeautifulSoup
import requests, openpyxl, codecs
import re

def save() :
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(index=0,title="naver")
    titles = take_title()
    singers = take_singer()
    #print(len(titles))
    ids = take_id()
    r = 1
    for i in range(0,100):
        ws.cell(row=r, column=1).value = titles[i]
        ws.cell(row=r, column=2).value = singers[i]
        ws.cell(row=r, column=3).value = ids[i]
        r += 1
    wb.save('naver.xlsx')

def take_id() :
    id_list = []
    for i in range(1,3):
        url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&page=" + str(i) 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        songid = soup.select(
            '#content > div > div._tracklist_mytrack.tracklist_table.tracklist_type1'
        )
        for j in range(1,51):
            songnum = songid[0]['artistdata'].split('{\\"')[j].split('\\"')[0]
            id_list.append(songnum)
    return id_list
       

def take_title() : #title 가져옴
    title_list = []
    for i in range(1,3):
        url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&page=" + str(i) 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        select = '#content > div > div > table > tbody > tr > td.name > a > span'
        titles = soup.select(
            select
        )
        for title in titles:
            title_list.append(title.text)
    return title_list

def take_singer() : #가수 가져옴
    singer_list = []
    for i in range(1,3):
        url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&page=" + str(i) 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        select = '#content > div > div > table > tbody > tr > td._artist.artist > a'
        names = soup.select(
            select
        )
        for name in names:
            singer = name.text
            singer = singer.replace('\r','')
            singer = singer.replace('\n','')
            singer = singer.replace('\t','')
            singer_list.append(singer)
    return singer_list  

if __name__ == "__main__":
    save()
    #print(take_id())
    #print(take_title())
    #print(take_singer())
