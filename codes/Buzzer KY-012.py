#Buzzer KY-012
#Benitez Solorzano Paola


```python
from machine import Pin, PWM
from utime import sleep

ky012 = PWM(Pin(0))
ky012.freq(500)
ky012.duty_u16(1000)
sleep(1)
ky012.duty_u16(0)
```




