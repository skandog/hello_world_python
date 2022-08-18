class Car:
    speed = 0
    start = False

    def start(self):
        self.started = True
        print("Car started, lets roll!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("vroom vroom")
        else:
            print("you should probs start the car first")

    def stop(self):
        self.speed = 0
        print("screeech")
