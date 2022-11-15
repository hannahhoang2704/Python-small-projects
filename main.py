#Exercise 10
#Part 1: Elevator: choose the floor in elevator

class Elevator:
    def __init__(self, bottom: int,top: int):
        self.bottom = bottom
        self.top = top
        self.current_floor = self.bottom


    def call(self):
        return print(self.current_floor)

    def floor_up(self, floor_nr: int):
        if floor_nr <= self.top:
            for i in range(self.current_floor,floor_nr):
                self.current_floor += 1
                print(f"You're in floor {self.current_floor}")
        else:
            print("Can't go above this floor")

    def floor_down(self, floor_nr: int):
        if floor_nr >= self.bottom:
            for i in range(floor_nr, self.current_floor):
                self.current_floor -= 1
                print(f"You're in floor {self.current_floor}")
        else:
            print("Can't go below this floor")

    def go_to_floor(self, floor_number: int):

        if floor_number > self.current_floor:
            self.floor_up(floor_number)
        elif floor_number < self.current_floor:
            self.floor_down(floor_number)
        else:
            print(f"You are in {floor_number}")



kone = Elevator(1, 15)
kone.go_to_floor(5)
kone.call()
kone.go_to_floor(4)


#Part 2: building class with many elevators

class Building:
    def __init__(self, elevators_nr: int, bottom: int, top: int):
        self.elevators_nr = elevators_nr
        self.top = top
        self.bottom = bottom
        self.elevator_list = []

    def run_elevator(self, destination_floor):
        for i in range(1, self.elevators_nr + 1):
            #new_elevator = "elevator" + str(i)
            new_elevator = Elevator(self.bottom, self.top)
            self.elevator_list.append(new_elevator)
        #print(self.elevator_list)                          #check the list of elevator
        new_elevator.go_to_floor(destination_floor)

#Part 3
    def fire_alarm(self):
        for elevator in self.elevator_list:
            elevator.go_to_floor(self.bottom)
            print(f"Current floor is {elevator.current_floor}")


building = Building(3, 1, 20)
building.run_elevator(5)
building.fire_alarm()


#Part 4: Car race
import random


class Car:
    def __init__(self, registration_nr: str, max_speed: int, current_speed=0, distance=0):
        self.registration_nr = registration_nr
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def show(self):
        print(f"{self.registration_nr}: "
              f"Maximum speed: {self.max_speed} km/h, "
              f"Current speed: {self.current_speed} km/h, "
              f"Distance: {self.distance}km")

    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, time):
        distance = time * self.current_speed
        self.distance += distance


class Race:
    def __init__(self, name, race_distance):
        self.name = name
        self.race_distance = race_distance
        self.car_list = []

    def race_finished(self):
        for car_race in self.car_list:
            if car_race.distance >= self.race_distance:
                print(f"The winner car is {car_race.registration_nr} with {car_race.distance}km")
                return True

    def hour_passes(self):
        for car_race in self.car_list:
            random_acceleration = random.randint(-10, 15)
            car_race.accelerate(random_acceleration)
            car_race.drive(1)

    def print_status(self):
        for car_race in self.car_list:
            car_race.show()


race = Race("Grand Demolition Derby", 8000)                                 #create the race

travel_max = 0
time = 0

for car in range(10):                                               #register the car in the race
    random_max_speed = random.randint(100, 200)
    new_car = Car("ABC-" + str(car + 1), random_max_speed)
    race.car_list.append(new_car)


while not race.race_finished():
    race.hour_passes()
    time += 1
    if time % 10 == 0:                              #print out current status every 10 hours
        race.print_status()
        print(f"{time} hours")
else:
    race.print_status()