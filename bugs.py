from bs4 import BeautifulSoup
import requests, openpyxl

def save() :
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(index=0,title="bugs")
    titles = take_title()
    singers = take_singer()
    ids = take_id()
    r = 1
    for i in range(0,100):
        ws.cell(row=r, column=1).value = titles[i]
        ws.cell(row=r, column=2).value = singers[i]
        ws.cell(row=r, column=3).value = ids[i]
        r += 1
    wb.save('bugs.xlsx')

def take_id() :
    id_list = []
    url = "https://music.bugs.co.kr/chart"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    songid = soup.select(
        '#CHARTrealtime > table > tbody > tr'
    )
    for i in range(0,100) :
        id_list.append(songid[i]['trackid'])
    return id_list

def take_title() : #title 가져옴
    title_list = []
    url = "https://music.bugs.co.kr/chart"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    select = '#CHARTrealtime > table > tbody > tr > th > p > a'
    titles = soup.select(
        select
    )
    for title in titles:
        title_list.append(title.text)
    return title_list

def take_singer() : #가수 가져옴
    singer_list = []
    url = "https://music.bugs.co.kr/chart"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    select = '#CHARTrealtime > table > tbody > tr > td > p > a'
    names = soup.select(
        select
    )
    for name in names:
        singer_list.append(name.text)
    return singer_list    

if __name__ == "__main__":
    save()
    #print(take_id())
    #print(take_title())
    #print(take_singer())
