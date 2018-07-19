import requests
from bs4 import BeautifulSoup
from Crypto.PublicKey import RSA
import Crypto
import os
import base64
import json
import js2py
import execjs
#cookies = {'MAC': 'h7vSo4nQqQgeYEYpphbveOWWxnzEnUNhWndwKhzFwpMLlLXlGenypE1NUM6Qpld/', "keyCookie": '20743826'}
cookies = {'PCID':'1'}
def getHtml(url):
   _html = ""
   #resp = requests.get(url, cookies=cookies)
   referer = "https://www.melon.com/"
   user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
   headers = {'User-Agent': user_Agent, 'Referer' : referer}
   resp = requests.get(url,headers=headers, cookies=cookies)
   print(resp.content.decode())
   return _html

def encrypt(pub, primen, plaintext):
    key = int(pub,16)
    n = primen
    cipher = [(ord(char) ** key) % n for char in plaintext]
    print(cipher)
    return cipher

def usingjs():
    filename = r"C:\Users\BYEONGMINCHAE\Desktop\DB\KoreaTop100_parsing\rsa.js"
    #print(rsa.AuthRSA)

def GetPub():
    url = "https://www.melon.com/muid/web/authentication/authentication_getRSAPublic.json"
    _html = ""
    referer = "https://www.melon.com/"
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {'User-Agent': user_Agent, 'Referer' : referer}
    resp = requests.post(url,headers=headers, cookies=cookies)
    #print  (resp.content.decode())
    publickey = resp.content.decode().replace('"',"").split("publickey:")[1].split(",")[0]
    print(int(publickey,16))
    return publickey
    #print(resp.content.decode())

def login(memberid,memberpw):
    publickey = GetPub()
    publickey = "be0ae624d65b134d7863f964fa8db287e49f07cdb08e6414167c9d3c0580cecd19aed9fc939fe3230b453c3da4c85379fbc3bad0c2c0c4e891e20981e810d16df2ddd6ba33ebbd9052bf0c9add4bf4307a34ccb72bcc1170bd1612b926b06987c9ef75bcdf282bbc0e2e147549e64ec41ddf9bef2f17f472af78c28185f21619"
    memberid = encrypt(publickey,10001,memberid)
    memberpw = encrypt(publickey,10001,memberpw)
    data = {'memberId': memberid, 'memberPwd' : memberpw, 'publicKey' : publickey, 'saveId' : 'N'}
    url = "https://member.melon.com/muid/web/login/login_informProcs.htm?returnPage=https%3A%2F%2Fwww.melon.com%2F"
    referer = "https://www.melon.com/"
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    headers = {'User-Agent': user_Agent, 'Referer' : referer}
    #resp = requests.post(url,headers=headers, cookies=cookies, data=data)
    #print(resp.content.decode())

def RSAf():
    pass


if __name__ == "__main__":
    #GetPub()
    #login("jbshs2013","ehdgnl@806")
    #usingjs()
    pass