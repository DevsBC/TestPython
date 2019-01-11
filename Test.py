from Sensor import Sensor
import random


def random_temperature():
    return random.randint(0, 100)


def random_humidity():
    return random.randint(0, 100)


class Test:
    list_sensor = []
    count = 0

    for i in range(1, 16):
        exec("sensor{} = Sensor(random_temperature(), random_humidity())".format(i))
        exec("list_sensor.append(sensor{})".format(i))

    for sensor in list_sensor:
        if sensor is not None:
            count += 1
            print("\nSensor #", count)
            print(sensor.show_data())
            if sensor.get_temperature() > 50:
                print("\nALERTA\nSensor #", count, "Excedio limite")
                break
