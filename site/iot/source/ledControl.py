from gpiozero import LED
import machine

class RGBLed:
    def __init__(self, pinR, pinG, pinB):
        pR = machine.Pin(pinR)
        pG = machine.Pin(pinG)
        pB = machine.Pin(pinB)
        self.ledR = machine.PWM(pR, freq=1000)
        self.ledG = machine.PWM(pG, freq=1000)
        self.ledB = machine.PWM(pB, freq=1000)
        self.color = '#00FF00'
        self.tim = Timer()
    
    def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    def on(self):
        self.setColor()
        
    def off(self):
        self.ledR.duty(0)
        self.ledG.duty(0)
        self.ledB.duty(0)
        
    def setColor(self, color = self.color):
        if color[0] == '#':
            self.color = color
            rgb = hex_to_rgb(color.removeprefix('#'))
            self.ledR.duty(rgb[0])
            self.ledG.duty(rgb[1])
            self.ledB.duty(rgb[2])
