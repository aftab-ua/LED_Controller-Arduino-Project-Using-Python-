import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA
from time import strftime, time
import time

comport='COM3'

board=pyfirmata.Arduino(comport)

bule=board.get_pin('d:13:o')
yellow=board.get_pin('d:12:o')
green=board.get_pin('d:11:o')
red=board.get_pin('d:10:o')
white=board.get_pin('d:9:o')

lightOn= " " + "All led are on"
lightOff= " " + "All led are off"
blue_led = " " + "blue"
yellow_led =" " + "yellow_led"
green_led = " " + "green"
red_led = " " + "red"
white_led = " " + "white"
exit = " " + "Exit! Have Nice Day"
    

#bule=board.get_pin('d:13:o')
#yellow=board.get_pin('d:12:o')
#green=board.get_pin('d:11:o')
#red=board.get_pin('d:10:o')
#white=board.get_pin('d:9:o')

def led(val):
    if val=='b':
        bule.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(blue_led))
    elif val=='y':
        yellow.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(yellow_led))
        
    elif val=='g':
        green.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(green_led))
        
    elif val=='r':
        red.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(red_led))
        
    elif val=='w':
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(white_led))

        white.write(1)
    elif val=='e':

        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(exit))
    
    elif val=='a':
        bule.write(1)
        yellow.write(1)
        green.write(1)
        red.write(1)
        white.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(lightOn))
    elif val==0:
        bule.write(0)
        yellow.write(0)
        green.write(0)
        red.write(0)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(lightOff))


def led_number(total):
    if total==0:
        bule.write(0)
        yellow.write(0)
        green.write(0)
        red.write(0)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(lightOff))
    elif total==1:
        bule.write(1)
        yellow.write(0)
        green.write(0)
        red.write(0)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(blue_led))
    elif total==2:
        bule.write(1)
        yellow.write(1)
        green.write(0)
        red.write(0)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(blue_led))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(yellow_led))
    elif total==3:
        bule.write(1)
        yellow.write(1)
        green.write(1)
        red.write(0)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(blue_led))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(yellow_led))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(green_led))
    elif total==4:
        bule.write(1)
        yellow.write(1)
        green.write(1)
        red.write(1)
        white.write(0)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(blue_led))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(red_led ))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(yellow_led))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(green_led))
    elif total==5:
        bule.write(1)
        yellow.write(1)
        green.write(1)
        red.write(1)
        white.write(1)
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(lightOn))
        

