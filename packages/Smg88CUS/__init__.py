from Smg88CUS import Smg88Class
import random as r

def test_smg88Class_overloading():
  randGen = lambda: r.randrange(0, 100, 0.1) # Hard coded values here
  class testArgumentNumber(metaclass=Smg88Class):
    def f(self, a): return [a]
    def f(self, a,b): return [a,b]
    def f(self, a,b,c): return [a,b,c]
  testArgumentNumberInstance = testArgumentNumber() # Creates instance because I don't fully understand and want to make sure (actual functionality works :)
  tr_vals = [randGen() for i in range(0, 3)]
  assert testArgumentNumberInstance.f(tr_vals[0], tr_vals[1], tr_vals[2])