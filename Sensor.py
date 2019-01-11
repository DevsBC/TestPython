class Sensor:

    def __init__(self, temperature, humidity):
        self.__temperature = self.set_temperature(temperature)
        self.__humidity = self.set_humidity(humidity)

    def set_temperature(self, temperature):
        self.__temperature = temperature
        return self.__temperature

    def set_humidity(self, humidity):
        self.__humidity = humidity
        return self.__humidity

    def show_data(self):
        print("\nLa temperatura es: ", self.__temperature,
              "\nLa humedad es: ", self.__humidity)

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

