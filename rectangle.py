
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_hekef(self):
        return (self.width + self.height) * 2

    def get_area(self):
        return self.width * self.height

