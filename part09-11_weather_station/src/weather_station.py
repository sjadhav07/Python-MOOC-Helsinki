# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, station_name:str):
        self.__station_name = station_name
        self.__lst = []
    def add_observation(self, observation: str):
        self.__lst.append(observation)
    def latest_observation(self):
        if len(self.__lst) < 1:
            return ""
        else:
            return self.__lst[-1]
    def number_of_observations(self):
        return len(self.__lst)
    def __str__(self):
        return f"{self.__station_name}, {len(self.__lst)} observations"
