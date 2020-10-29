import time
from plyer import notification
import os
import sys


file1=open(os.getcwd() + "/spanish_vocab_1000.txt","r",encoding="utf-8")
lines=file1.readlines()
log=open(os.getcwd() + "/log_last.txt")
log_last=log.read()
i=int(log_last)
for j in range(i,len(lines)):
    line=lines[j]
    logchange=open(os.getcwd() + "/log_last.txt","w")
    logchange.write(str(j))
    number=str(j)
    words=line.split()
    words.pop(0)
    spnwrd=words[0]
    engwrd=words[1]
    strprnt=number+"\nSpanish : "+spnwrd+"\nEnglish : "+engwrd
    time.sleep(900)
    notification.notify(title="Spanish vocabulary" , message=strprnt, timeout=8, app_icon=os.getcwd() + "/spain_icon.ico")
