from bs4 import BeautifulSoup
import requests, openpyxl

def save() :
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(index=0,title="melon")
    titles = take_title()
    singers = take_singer()
    ids = take_id()
    r = 1
    for i in range(0,100):
        ws.cell(row=r, column=1).value = titles[i]
        ws.cell(row=r, column=2).value = singers[i]
        ws.cell(row=r, column=3).value = ids[i]
        r += 1
    wb.save('melon.xlsx')

def take_id() :
    id_list = []
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    songid1 = soup.select(
        '#lst50 > td > div > input'
    )
    songid2 = soup.select(
        '#lst100 > td > div > input'
    )
    for i in range(0,50):
        id_list.append(songid1[i]['value'])
    for i in range(0,50):
        id_list.append(songid2[i]['value'])
    return id_list

def take_title() : #title 가져옴
    title_list = []
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    for i in range(0,2):
        if i==0:
            select_t = '#lst50 > td > div > div > div.ellipsis.rank01 > span > a'
        else:
            select_t = '#lst100 > td > div > div > div.ellipsis.rank01 > span > a'
        titles = soup.select(
            select_t
        )
        for title in titles:
            title_list.append(title.text)
    return title_list

def take_singer() : #가수 가져옴
    singer_list = []
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    names = soup.find_all('span', {'class' : 'checkEllipsis'})
    for name in names:
        singer_list.append(name.text)
    return singer_list    

if __name__ == "__main__":
    save()
    #print(take_id())
    #print(take_singer())
    #print(take_title())