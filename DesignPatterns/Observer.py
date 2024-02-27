from abc import ABC, abstractmethod

"""
Define the interfaces
"""
class Observer(ABC):
  @abstractmethod
  def update(self, temperature, humidity, pressure):
    pass

class Subject(ABC):
  @abstractmethod
  def register_observer(self, observer):
    pass

  @abstractmethod
  def remove_observer(self, observer):
    pass

  @abstractmethod
  def notify_observers(self):
    pass

"""
Concrete Subject
"""
class WeatherStation(Subject):
  def __init__(self):
    self.observers = []
    self.temperature = 0
    self.pressure = 0
    self.humidity = 0

  def register_observer(self, observer):
    self.observers.append(observer)

  def remove_observer(self, observer):
    self.observers.remove(observer)

  def notify_observers(self):
    for observer in self.observers:
      observer.update(self.temperature, self.humidity, self.pressure)

  def measurements_changed(self):
    self.notify_observers()

  def set_measurements(self, temperature, humidity, pressure):
    self.temperature = temperature
    self.pressure = pressure
    self.humidity = humidity
    self.measurements_changed()

"""
Concrete Observers
"""
class CurrentConditionsDisplay(Observer):
  def update(self, temperature, humidity, pressure):
    print(f"Current conditions: {temperature}°C, {humidity}%, and {pressure} bar pressure.")

class StatisticsDisplay(Observer):
  def update(self, temperature, humidity, pressure):
    # Some logic
    print(f"Stats: {temperature}°C, {humidity}%, and {pressure} bar pressure.")

"""
Use the pattern
"""
# Create subject
weather_station = WeatherStation()

# Create Observers
current_conditions_display = CurrentConditionsDisplay()
stats_display  = StatisticsDisplay()

# Register Observers with Subject
weather_station.register_observer(current_conditions_display)
weather_station.register_observer(stats_display)

# Update weather
weather_station.set_measurements(25, 65, 1.02)
weather_station.set_measurements(22, 70, 1.05)
