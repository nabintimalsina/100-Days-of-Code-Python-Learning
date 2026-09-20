class Car:
    def _init_(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brk = False
        self.clutch = False 
        print("Car is started")
car1 = Car()
car1.start()