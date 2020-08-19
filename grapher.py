import requests
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
from time import sleep
import matplotlib.pyplot as plt
import datetime
import random

plt.ion()
plt.xlabel('Time')
plt.ylabel('Signal Strength (dB)')
plt.ylim(20,90)
plt.xlim(0,100)
i = 0
while 1:
    r = requests.get('http://192.168.0.1/wlanAccess.asp')
    soup = BeautifulSoup(r.text, 'html.parser')
    signalTable = [tbl for tbl in soup.find_all('table') if not tbl.attrs][-1]

    tableBody = signalTable.find('tbody')
    rows = signalTable.find_all('tr')
    data = []
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) #to get rid of empty columns
    print(data[3][2])
    #print(AsciiTable(data).table)

    signal = abs(int(data[3][2]))
    plt.plot(i,signal, 'xb-')
    plt.draw()
    plt.pause(0.3)
    sleep(0.3)
    i += 1

plt.show(block=True) # block=True lets the window stay open at the end of the animation.
