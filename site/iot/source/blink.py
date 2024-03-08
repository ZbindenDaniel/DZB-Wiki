from machine import Pin, Timer

class ledControl:
    def __init__(self):
        self.led = Pin("LED", Pin.OUT)
        self.LED_state = True
        self.tim = Timer()
        self.freq = 1
    def tick(self,timer):
        self.LED_state = not self.LED_state
        self.led.value(self.LED_state)
    
    def start(self, freq=1):
        self.tim.init(freq=freq, mode=Timer.PERIODIC, callback=self.tick)