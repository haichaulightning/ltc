from telethon import TelegramClient,events
lxLQHFTGBiJPeIY=True
lxLQHFTGBiJPeIz=None
lxLQHFTGBiJPeIw=False
lxLQHFTGBiJPeIn=print
lxLQHFTGBiJPeIc=len
lxLQHFTGBiJPeIV=bytes
lxLQHFTGBiJPeIA=enumerate
lxLQHFTGBiJPeIq=exit
lxLQHFTGBiJPeIs=range
lxLQHFTGBiJPeIa=type
lxLQHFTGBiJPeIu=hasattr
lxLQHFTGBiJPeIM=int
lxLQHFTGBiJPeIg=KeyboardInterrupt
lxLQHFTGBiJPeIy=events.NewMessage
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest as botcallback
from colorama import Fore,init as lxLQHFTGBiJPeOI
lxLQHFTGBiJPeIS=Fore.RESET
lxLQHFTGBiJPeIb=Fore.RED
lxLQHFTGBiJPeIh=Fore.GREEN
lxLQHFTGBiJPeOI(autoreset=lxLQHFTGBiJPeIY)
from datetime import datetime
lxLQHFTGBiJPeIR=datetime.now
from bs4 import BeautifulSoup
import os
lxLQHFTGBiJPeIj=os.mkdir
lxLQHFTGBiJPeIk=os.path
lxLQHFTGBiJPeIm=os.name
lxLQHFTGBiJPeIr=os.system
import re
import time
lxLQHFTGBiJPeIN=time.sleep
import requests
lxLQHFTGBiJPeIv=requests.post
lxLQHFTGBiJPeIK=requests.exceptions
lxLQHFTGBiJPeIE=requests.request
import sys
lxLQHFTGBiJPeIp=sys.argv
lxLQHFTGBiJPeId=sys.stdout
import asyncio
lxLQHFTGBiJPeIU=asyncio.get_event_loop
lxLQHFTGBiJPeOy=lxLQHFTGBiJPeIU()
import logging
lxLQHFTGBiJPeID=logging.ERROR
lxLQHFTGBiJPeIf=logging.basicConfig
lxLQHFTGBiJPeIf(level=lxLQHFTGBiJPeID)
lxLQHFTGBiJPeOb=64179
lxLQHFTGBiJPeOS="dd60bb74bb03d8aa368aa37ec7b35d42"
lxLQHFTGBiJPeOR={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
lxLQHFTGBiJPeIr('cls' if lxLQHFTGBiJPeIm=='nt' else 'clear')
try:
 def lxLQHFTGBiJPeOs(phone_number=lxLQHFTGBiJPeIz):
  return TelegramClient("session/"+phone_number,lxLQHFTGBiJPeOb,lxLQHFTGBiJPeOS)
 def lxLQHFTGBiJPeOa(lxLQHFTGBiJPeOr,addnewline=lxLQHFTGBiJPeIw):
  if addnewline is lxLQHFTGBiJPeIw:
   lxLQHFTGBiJPeIn("[%s] %s"%(lxLQHFTGBiJPeIR().strftime("%H:%M:%S"),lxLQHFTGBiJPeOr))
  else:
   lxLQHFTGBiJPeIn("[%s] %s"%(lxLQHFTGBiJPeIR().strftime("%H:%M:%S"),lxLQHFTGBiJPeOr),end='\n\n')
 def lxLQHFTGBiJPeOu(byt):
  lxLQHFTGBiJPeOk=b'210400'
  lxLQHFTGBiJPeOj=lxLQHFTGBiJPeIc(lxLQHFTGBiJPeOk)
  return lxLQHFTGBiJPeIV(c^lxLQHFTGBiJPeOk[i%lxLQHFTGBiJPeOj]for i,c in lxLQHFTGBiJPeIA(byt))
 def lxLQHFTGBiJPeOM(lxLQHFTGBiJPeOU,method='GET',data=lxLQHFTGBiJPeIz):
  try:
   lxLQHFTGBiJPeON=lxLQHFTGBiJPeIE(method,lxLQHFTGBiJPeOU,data=data,headers=lxLQHFTGBiJPeOR,timeout=15,allow_redirects=lxLQHFTGBiJPeIw)
   lxLQHFTGBiJPeOE=lxLQHFTGBiJPeON.status_code
   lxLQHFTGBiJPeOK=lxLQHFTGBiJPeON.text
   return[lxLQHFTGBiJPeOE,lxLQHFTGBiJPeOK]
  except lxLQHFTGBiJPeIK.Timeout:
   lxLQHFTGBiJPeOa('Connection Timeout, Please check your internet connection')
   lxLQHFTGBiJPeIq(1)
  except lxLQHFTGBiJPeIK.ConnectionError:
   lxLQHFTGBiJPeOa('Connection Error, Please check your internet connection')
   lxLQHFTGBiJPeIq(1)
 def lxLQHFTGBiJPeOg(i):
  for x in lxLQHFTGBiJPeIs(0,i+1):
   lxLQHFTGBiJPeId.write('[%s] Waiting %s seconds! %d\r'%(lxLQHFTGBiJPeIR().strftime("%H:%M:%S"),i,x))
   lxLQHFTGBiJPeIN(1)
 def lxLQHFTGBiJPeOW(markup):
  lxLQHFTGBiJPeOv=markup.rows[0].buttons[0]
  if lxLQHFTGBiJPeIa(lxLQHFTGBiJPeOv)is KeyboardButtonUrl:
   return lxLQHFTGBiJPeOv.url
  else:
   return lxLQHFTGBiJPeIz
 def lxLQHFTGBiJPeOX():
  lxLQHFTGBiJPeIn("------------------------------")
  lxLQHFTGBiJPeIn("LTCClick Script v4.4\n")
  lxLQHFTGBiJPeIn("Telegram: https://t.me/netiranz")
  lxLQHFTGBiJPeIn("Groups: https://t.me/bot_scripter")
  lxLQHFTGBiJPeIn("Facebook: https://fb.me/rafinetiz")
  lxLQHFTGBiJPeIn("")
  lxLQHFTGBiJPeIn("Join group for more info about\nnew update or requesting other script")
  lxLQHFTGBiJPeIn(lxLQHFTGBiJPeIh+"Created by rafinetiz\033[0m")
  lxLQHFTGBiJPeIn("------------------------------")
 async def lxLQHFTGBiJPeOC():
  if not lxLQHFTGBiJPeIk.exists("session"):
   lxLQHFTGBiJPeIj("session")
  lxLQHFTGBiJPeOX()
  if lxLQHFTGBiJPeIc(lxLQHFTGBiJPeIp)<2:
   lxLQHFTGBiJPeIn("Usage: python main.py phone_number",end="\n\n")
   lxLQHFTGBiJPeIn("phone_number must be write in internasional format (example: +6283174705555)")
   lxLQHFTGBiJPeIq(1)
  lxLQHFTGBiJPeIn("Press CTRL+C / Volume Down + C to stop",end="\n\n")
  lxLQHFTGBiJPeOd=lxLQHFTGBiJPeOs(lxLQHFTGBiJPeIp[1])
  await lxLQHFTGBiJPeOd.start(lxLQHFTGBiJPeIp[1])
  me=await lxLQHFTGBiJPeOd.get_me()
  lxLQHFTGBiJPeIn('Current account: %s%s\n'%("" if me.first_name is lxLQHFTGBiJPeIz else me.first_name,"" if me.username is lxLQHFTGBiJPeIz else "("+me.username+")"))
  lxLQHFTGBiJPeOa('Sending first command')
  await lxLQHFTGBiJPeOd.send_message('LTCClickBot','/visit')
  async def lxLQHFTGBiJPeOt(event):
   lxLQHFTGBiJPeOp=event.original_update
   if lxLQHFTGBiJPeIa(lxLQHFTGBiJPeOp)is not UpdateShortMessage:
    if lxLQHFTGBiJPeIu(lxLQHFTGBiJPeOp.message,'reply_markup')and lxLQHFTGBiJPeIa(lxLQHFTGBiJPeOp.message.reply_markup)is ReplyInlineMarkup:
     lxLQHFTGBiJPeOU=lxLQHFTGBiJPeOW(lxLQHFTGBiJPeOp.message.reply_markup)
     if lxLQHFTGBiJPeOU is not lxLQHFTGBiJPeIz:
      lxLQHFTGBiJPeOa('Requesting reward')
      lxLQHFTGBiJPeOf=20
      lxLQHFTGBiJPeOD=0
      while lxLQHFTGBiJPeIY:
       (lxLQHFTGBiJPeOE,lxLQHFTGBiJPeOK)=lxLQHFTGBiJPeOM(lxLQHFTGBiJPeOU)
       lxLQHFTGBiJPeOY=BeautifulSoup(lxLQHFTGBiJPeOK,'html.parser')
       cc=lxLQHFTGBiJPeOY.find('div',{'class':'g-recaptcha'})
       tt=lxLQHFTGBiJPeOY.find('div',{'id':'headbar'})
       if lxLQHFTGBiJPeOE==302:
        lxLQHFTGBiJPeId.write('[%s] STATUS: %s (%d)\r'%(lxLQHFTGBiJPeIR().strftime("%H:%M:%S"),'FALSE' if cc is not lxLQHFTGBiJPeIz else 'TRUE',lxLQHFTGBiJPeOD))
        break
       elif lxLQHFTGBiJPeOE==200 and cc is lxLQHFTGBiJPeIz and tt is not lxLQHFTGBiJPeIz:
        lxLQHFTGBiJPeOz=tt.get('data-code')
        lxLQHFTGBiJPeOw=tt.get('data-timer')
        lxLQHFTGBiJPeOn=tt.get('data-token')
        lxLQHFTGBiJPeOg(lxLQHFTGBiJPeIM(lxLQHFTGBiJPeOw))
        lxLQHFTGBiJPeIv('http://ltc.dogeclick.com/reward',data={'code':lxLQHFTGBiJPeOz,'token':lxLQHFTGBiJPeOn},headers=lxLQHFTGBiJPeOR,allow_redirects=lxLQHFTGBiJPeIw)
        break
       elif lxLQHFTGBiJPeOE==200 and cc is not lxLQHFTGBiJPeIz:
        lxLQHFTGBiJPeId.write('[%s] STATUS: %s (%d)\r'%(lxLQHFTGBiJPeIR().strftime("%H:%M:%S"),'FALSE' if cc is not lxLQHFTGBiJPeIz else 'TRUE',lxLQHFTGBiJPeOD))
       if lxLQHFTGBiJPeOf==lxLQHFTGBiJPeOD:
        lxLQHFTGBiJPeOa('Skipping ads, because max retry is reached',lxLQHFTGBiJPeIY)
        lxLQHFTGBiJPeOz=lxLQHFTGBiJPeOU[-7:]
        lxLQHFTGBiJPeOV='{"method":"skip_click","id":"%s"}'%lxLQHFTGBiJPeOz
        lxLQHFTGBiJPeOA=botcallback('LTCClickBot',lxLQHFTGBiJPeOp.message.id,data=lxLQHFTGBiJPeOV.encode())
        await lxLQHFTGBiJPeOd(lxLQHFTGBiJPeOA)
        break
       lxLQHFTGBiJPeOD+=1
       lxLQHFTGBiJPeIN(3)
  lxLQHFTGBiJPeOd.add_event_handler(lxLQHFTGBiJPeOt,lxLQHFTGBiJPeIy(incoming=lxLQHFTGBiJPeIY,chats="LTCClickBot"))
  async def lxLQHFTGBiJPeIO(event):
   lxLQHFTGBiJPeOa(lxLQHFTGBiJPeIb+"Ads not available detected"+lxLQHFTGBiJPeIS)
   lxLQHFTGBiJPeOa("Disconnecting")
   await lxLQHFTGBiJPeOd.disconnect()
  lxLQHFTGBiJPeOd.add_event_handler(lxLQHFTGBiJPeIO,lxLQHFTGBiJPeIy(incoming=lxLQHFTGBiJPeIY,chats="LTCClickBot",pattern='Sorry, there are no new ads available.'))
  async def lxLQHFTGBiJPeIo(event):
   if lxLQHFTGBiJPeIa(event.original_update):
    lxLQHFTGBiJPeOa(lxLQHFTGBiJPeIh+event.raw_text+"\n")
  lxLQHFTGBiJPeOd.add_event_handler(lxLQHFTGBiJPeIo,lxLQHFTGBiJPeIy(incoming=lxLQHFTGBiJPeIY,chats="LTCClickBot",pattern='You earned'))
  await lxLQHFTGBiJPeOd.run_until_disconnected()
 lxLQHFTGBiJPeOy.run_until_complete(lxLQHFTGBiJPeOC())
except lxLQHFTGBiJPeIg:
 lxLQHFTGBiJPeIr('cls' if lxLQHFTGBiJPeIm=='nt' else 'clear')