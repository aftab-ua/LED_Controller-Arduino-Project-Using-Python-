import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA
from time import strftime, time
import time
comport='COM3'

board=pyfirmata.Arduino(comport)

data=" " + "Digital Clock"



while True:
    string=strftime('%H:%M:%S %p')
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))
    time.sleep(1)