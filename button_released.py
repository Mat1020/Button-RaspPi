from gpiozero import Button, LED
from signal import pause

button = Button(2)
led = LED(17)

button.when_pressed = led.on
button.when_released = led.off

pause()
