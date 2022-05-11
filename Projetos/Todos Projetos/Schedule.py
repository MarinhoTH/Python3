import schedule
import time
import pyautogui as x
from time import sleep

def job():
    x.click(-559,716) # clicar no video
    sleep(1)
    x.click(-180,809) # ir pro final do video
    sleep(2)
    x.press('right')

    sleep(6)
    x.click(-404,129) # concluido
    


'''schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)

schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("07:44").do(job)'''
schedule.every(15).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)