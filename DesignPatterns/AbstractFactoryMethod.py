"""
In theory, we make the Factory class abstract, and create concrete factories, each factory creating multiple objects.
"""
from abc import ABC, abstractmethod

# Step 1: Create Abstract products.
class Chair(ABC):
  @abstractmethod
  def sit_on(self):
    pass

class Sofa(ABC):
  @abstractmethod
  def lie_on(self):
    pass

# Step 2: Create Concreate products
class VictorianChair(Chair):
  def sit_on(self):
    return "Sitting on Victorian chair."
  
class ModernChair(Chair):
  def sit_on(self):
    return "Sitting on Modern chair."
  
class VictorianSofa(Sofa):
  def lie_on(self):
    return "Lying on Victorian Sofa."
  
class ModernSofa(Sofa):
  def lie_on(self):
    return "Lying on Modern Sofa."
  
# Step 3: Define Abstract Factory
class FurnitureFactory(ABC):
  @abstractmethod
  def create_chair(self):
    pass

  @abstractmethod
  def create_sofa(self):
    pass

# Step 4: Implement concrete factories
class VictorianFurnitureFactory(FurnitureFactory):
  def create_chair(self):
    return VictorianChair()
  
  def create_sofa(self):
    return VictorianSofa()
  
class ModernFurnitureFactory(FurnitureFactory):
  def create_chair(self):
    return ModernChair()
  
  def create_sofa(self):
    return ModernSofa()
  
# Step 5: Use the factory
def furniture_client(factory: FurnitureFactory):
  chair = factory.create_chair()
  sofa = factory.create_sofa()
  print(chair.sit_on())
  print(sofa.lie_on())


# Create Victorian-style furniture
victorian_factory = VictorianFurnitureFactory()
furniture_client(victorian_factory)

# Create modern-style furniture
modern_factory = ModernFurnitureFactory()
furniture_client(modern_factory)


  

