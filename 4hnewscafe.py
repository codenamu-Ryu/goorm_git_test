#4hnewscafe6.py
#4hplayground 중고등활동보고 추가

import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import sys, os, time

import smtplib
from email.mime.text import MIMEText

def error_email() :
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    #smtp = smtplib.SMTP('smtp-relay.gmail.com', 587)
    smtp.ehlo()      # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('ysh1797@gmail.com', 'ugertszlfgagipcx')
    #smtp.login('shyu@codenamu.co.kr', 'rphxekufwguflvvt')
    msg = MIMEText('4H.py Error')
    msg['Subject'] = '4H.py Error'
    msg['To'] = 'ysh1797@gmail.com'
    smtp.sendmail('ysh1797@gmail.com', 'shyu@codenamu.co.kr', msg.as_string())

    smtp.quit()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('C:/chromedriver', options = options)
#print("content-type: text/html; charset=utf-8\n")
#def loop():
url = 'http://www.4hnews.kr/'
html = requests.get(url).text

#soup = BeautifulSoup(html,"html5lib")
soup = BeautifulSoup(html,"html.parser")

title1 = soup.find_all(class_ = 'item martop-20')

board_title1 = []
board_subtitle1 = []
board_url1 = []
board_img1 = []
board_idxno1 = []
board_date1 = []
iurl = 0

for i in title1:
    try:
        board_url1.append(i.a.attrs['href'])
        board_idxno1.append(i.a.attrs['href'].split('idxno=')[1])
        title1 = i.find(class_='auto-titles' )
        title1 = title1.get_text().strip()
        content1 = i.find(class_='auto-sums' )
        content1 = content1.get_text().strip()
        board_title1.append(title1)
        board_subtitle1.append(content1)
        board_img1.append(i.em.attrs['style'].split('(')[1].strip('()'))
    except KeyError:
        board_img1.append('None')
        continue
print('4h 신문 농정 ')
print(board_idxno1)
print(board_url1)
print(board_title1)
print(board_subtitle1)
print(board_img1)


title2 = soup.find(id='skin-26').find_all(class_='item')

board_title2 = []
board_subheading2 = []
board_url2 = []
board_img2 = []
board_idxno2 = []

for i in title2:
    board_url2.append(i.a.attrs['href'])
    board_idxno2.append(i.a.attrs['href'].split('idxno=')[1])
    board_img2.append(i.em.attrs['style'].split('(')[1].strip('()'))
    title2 = i.find(class_='auto-titles')
    title2 = title2.get_text().strip()
    content2 = i.find(class_='auto-section')
    content2 = content2.get_text().strip()

    board_title2.append(title2)
    board_subheading2.append(content2)

print('4h 신문 청년농부')
print(board_idxno2)
print(board_url2)
print(board_title2)
print(board_subheading2)
print(board_img2)


title5 = soup.find(id='skin-61').find_all(class_='item')

board_title5 = []
board_name5 = []
board_url5 = []
board_img5 = []
board_idxno5 = []
none_imgurl = "https://atf.wowexample.com:8443/attach/logo.png"

for i in title5:
    try:
        board_url5.append(i.a.attrs['href'])
        board_idxno5.append(i.a.attrs['href'].split('idxno=')[1])
        title5 = i.find(class_='auto-titles')
        title5 = title5.get_text().strip()
        name5 = i.find(class_='auto-name')
        name5 = name5.get_text().strip()
        board_title5.append(title5)
        board_name5.append(name5)
        board_img5.append(i.em.attrs['style'].split('(')[1].strip('()'))
    except KeyError:
        board_img5.append(none_imgurl)
        continue

print('4h 신문  4h소식 ')
print(board_idxno5)
print(board_url5)
print(board_title5)
print(board_name5)
print(board_img5)


##korea4-h 알림 소식
url = 'https://www.korea4-h.or.kr/'
html = requests.get(url).text
driver.get(url)
#soup = BeautifulSoup(html,"html5lib")
soup = BeautifulSoup(driver.page_source,"html.parser")
#korea4-h 알림터
title6 = soup.find_all(class_='media-body')[0]
title6 = title6.find_all('li')
board_title6 = []
board_url6 = []
board_idxno6 = []

for i in title6:
    board_url6.append(i.a.attrs['href'])
    board_idxno6.append(i.a.attrs['href'].split('srno=')[1])
    #title6 = i.find('li')
    #title6 = title6.get_text().strip()
    board_title6.append(i.get_text())
print('korea4h 알림소식')
print(board_url6)
print(board_idxno6)
print(board_title6)

#korea4-h 서식자료실
title7 = soup.find_all(class_='media-body')[1]
title7 = title7.find_all('li')
board_title7 = []
board_url7 = []
board_idxno7 = []

for i in title7:
    board_url7.append(i.a.attrs['href'])
    board_idxno7.append(i.a.attrs['href'].split('srno=')[1])
    #title6 = i.find('li')
    #title6 = title6.get_text().strip()
    board_title7.append(i.get_text())
print('korea4h 서식자료실')
print(board_url7)
print(board_idxno7)
print(board_title7)

#korea4-h 교육자료실
title8 = soup.find_all(class_='media-body')[2]
title8 = title8.find_all('li')
board_title8 = []
board_url8 = []
board_idxno8 = []

for i in title8:
    board_url8.append(i.a.attrs['href'])
    board_idxno8.append(i.a.attrs['href'].split('srno=')[1])
    #title6 = i.find('li')
    #title6 = title6.get_text().strip()
    board_title8.append(i.get_text())
print('korea4h 교육자료실')
print(board_url8)
print(board_idxno8)
print(board_title8)

#korea4-h 교육자료실
title10 = soup.find_all(class_='bannerBox')[2]
title10 = title10.find_all('div')
#board_title10 = []
board_url10 = []
board_img10 = []

for i in title10:
    board_url10.append(i.a.attrs['href'])
    board_img10.append(i.img.attrs['src'])

print('korea4h 배너')
print(board_url10)
print(board_img10)


###
cafeurl = 'https://cafe.naver.com/4hplayground?iframe_url=/MyCafeIntro.nhn%3Fclubid=30077118'
driver.get(cafeurl)

driver.switch_to.frame('cafe_main')
cafehtml = requests.get(cafeurl).text
soup = BeautifulSoup(driver.page_source,"html.parser")
#soup = soup.find_all(class_ = 'td_article')
#title = soup.find_all(class_ = 'td_article')
title = soup.find_all(class_ = 'td_article')

board_title3 = []
board_url3 = []
board_idxno3 = []


for i in title:
    board_url3.append(i.a.attrs['href'])
    board_title3.append(i.a.attrs['title'])
    board_idxno3.append(i.a.attrs['href'].split('articleid=')[1].split('&')[0])
print('4hcafe 전체게시물')
print(board_url3)
print(board_title3)
print(board_idxno3)

album = soup.find_all(class_ = 'album-box')[0]
li = album.find_all('li')

board_img4 = []
board_title4 = []
board_name4 = []
board_date4 = []
board_url4 = []
board_idxno4 = []
board_img4 = []
imgname4 = []
for i in li:
    photo4 = i.find(class_='photo' )
    photo4 = photo4.a.attrs['href']
    board_url4.append(photo4)

    tit4 = i.find(class_ = 'tit')
    tit4 = tit4.get_text().strip()
    board_title4.append(tit4)

    pnick4 = i.find(class_ = 'p-nick')
    pnick4 = pnick4.get_text().strip()
    board_name4.append(pnick4)

    date4 = i.find(class_ = 'date')
    date4 = date4.get_text().strip()
    board_date4.append(date4)

    board_idxno4.append(i.a.attrs['href'].split('articleid=')[1].split('&')[0])

    board_img4.append(i.img.attrs['src'])
    imgname4.append(i.img.attrs['src'].split('/')[4])#.split('/')[3])

print('4hcafe 메이커프로젝트')
print(board_img4)
print(board_url4)
print(board_title4)
print(board_name4)
print(board_date4)
print(board_idxno4)
print(imgname4)

album = soup.find_all(class_ = 'album-box')[1]
li = album.find_all('li')

board_img9 = []
board_title9 = []
board_name9 = []
board_date9 = []
board_url9 = []
board_idxno9 = []
board_img9 = []
imgname9 = []

for i in li:
    photo9 = i.find(class_='photo' )
    photo9 = photo9.a.attrs['href']
    board_url9.append(photo9)

    tit9 = i.find(class_ = 'tit')
    tit9 = tit9.get_text().strip()
    board_title9.append(tit9)

    pnick9 = i.find(class_ = 'p-nick')
    pnick9 = pnick9.get_text().strip()
    board_name9.append(pnick9)

    date9 = i.find(class_ = 'date')
    date9 = date9.get_text().strip()
    board_date9.append(date9)

    board_idxno9.append(i.a.attrs['href'].split('articleid=')[1].split('&')[0])

    board_img9.append(i.img.attrs['src'])
    imgname9.append(i.img.attrs['src'].split('/')[4])#.split('/')[3])

print('4hcafe 중고등 활동보고')
print(board_img9)
print(board_url9)
print(board_title9)
print(board_name9)
print(board_date9)
print(board_idxno9)
print(imgname9)

#dburl = "http://localhost/api/BoardAction.php"
dburl = "http://54.180.54.186/api/BoardAction.php"
n = 3;
for i in range(4):
    #board_num 1 농정
    payload1 = {'board_num':'1','board_title': board_title1[n],'board_subtitle': board_subtitle1[n], 'board_url': board_url1[n], 'board_img':board_img1[n],'board_idxno':board_idxno1[n]}
    r = requests.post(dburl, params=payload1)
    n = n - 1
    if r.status_code == 404:
        error_email()

m = 5;

for i in range(6):
    #board_num 2 청년농부
    payload2 = {'board_num':'2', 'board_title': board_title2[m],'board_subheading': board_subheading2[m], 'board_url': board_url2[m], 'board_img':board_img2[m],'board_idxno':board_idxno2[m]}
    r = requests.post(dburl, params=payload2)
    m= m - 1
    if r.status_code == 404:
        error_email()

ii = 5;

for i in range(6):
    #board_num 5 4h-소식
    payload2 = {'board_num':'5', 'board_title': board_title5[ii],'board_name': board_name5[ii], 'board_url': board_url5[ii], 'board_img':board_img5[ii],'board_idxno':board_idxno5[ii]}
    r = requests.post(dburl, params=payload2)
    ii = ii - 1
    if r.status_code == 404:
        error_email()


mm = 5;
for i in range(6):
    #board_num 4 cafe 메이커
    payload2 = {'board_num':'4', 'board_title': board_title4[mm], 'board_url': board_url4[mm], 'board_date': board_date4[mm],'board_img': board_img4[mm], 'board_name': board_name4[mm], 'board_idxno' : board_idxno4[mm], 'imgname' : imgname4[mm]}
    r = requests.post(dburl, params=payload2)
    filename = imgname4[mm]
    image_url = board_img4[mm]
    path = "C:/Bitnami/wampstack-7.1.27-0/apache2/htdocs/suho/attach/playground/"
    urllib.request.urlretrieve(image_url, path+filename)
    mm = mm - 1

mm = 5;
for i in range(6):
    #board_num 9 중고등활동보고
    payload2 = {'board_num':'9', 'board_title': board_title9[mm], 'board_url': board_url9[mm], 'board_date': board_date9[mm],'board_img': board_img9[mm], 'board_name': board_name9[mm], 'board_idxno' : board_idxno9[mm], 'imgname' : imgname9[mm]}
    r = requests.post(dburl, params=payload2)
    filename = imgname9[mm]
    image_url = board_img9[mm]
    path = "C:/Bitnami/wampstack-7.1.27-0/apache2/htdocs/suho/attach/playground/"
    urllib.request.urlretrieve(image_url, path+filename)
    mm = mm - 1

nn = 3;
for i in range(10, 3):
    #board_num 3 cafe 전체게시글
    payload1 = {'board_num':'3','board_title': board_title3[nn], 'board_url': board_url3[nn], 'board_idxno':board_idxno3[nn]}
    r = requests.post(dburl, params=payload1)
    nn = nn - 1
    if r.status_code == 404:
        error_email()
##korea4-h 알림소식 db insert
n = 4;
for i in range(5):
    #board_num 6 알림터
    payload1 = {'board_num':'6','board_title': board_title6[n], 'board_url': board_url6[n], 'board_idxno':board_idxno6[n]}
    r = requests.post(dburl, params=payload1)
    n = n - 1
    if r.status_code == 404:
        error_email()

n = 4;
for i in range(5):
    #board_num 7 서식자료실
    payload1 = {'board_num':'7','board_title': board_title7[n], 'board_url': board_url7[n], 'board_idxno':board_idxno7[n]}
    r = requests.post(dburl, params=payload1)
    n = n - 1
    if r.status_code == 404:
        error_email()

n = 4;
for i in range(5):
    #board_num 8 교육자료실
    payload1 = {'board_num':'8','board_title': board_title8[n], 'board_url': board_url8[n], 'board_idxno':board_idxno8[n]}
    r = requests.post(dburl, params=payload1)
    n = n - 1
    if r.status_code == 404:
        error_email()

bn = 1;
for i in range(0):
    #board_num 10 배너 이미지
    payload1 = {'board_num':'10', 'board_url': board_url10[bn], 'board_img':board_img10[bn]}
    r = requests.post(dburl, params=payload1)
    bn = bn - 1
    if r.status_code == 404:
        error_email()

time.sleep(2)
print('Completed')
driver.quit()
