import urllib.request, urllib.error, urllib.parse
import requests
import http.cookiejar
from getpass import getpass
import sys
import os
from stat import *
import re
msg_base= requests.get("http://www.hltv.org/").text
def hltvInfoGet(num,username,passwd):
    global msg_base
    try:
        msg= msg_base
        msg= msg[msg.find("newstext"):]
        msg= msg[msg.find(">"):msg.find("</div>")]
        msg1 = msg_base
        msg1 = msg1[msg1.find("newstext"):]
        msg1 = msg1[msg1.find("</div>"):]
        msg1 = msg1[msg1.find("newstext"):]
        msg1 = msg1[msg1.find(">"):msg1.find("</div>")]
        msg2 = msg_base
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find("</div>"):]
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find("</div>"):]
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find(">"):msg2.find("</div>")]
        msg = "CS NEWS: "+msg+", "+msg1+", "+msg2+"."
        msg= msg.replace("&amp;","and")
        smsSend(msg,num,username,passwd)
    except:
        cronJob()
def smsSend(message,number,username,passwd):
    try:
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
    except:import urllib2
import requests
import cookielib
from getpass import getpass
import sys
import os
from stat import *
import re
msg_base= requests.get("http://www.hltv.org/").text
def hltvInfoGet(num,username,passwd):
    global msg_base
    try:
        msg= msg_base
        msg= msg[msg.find("newstext"):]
        msg= msg[msg.find(">"):msg.find("</div>")]
        msg1 = msg_base
        msg1 = msg1[msg1.find("newstext"):]
        msg1 = msg1[msg1.find("</div>"):]
        msg1 = msg1[msg1.find("newstext"):]
        msg1 = msg1[msg1.find(">"):msg1.find("</div>")]
        msg2 = msg_base
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find("</div>"):]
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find("</div>"):]
        msg2 = msg2[msg2.find("newstext"):]
        msg2 = msg2[msg2.find(">"):msg2.find("</div>")]
        msg = "CS NEWS: "+msg+", "+msg1+", "+msg2+"."
        msg= msg.replace("&amp;","and")
        smsSend(msg,num,username,passwd)
    except:
        cronJob()
def smsSend(message,number,username,passwd):
    try:
        message = "+".join(message.split(' '))
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
        cj= cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock =opener.open(url, data)
        except IOError:
            print "error"
        jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print "error"
        print "success"
    except:
        cronJob()
def cronJob():
    global msg_base
    msg_base= requests.get("http://www.hltv.org/").text
    hltvInfoGet("9798556787","9472713842","R3249K") #Aakash Pahwa
    
    print "********************************"
cronJob()

        cronJob()
def cronJob():
    global msg_base
    msg_base= requests.get("http://www.hltv.org/").text
    hltvInfoGet("recipient","userid","password") 
    
    print("********************************")
cronJob()
