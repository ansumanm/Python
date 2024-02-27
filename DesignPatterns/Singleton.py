class Singleton:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(Singleton, cls).__new__(cls, *args, *kwargs)
    return cls._instance
  
  def some_business_logic(self):
    pass

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

assert singleton1 is singleton2
