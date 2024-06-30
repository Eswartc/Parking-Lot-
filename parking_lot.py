class slot:
    def __init__(self, number):
        
        self.number = number
        self.car = 'Empty'

    def __str__(self):
        return f"Slot {self.number}: {'Empty' if self.car == 'Empty' else 'Occupied'}"

    def park(self, car):
        self.car = car

    def remove(self):
        self.car = 'Empty'

    def isempty(self):
        return self.car == 'Empty'
        
class lane:
    def __init__(self, number, no_slots):
        
        self.number = number
        self.no_slots = no_slots
        self.slots = [slot(i) for i in range(self.no_slots)]

    def __str__(self):
        slot_status = []
        for slot in self.slots:
            slot_status.append((slot.number, slot.car))
        return f"Lane: {self.number}: {', '.join([f'Slot: {x} - {y}' for x, y in slot_status])}"

    def isempty(self, car):
        try:
            return all(self.slots[i].car == 'Empty' for i in range(car.size))
        except:
            print('Space in not enough for', car.plate)
            return False

    def park_car(self, car):
        if self.isempty(car):
            for i in range(car.size):
                self.slots[i].car = car.plate
            return True
        return False

    def remove_car(self, car):
        for i in range(car.size):
            self.slots[i].car = 'Empty'
        return True

class level:
    def __init__(self, number, no_lanes, no_slots):
        
        self.number = number
        self.no_lanes = no_lanes
        self.no_slots = no_slots
        self.lanes = [lane(i, self.no_slots) for i in range(self.no_lanes)]

    def __str__(self):
        lane_status = []
        for lane in self.lanes:
            for slot in lane.slots:
                lane_status.append("Level: {0} Lane: {1} Slot: {2} - {3}".format(self.number, lane.number, slot.number, slot.car))
        return '\n'.join(lane_status)

    def park_car(self, car):
        for lane in self.lanes:
            if lane.park_car(car):
                print('Car:', car.plate, 'parked')
                return True
        return False

    def remove_car(self, car):
        for lane in self.lanes:
            for slots in lane.slots:
                if slots.car == car.plate:
                    lane.remove_car(car)
                    print('Car:', car.plate, 'removed')
                    return True
        return False

class Parking_Lot:
    def __init__(self, no_levels, no_lanes, no_slots):
        self.no_levels = no_levels
        self.no_lanes = no_lanes
        self.no_slots = no_slots
        self.levels = [level(i, self.no_lanes, self.no_slots) for i in range(self.no_levels)]

    def park_car(self, car):
        for level in self.levels:
            if level.park_car(car):
                return True
        return False

    def remove_car(self, car):
        for level in self.levels:
            if level.remove_car(car):
                return True
        print('Car:', car.plate, 'not found')
        return False

    def __str__(self):
        lane_status = []
        for level in self.levels:
            for lane in level.lanes:
                for slot in lane.slots:
                    lane_status.append("Level: {0} Lane: {1} Slot: {2} - {3}".format(level.number, lane.number, slot.number, slot.car))
                lane_status.append('\n')
        return '\n'.join(lane_status)

class Car:
    def __init__(self, plate, size = 1):
        self.plate = plate
        self.size = size