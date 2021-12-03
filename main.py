from time import sleep
from components.analog import Analog
from components.buzzer import Buzzer
from components.buzzer.melody import jingle1


photosensor = Analog(36)
piezzo = Buzzer(33)
light_level = photosensor.get_adc_aver()

LIGHT_THRESHOLD = 900
DELAY = 1 #pouse time in seconds


while True: 
    light_level = photosensor.get_adc_aver()
    print(light_level)
    if light_level > LIGHT_THRESHOLD:
        piezzo.play_melody(jingle1)
    sleep(DELAY)