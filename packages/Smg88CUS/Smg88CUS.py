print("HOLY IT ACTUALLY WORKS!!!")

"""
The plan:

class customClass(metaclass=Smg88.Class.Decorator(overload=True)):
  def exampleFunc(input: Smg88.Annotations.BuiltIt(list, input_range=lambda i: 0 <= i <= 10))):
    #!!Smg88::Require::Strict Parameters # Ensures that my module raises non-conforming params
    #!!Smg88::Require::Level ?MODULE_DEFINED? Debugging # Will set debugging level to module num
    #!!Smg88::Ensure::Level <=30 Debugging # 'Ensure' means try but only warn if not
    print(f"{Smg88.ass(input, gen=Smg88.assGen(simple=True))}")

"""
"""
First Part:

- Completely learn what a metaclass can do :)
- Create a solid overload system

"""
"""
Second Part:

- Be able to extract stuff from comments
- Or, if that is not possible at run time, create an easy alternative :)

"""
"""
Third Part:

- Use type checking software ;) mypy

"""

class SmgClass(type):
  """
  This class is designed to be used as a meta class
  """
  def __init__(self):
    