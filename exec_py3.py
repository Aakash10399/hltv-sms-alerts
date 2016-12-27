import urllib.request, urllib.error, urllib.parse
import requests
import http.cookiejar
from getpass import getpass
import sys
import os
from stat import *
import re
import time

def checkForUpdates():
    msg= requests.get("http://www.hltv.org/").text
    msg= msg[msg.find("newsRight"):]
    msg= msg[msg.find("<b>")+3:msg.find("</b>")]    
    flag=0
    readMe = open('hltv.txt','r').read()    
    if readMe!=msg:
        flag=1
        saveFile = open('hltv.txt','w')
        saveFile.write(msg)
        saveFile.close()
    return flag    
def hltvInfoGet(num,username,passwd):
    msg= requests.get("http://www.hltv.org/").text
    msg= msg[msg.find("newsRight"):]
    msg= msg[msg.find("<b>")+3:msg.find("</b>")]
    msg1= requests.get("http://www.hltv.org/").text
    msg1= msg1[msg1.find("newsRight"):]
    msg1= msg1[msg1.find("</b>")+4:]
    msg1= msg1[msg1.find("<b>")+3:msg1.find("</b>")]
    msg = "CSGO NEWS: "+msg+" , "+msg1+". Check www.hltv.org for more info."
    msg= msg.replace("&amp;","and")
    smsSend(msg,num,username,passwd)
def smsSend(message,number,username,passwd):    
    message = "+".join(message.split(' '))
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
    cj= http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print("error")
    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print("error")       
    print("success") 
def cronJob():
    while 0==0:
        rt = checkForUpdates()
        if rt==1:
            hltvInfoGet("number_to_send","way2smsuid","way2smspass") 
            print("********************************")    
        else:
            print("Old News")
            print("********************************")   
        refresh_rate = 1800 #in seconds
        time.sleep(refresh_rate)  
cronJob()
