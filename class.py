class vehicle:
    def car(self):
        print('car')
        
class car_v(vehicle):
    def brake_system(self):
        print('brake system')
        

c= car_v()
c.brake_system()