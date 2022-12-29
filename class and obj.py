class car:
    def sample_car_instance_method(self,a):
        print(a)
carobj=car()
carobj.sample_car_instance_method("hello again!")

carobj2=car()
carobj.sample_car_instance_method(2)


class CarClassMethod():
    attributeis_engine_started=True
    attributeis_engine_stopped=False
    @classmethod
    def sampleCar_Class_Method(car):
        car.attributeis_engine_started="ON"
        car.attributeis_engine_stopped="OFF"
        CarClassMethod.sampleCar_Class_Method()
        print(CarClassMethod.attributeis_engine_started)
        print(CarClassMethod.attributeis_engine_stopped)


class car():
    def attributeis_engine_started(self,true):
        print(true)
    def attributeis_engine_stopped(self,false):
        print(false)
carobj=car()
carobj.attributeis_engine_started("ON")
carobj.attributeis_engine_stopped("OFF")

def acceleration(self):
    #     self.accelaration()
    #     if not self.is_engine_started:
    #         print("car is not started yet")
    #     else:
    #         self.current_speed += self.accelaration
    #         if self.current_speed > self.max_speed
    #             self.current_speed = self.max_speed

    class car():
        def __init__(self, color, max_speed, tyre_friction, current_speed):
            self.color = color
            self.max_speed = max_speed
            self.tyre_friction = tyre_friction
            self.current_speed = current_speed

        def start_engine(self):
            self.is_engine_started = True

        def stop_engine(self):
            self.is_engine_stopped = False

        def apply_breaks(self):
            if self.current_speed >= self.tyre_friction:
                self.current_speed = self.current_speed - self.tyre_friction
            else:
                self.current_speed = 0
            print(self.current_speed)

        def sound_horn(self):
            if self.is_engine_started == True:
                print("beep beep")
            else:
                print("car not started")

    carobj = car("black", "67", 70, 80)
    carobj.start_engine()
    carobj.sound_horn()
    carobj.apply_breaks()
    carobj.apply_breaks()
    carobj.stop_engine()
    carobj.sound_horn()

