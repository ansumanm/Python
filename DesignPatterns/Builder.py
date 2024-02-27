"""
Builder pattern components:
  Builder: Abstract interface for creating parts of a Product object.
  Concrete Builder: Implements the Builder interface.
  Director: Constructs an object using Builder interface.
  Product: Represents the complex object being built.
"""
from abc import ABC, abstractmethod

"""
Product class
"""
class Car:
  def __init__(self):
    self.features = []

  def add_feature(self, feature):
    self.features.append(feature)

  def list_features(self):
    return ', '.join(self.features)
  
"""
Builder interface
"""
class CarBuilder(ABC):
  @abstractmethod
  def set_wheels(self):
    pass

  @abstractmethod
  def set_color(self):
    pass

  @abstractmethod
  def add_extra_feature(self, feature):
    pass

  @abstractmethod
  def get_results(self):
    pass

"""
Concrete Builders
"""
class SportsCarBuilder(CarBuilder):
  def __init__(self):
    self.car = Car()

  def set_wheels(self):
    self.car.add_feature('4 sports wheels')

  def set_color(self):
    self.car.add_feature('red color')

  def add_extra_feature(self, feature):
    self.car.add_feature(feature=feature)

  def get_results(self):
    return self.car
  
class SUVCarBuilder(CarBuilder):
  def __init__(self):
    self.car = Car()

  def set_wheels(self):
    self.car.add_feature('4 SUV wheels')

  def set_color(self):
    self.car.add_feature('black color')

  def add_extra_feature(self, feature):
    self.car.add_feature(feature=feature)

  def get_results(self):
    return self.car
  
"""
Director
"""
class CarDirector:
  def __init__(self, builder):
    self._builder = builder

  def construct_car(self):
    self._builder.set_wheels()
    self._builder.set_color()

  def get_car(self):
    return self._builder.get_results()
  
"""
Use the builder
"""
sportsCarBuilder = SportsCarBuilder()
director = CarDirector(sportsCarBuilder)
director.construct_car()
sports_car = director.get_car()
print("Sports car features: ", sports_car.list_features())

suvCarBuilder = SUVCarBuilder()
director = CarDirector(suvCarBuilder)
director.construct_car()
suvCar = director.get_car()
print("SUV car features: ", suvCar.list_features())
