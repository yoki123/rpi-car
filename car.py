import RPi.GPIO as gpio


class Wheel(object):
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2

        gpio.setup(pin1, gpio.OUT)
        gpio.setup(pin2, gpio.OUT)

        gpio.output(pin3, True)
        gpio.output(pin4, True)

    def forward(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)

    def backward(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)

    def stop(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)

    def forward_slow(self):
        pass

    def backward_slow(self):
        pass


class Car(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)

        self.left_wheel = Wheel(16, 18, 22, 29)
        self.right_wheel = Wheel(13, 15, 7, 11)

    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()

    def backward(self):
        self.left_wheel.backward()
        self.right_wheel.backward()

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()

    def right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()

    def stop(self):
        self.left_wheel.stop()
        self.left_wheel.stop()

    def shutdown(self):
        self.stop()
        gpio.cleanup()
