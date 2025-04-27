class bird:

    def __init__(self):
         print("Bird is ready")

    def who_is_this(self):
         print("bird")

    def swim(self):
         print("swim faster")

class penguin(bird):

     def __init__(self):
          super().__init__()
          print("penguin ready")

     def who_is_this(self):
          print("penguin")

     def run(self):
          print("run faster")


peggy = penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()