import RPi.GPIO as gpio
import config as c


class Wheel(object):
    def __init__(self, in_pin1, in_pin2, enable_pin1, enable_pin2):
        '''
        :param in_pin1 in_pin2: IN1 IN2 or IN3 IN4
        :param enable_pin1 enable_pin2: ENA or ENB
        '''
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        # setup I/O OUT
        gpio.setup(in_pin1, gpio.OUT)
        gpio.setup(in_pin2, gpio.OUT)
        gpio.setup(enable_pin1, gpio.OUT)
        gpio.setup(enable_pin2, gpio.OUT)

        # enable
        gpio.output(enable_pin1, True)
        gpio.output(enable_pin2, True)

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

        self.left_wheel = Wheel(c.PIN_IO_IN1, c.PIN_IO_IN2, c.PIN_ENABLE_A1, c.PIN_ENABLE_A2)
        self.right_wheel = Wheel(c.PIN_IO_IN3, c.PIN_IO_IN4, c.PIN_ENABLE_B1, c.PIN_ENABLE_B2)

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
        self.right_wheel.stop()

    def shutdown(self):
        self.stop()
        gpio.cleanup()
