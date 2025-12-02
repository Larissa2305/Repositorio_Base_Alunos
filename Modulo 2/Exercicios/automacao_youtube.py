import pyautogui as pg
from time import sleep
#pg.mouseInfo()

pg.press('win')
pg.write('Chrome')
pg.press('enter')
pg.write('www.youtube.com.br')
pg.press('enter')
sleep(2)
pg.moveTo(715,100, duration=2)
pg.click()
pg.write('rihanna')
pg.press('enter')