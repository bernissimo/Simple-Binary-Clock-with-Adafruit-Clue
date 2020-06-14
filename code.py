from adafruit_clue import clue
import rtc
import time

r = rtc.RTC()
#                              year, mon, date, hour, min, sec, wday, yday, isdst
r.datetime = time.struct_time((2020, 6,   14,   10,   19,  00,  0,    -1,   -1)) # set time

screen = clue.simple_text_display(text_scale=2, colors=(clue.WHITE,))
screen[0].color = clue.BLUE
screen[1].color = clue.BLUE
screen[3].color = clue.GREEN
screen[4].color = clue.GREEN
screen[6].color = clue.RED
screen[7].color = clue.RED

binaer = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001"]

while True:
    current_time = r.datetime
    std = current_time.tm_hour
    minu = current_time.tm_min
    seku = current_time.tm_sec
    std0 = int(std/10)
    minu0 = int(minu/10)
    seku0 = int(seku/10)
    std1 = (std - (std0*10))
    minu1 = (minu - (minu0*10))
    seku1 = (seku - (seku0*10))
    screen[0].text = binaer[std0]
    screen[1].text = binaer[std1]
    screen[3].text = binaer[minu0]
    screen[4].text = binaer[minu1]
    screen[6].text = binaer[seku0]
    screen[7].text = binaer[seku1]
    screen.show()
    time.sleep(1)
