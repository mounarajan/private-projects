import os
import time
import re
from multiprocessing.pool import Pool
import requests
import csv

def wget_cookie(url):
    data = os.popen('wget -qO- --no-cookies --header "Cookie: PREF=ID=1111111111111111:FF=0:LD=en:TM=1436290443:LM=1436416084:GM=1:V=1:S=OAaQWZel2Z7y4x1p; NID=74=GLwB9lf6lZlA5_McRg8SlHSZ8yX1Kgyfg5Ws_8TxuMzk1PxAPTuo8rlQGSgiZMA-qLf30iwlQAtiz5rlitcVTHMOW7rOv9VvEATdigqequ1R7Vw-K2fDKYDXQx890ZeIr3VGCBpT_Y2qnVwkAQbuTeV96zbPOItcst2Vv65f3cWeL32iKowtBN-5plPXu8ryEhE-Y1mnSdfG9pO16fwPNP_xqMHM6nBVPu-7-Wxhd1Sva4RtZKJ7_mrIljfWbnb8pi3udFecv7HroY2L4N4Gg5npQbkJ789IdLmPy0QmZGpsXDEuq4CAat32c_EdmWSrXO0; SID=DQAAALkBAACNQ2_VECWVHHPvzPw5zeCz4i7sCGrZ-EPJnSstSx_bAHKaUK-sGsJz_NsCJarNpJ6qe-5Ts6fGe5c0FypLc0OKOcBiFEuNziFTPoNDFGVREU5RDBPd0s95-SrwlQyJYkIMbtad44X0QdEf52b9jX4sOFQ088XTCd3D5LBEycjM6Opsekt_ftzt1kp52LeDx8-jjBz4MW-_Z7TDlZaSNxoVy3w4IDFfll7gJf3u75Rc8EA78XTLUXh1DVfIq7oYtwGDQ36tZ6rnWHajS-toXtEDdUma1P5CRXr13OZ5pEwLAT8qGFc3q7GKelHa0l5HcSe6izm7BhoaZq_c4qspMOxfbDBBam3vGMOvqrzKBT6U7mIQuIidZYFWn--SePbFSN_JW3bExOGiwbvlagNX0M9LpU7CxdsbdNlxkcwq0466u-rI-eOnauauJWPvSVUuCIE_RxUsuDCw90lGGfT2wNFR5zBnMzC0VLctZFS-HhXjMkrs3-KxcUDYsRYEX2dbU4YV8uV9yg5JfEuufmMMKQNNqQKB-xBEmFScpVMvso9tmt3I7-0T7bXi9NaYcZ6cD0BZXFHJ7zmRQ_MVI6kXUTXZ; HSID=ATVQjd3hxGbpcRAUF; SSID=AZjLdgea1C8pxyeyc; APISID=soBn4_aazTI4Wywn/ADRCh3F_lHo-hPEXx; SAPISID=vhXD61-cvsSQwADN/A8hDmgS1-sePcS7Rp; _ga=GA1.3.1983500809.1437616179; OGPC=4061155-2:; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=mounarajan@semantics3.com; PLAY_PREFS=CtwDCKrLu9TFChLSAwoCSU4Q8Pn0zZgqGpcDERITFBUWGNQB1QGDAqsC2QPCBMQE4wXlBegF1wbYBt4G3wbdD_APkJWBBpGVgQaSlYEGk5WBBpWVgQaXlYEGpJWBBq2VgQa4lYEGwZWBBsSVgQbFlYEGyJWBBs6VgQbPlYEG0JWBBtSVgQbZlYEG65WBBuyVgQbtlYEG8pWBBviVgQb5lYEGhpaBBoiWgQaMloEGj5aBBpCWgQaeloEGn5aBBqCWgQahloEGppaBBqeWgQaoloEGypeBBu6XgQbvl4EGgZiBBoWYgQa-mIEGiJqBBqObgQatm4EGy5uBBrudgQa8nYEGw52BBsSdgQbFnYEGxp2BBsedgQbdnYEG7J2BBpCegQbon4EG-5-BBoCggQakoIEG9aCBBoShgQaQoYEGwKGBBsuhgQbMoYEGzaGBBu6hgQbxoYEG4qKBBvOigQaxo4EGmqSBBrKkgQbvpIEGhKWBBq-lgQbqpYEGnaaBBsamgQa3p4EGx6eBBo-ogQbNqIEGvKyBBoOugQaZr4EG1q-BBtivgQbjr4EGlbCBBuD8nDEo8Pn0zZgqOiQxYTBmN2Q0Yy1hZDNlLTQ2NTAtYmU3Ny1jYmY1Njk3ZmI2YjQ:S:ANO1ljKOEhExS4ysyg; _gat=1;" %s'% url).read()
    print data

def wget_sepcial(url):
    data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
    return data

def urlLib(url):
    
    user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
    headers = {'User-Agent': user_agent}
    data = requests.get(url,headers = headers,verify=False)
    return data.text.encode('utf-8')

def curl(url):

	url = url 
	data = os.popen('curl --silent --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" %s >/dev/null'% url).read()
	return data

os.popen('rm demo_data.csv')
f4 = open("demo_data.csv", 'at')
writer = csv.writer(f4,delimiter = ',', lineterminator='\n',quoting=csv.QUOTE_ALL)
headers = ['Business Category','Sub Category','Company Name','Address','Contact Number 1','Contact Number 2','Area','City','Pincode','Year Establish','Source Link']
writer.writerow(headers)


def crawl(url):

    os.popen('rm cat-urls.txt')
    f2 = open('cat-urls.txt','a')
    data = wget_sepcial(url)
    data = str(data)
    print data
    print "done"
    if re.search(r'(?mis)<li><a\sHREF\=\"([^\"]*)\"\stitle',data):
        urls = re.findall(r'(?mis)<li><a\sHREF\=\"([^\"]*)\"\stitle',data)
        for url in urls:
          url = re.sub(r'^','http://justdial.com/Hyderabad/',url)
          f2.write(url+"\n")
          print url
            
            

    if re.search(r'(?mis)<li style\=\"\"><a\sHREF\=\"([^\"]*)\"\stitle',data):
        urls = re.findall(r'(?mis)<li style\=\"\"><a\sHREF\=\"([^\"]*)\"\stitle',data)
        for url in urls:
          url = re.sub(r'^','http://justdial.com/Hyderabad/',url)
          f2.write(url+"\n")
          print url

def sub_cat(url):
    #os.popen('rm demo_data.csv')
    
    os.popen('rm sub-cat-urls.txt')
    f3 = open('sub-cat-urls.txt','a')
    url = re.sub(r'\n','',url)
    url = re.sub(r'&','\&',url)
    url = re.sub(r';','\;',url)
    #url = re.sub(r'.html','',url)
    url = re.sub(r'_.*','',url)
    print url
    data = wget_sepcial(url)
    data = str(data)

    if re.search(r'(?mis)javascript\:location\.href\=\'([^\']*)\'',data):
        urls = re.findall(r'(?mis)javascript\:location\.href\=\'([^\']*)\'',data)
        for url in urls:
            data_store = []
            f3.write(url+"\n")
            
            url = re.sub(r'&','\&',url)
            url = re.sub(r';','\;',url)
            
            print url
            data = wget_sepcial(url)
            data = str(data)

            if re.search(r'(?mis)comp-text also-list more ">[^>]*>\s*[^<]*\s*<\/a>[^>]*>[^>]*>\s*([^<]*)\s*<',data):
                cat = re.findall(r'(?mis)comp-text also-list more ">[^>]*>\s*[^<]*\s*<\/a>[^>]*>[^>]*>\s*([^<]*)\s*<',data)[0]
                print cat
                data_store.append(cat)
            else:
                data_store.append('')

            if re.search(r'(?mis)comp-text also-list more ">[^>]*>[^>]*>\s*([^<]*)\s*<',data):
                sub_cat = re.findall(r'(?mis)comp-text also-list more ">[^>]*>[^>]*>\s*([^<]*)\s*<',data)[0]
                data_store.append(sub_cat)
            else:
                data_store.append('')

            if re.search(r'(?mis)<h1[^>]*>[^>]*>[^>]*>\s*([^<]*)\s*<',data):
                name = re.findall(r'(?mis)<h1[^>]*>[^>]*>[^>]*>\s*([^<]*)\s*<',data)[0]
                data_store.append(name)
            else:
                data_store.append('')

            if re.search(r'(?mis)comp\_add\"\>\s*([^<]*)\s*<',data):
                address = re.findall(r'(?mis)comp\_add\"\>\s*([^<]*)\s*<',data)[0]
                data_store.append(address)
            else:
                data_store.append('')

            if re.search(r'(?mis)telCntct">[^>]*><a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)<\/a>',data):
                tel1 = re.findall(r'(?mis)telCntct">[^>]*><a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)<\/a>',data)[0]
                data_store.append(tel1)
            elif re.search(r'(?mis)telCntct">\s*<a\sclass\=\"tel\"\shref\=[^>]*><b>\s*([^<]*)\s*<',data):
                tel1 = re.findall(r'(?mis)telCntct">\s*<a\sclass\=\"tel\"\shref\=[^>]*><b>\s*([^<]*)\s*<',data)[0]
                data_store.append(tel1)
            elif re.search(r'(?mis)telCntct">\s*<a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)\s*<',data):
                tel1 = re.findall(r'(?mis)telCntct">\s*<a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)\s*<',data)[0]
                data_store.append(tel1)
            else:
                data_store.append('')

            if re.search(r'(?mis)telCntct">[^>]*><a\sclass\=\"tel\"\shref\=[^>]*>\s*[^<]*<\/a>\,\s*<a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)<\/a>',data):
                tel2 = re.findall(r'(?mis)telCntct">[^>]*><a\sclass\=\"tel\"\shref\=[^>]*>\s*[^<]*<\/a>\,\s*<a\sclass\=\"tel\"\shref\=[^>]*>\s*([^<]*)<\/a>',data)[0]
                data_store.append(tel2)
            else:
                data_store.append('')

            if re.search(r'(?mis)dtpg\'\)\;\"\stitle\=\"[^\,]*\,\s([^\"]*)\"',data):
                area = re.findall(r'(?mis)dtpg\'\)\;\"\stitle\=\"[^\,]*\,\s([^\"]*)\"',data)[0]
                data_store.append(area)
            else:
                data_store.append('')

            if re.search(r'(?mis)map\'\,\s\'([^\']*)\'',data):
                city = re.findall(r'(?mis)map\'\,\s\'([^\']*)\'',data)[0]
                data_store.append(city)
            else:
                data_store.append('')

            if re.search(r'(?mis)pincode\=(\d+)',data):
                pincode = re.findall(r'(?mis)pincode\=(\d+)',data)[0]
                data_store.append(pincode)
            else:
                data_store.append('')

            if re.search(r'(?mis)mreinfp">Yea[^>]*>[^>]*>[^>]*>\s*([^<]*)\s*<',data):
                yoe = re.findall(r'(?mis)mreinfp">Yea[^>]*>[^>]*>[^>]*>\s*([^<]*)\s*<',data)[0]
                data_store.append(yoe)
            else:
                data_store.append('')

            if re.search(r'(?mis)mreinflispn1">\s*([^<]*)<',data):
                wh_l = len(re.findall(r'(?mis)mreinflispn1">\s*([^<]*)<',data))
                print wh_l
                wh = re.findall(r'(?mis)mreinflispn1">\s*([^<]*)<',data)
                if wh_l >= 2:
                    whl1 = wh[1]
                else:
                    whl1 = ''
                wh = whl1+'-'+wh[wh_l - 1]
                data_store.append(wh)
            else:
                data_store.append('')

            data_store.append(url)

            writer.writerow(data_store)
        



    #print urls
    #for url in urls:
        #data = wget_sepcial(url)
        #data = str(data)
        #if re.search(r'(?mis)<li><a\sHREF\=\"([^\"]*)\"\stitle',data):
         #   urls = re.findall(r'(?mis)<li><a\sHREF\=\"([^\"]*)\"\stitle',data)
          #  for url in urls:
           #     urls.append(url)

    


crawl("http://hyderabad.justdial.com/category-1.html")
#3def get_urls1():
  #  f2 = open('cat-urls.txt','r')
#
   # nprocs = 50 # nprocs is the number of processes to run
    #ParsePool = Pool(nprocs)
    #ParsedURLS = ParsePool.map(sub_cat,f2)
#get_urls1()
f2 = open('cat-urls.txt','r')
for url in f2:
    sub_cat(url)
