from bs4 import BeautifulSoup
import requests, openpyxl

def save() :
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(index=0,title="genie")
    titles = take_title()
    singers = take_singer()
    ids = take_id()
    r = 1
    for i in range(0,100):
        ws.cell(row=r, column=1).value = titles[i]
        ws.cell(row=r, column=2).value = singers[i]
        ws.cell(row=r, column=3).value = ids[i]
        r += 1
    wb.save('genie.xlsx')

def take_id() :
    id_list = []
    url = "http://www.genie.co.kr/chart/top200"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    songid = soup.select(
        '#sAllSongID'
    )
    for i in range(0,100) :
        id_list.append(songid[0]['value'].split(";")[i])
    return id_list

def take_title() : #title 가져옴
    title_list = []
    for i in range(1,3):
        url = "http://www.genie.co.kr/chart/top200?pg=" + str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        select_t = '#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis'
        titles = soup.select(
            select_t
        )
        for title in titles:
            title_list.append(title.text.split('\n                                                ')[1])
    return title_list

def take_singer() : #가수 가져옴
    singer_list = []
    for i in range(1,3):
        url = "http://www.genie.co.kr/chart/top200?pg=" + str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        select_t = '#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis'
        names = soup.select(
            select_t
        )
        for name in names:
            singer_list.append(name.text)
    return singer_list    

if __name__ == "__main__":
    save()
    #print(take_id())
    #print(take_title())
    #print(take_singer())
