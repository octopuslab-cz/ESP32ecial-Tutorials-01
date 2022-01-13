from time import sleep
from utils.octopus import disp7_init
from components.analog import Analog
from components.buzzer import Buzzer
from components.buzzer.melody import jingle1


photosensor = Analog(36)
piezzo = Buzzer(27)
light_level = photosensor.get_adc_aver()
disp7 = disp7_init()


LIGHT_THRESHOLD = 900
DELAY = 1 #pouse time in seconds
print("test") #testing the display function
piezzo.play_melody(jingle1) #testing the piezzo melody


while True: 
    light_level = photosensor.get_adc_aver()
    print(light_level)
    disp7.show(light_level) #showing the light level number
    if light_level > LIGHT_THRESHOLD:
        piezzo.play_melody(jingle1) #alarm will start ringing when the ESP is exposed to light
    sleep(DELAY)
