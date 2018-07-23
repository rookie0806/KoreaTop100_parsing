import requests
from bs4 import BeautifulSoup
from Crypto.PublicKey import RSA
import Crypto
import os
import base64
import json
import js2py
import execjs
import execjs.runtime_names
import os
import codecs
from Naked.toolshed.shell import execute_js, muterun_js
import csv

def take_info(melon_url) :
    cookies = {'MLCP' : MLCP,'MAC': 'h7vSo4nQqQgeYEYpphbveOWWxnzEnUNhWndwKhzFwpMLlLXlGenypE1NUM6Qpld/',"keyCookie": '20743826'}
    global title_list
    title_list = []
    global artist_list
    artist_list = []
    global id_list
    id_list = []
    page = 1

    for i in range(0,2):
        referer = str(melon_url)
        url = str(melon_url) + "&memberKey=" + str(myid) + "&startIndex=" + str(page) + "&pageSize=50"
        headers = {'referer':referer,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'Upgrade-Insecure-Requests' : '1'}
        req = requests.get(url,headers=headers, cookies=cookies)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        songid = soup.select(
            '#frm > div > table > tbody > tr > td > div > input'
        )
        artists = soup.select(
            '#artistName'
        )
        titles = soup.select(
            '#frm > div > table > tbody > tr > td > div > div > button.btn_icon.play'
        )
        for j in range(0,len(artists)):
            title_list.append(titles[j]["title"].split(" 재생")[0])
            artist_list.append(artists[j].text.replace("\n",""))  
            id_list.append(songid[j]["value"])  
        page = page+50

    
def getHtml(url):
   referer = "https://www.melon.com/"
   html = ""
   cookies = {'PCID':'1'}
   user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
   headers = {'User-Agent': user_Agent, 'Referer' : referer}
   resp = requests.get(url,headers=headers, cookies=cookies)
   print(resp.content.decode())
   return html

def GetPub():
    cookies = {'PCID':'1'}
    url = "https://www.melon.com/muid/web/authentication/authentication_getRSAPublic.json"
    _html = ""
    referer = "https://www.melon.com/"
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {'User-Agent': user_Agent, 'Referer' : referer}
    resp = requests.post(url,headers=headers, cookies=cookies)
    publickey = resp.content.decode().replace('"',"").split("publickey:")[1].split(",")[0]
    return publickey

def login():
    cookies = {'PCID':'1'}
    global myid
    global MLCP
    publickey = rsakey
    memberid = rsaid
    memberpw = rsapw
    data = {'memberId': memberid, 'memberPwd' : memberpw, 'publicKey' : publickey, 'saveId' : 'N'}
    url = "https://member.melon.com/muid/web/login/login_informProcs.htm"
    referer = "https://member.melon.com/muid/web/login/login_inform.htm"
    content = "application/x-www-form-urlencoded"
    accept = "gzip, deflate, br"
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {'accpet-encoding':accept,'content-type':content,'User-Agent': user_Agent, 'Referer' : referer}
    resp = requests.post(url,headers=headers, cookies=cookies, data=data)
    myid = resp.cookies["keyCookie"]
    MLCP = resp.cookies["MLCP"]

def RSAf(melon_id,melon_pw):
    global rsakey 
    global rsaid
    global rsapw
    publickey = GetPub()
    f = codecs.open('rsa4.js','r','utf-8').read()
    myjs = execjs.get()
    compjs = myjs.compile(f)
    rsakey = publickey
    rsacall = compjs.call("a",publickey,melon_id,melon_pw)
    rsaid = rsacall.split("/")[0] 
    rsapw = rsacall.split("/")[1]
    login()

def save(filename):
    file = str(filename) + '.csv'
    with open( file, 'w', newline='') as csvfile:
        fieldnames = ['Music_id','Music_title', 'Music_artist']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,len(id_list)):
            writer.writerow({'Music_id': id_list[i], 'Music_title': title_list[i], 'Music_artist' : artist_list[i]})

if __name__ == "__main__":
    melon_id = "kpho1541"
    melon_pw = "ehdgnl@806"
    RSAf(melon_id,melon_pw)
    #print(take_id())   
    myid = "42501678"
    take_info("https://www.melon.com/mymusic/recent/mymusicrecentsong_list.htm?")
    save("recent")
    take_info("https://www.melon.com/mymusic/top/mymusictopmanysong_list.htm?dateType=3M")
    save("top")
    pass