#обработка csv файла


import csv
from os.path import splitext


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_whl = [float(x) for x in body_whl.split('x')]
            if len(self.body_whl) == 3:
                self.body_length = self.body_whl[0]
                self.body_width = self.body_whl[1]
                self.body_height = self.body_whl[2]
            else:
                self.body_whl = float(0)
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)

        except ValueError:
            self.body_whl = float(0)
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        if isinstance(self.body_whl, list) and len(self.body_whl) == 3:
            return float(self.body_length * self.body_width * self.body_height)
        else:
            return float(0)


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def NotNone(*args):
    if '' in args:
        return False
    else:
        return True


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_photo(str):
    if str.isdigit() is False and str.count('.') == 1 and str[-1] != '.' and str[0] != '.':
        return True
    else:
        return False


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for line in reader:
            if not line:
                continue
            elif line[0] == 'car' and NotNone(line[1], line[2], line[3], line[5]) and is_float(line[5]) and is_photo(
                    line[3]):
                car_list.append(Car(line[1], line[3], line[5], line[2]))
            elif line[0] == 'truck' and NotNone(line[1], line[3], line[5]) and is_float(line[5]) and is_photo(
                    line[3]):
                car_list.append(Truck(line[1], line[3], line[5], line[4]))
            elif line[0] == 'spec_machine' and NotNone(line[1], line[3], line[5], line[6]) and is_float(
                    line[5]) and is_photo(line[3]):
                car_list.append(SpecMachine(line[1], line[3], line[5], line[6]))
    return car_list
