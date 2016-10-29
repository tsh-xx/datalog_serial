from microbit import *

volts = 0
last = 0
display.clear()
timer = 0
tick = 0
# Just checking the UART baud rate
uart.init(9600)


def print_value(volts):
    time = running_time()/1000
    uart.write('{:02.0f}:{:02.0f}:{:04.1f}, {}\n'
               .format(int(time/3600), time/60 % 60, time % 60, volts))


def get_samples():
    global last
    global volts
    global timer
    global tick
# Get the voltage and disply 2 dots representing the voltage in 25 bins
    volts = pin0.read_analog()
    display.clear()
    display.set_pixel(2, int(volts/205), 9)
    display.set_pixel(3, int((volts % 205)/42), 9)
# If change in reported value is small, ignore it for a while
    if((last - volts < 10) and (last >= volts)):
        timer = timer + 1
        if (timer % 1000):
            display.set_pixel(0, 0, tick)
            if(tick == 9):
                tick = 0
            else:
                tick = 9
        if (timer > 10000):
            timer = 0
            print_value(volts)
            last = volts
    else:
        print_value(volts)
        last = volts
        timer = 0
# Control the maximum sample rate
    sleep(30)


while True:
    get_samples()
