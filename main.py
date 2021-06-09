import math
class CartesianP:

      def __init__(self, x, y, name):
          self.x = x
          self.y = y
          self.name = name

      def input_attributes(self):
          self.x = float(input(" faka ikho odineythi zakho ze x aksiz "))
          self.y = float(input(" faka ikho odineythi zakho ze y aksiz"))
          self.name = input("faka igama le poyinti")

      def poyntiy_axis(self):
          self.x = self.x * (-1)
          return self.x

      def poyntix_axis(self):
          self.y = self.y * (-1)
          return self.y

      def calc_distance(self):
          distance = math.sqrt((0-self.x) * (0-self.x) + (0-self.y) * (0-self.y))
          return distance

      def equation(self):
            gradient = (0-self.y) / (0-self.x)
            print("equation is", gradient, "x", "+", self.y)

      def quadrant(self):
          if self.x < 0 and self.y > 0:
            print("north west quadrant")
          if self.x > 0 and self.y > 0:
            print("north east quadrant")
          if self.x < 0 and self.y < 0:
            print("south west quadrant")
          if self.x > 0 and self.y < 0:
            print("south east quadrant")

if __name__ == '__main__':
    p = CartesianP(4, 6, "A")
    p.input_attributes()
    p.poyntix_axis()
    p.poyntiy_axis()
    p.calc_distance()
    p.equation()
    p.quadrant()
