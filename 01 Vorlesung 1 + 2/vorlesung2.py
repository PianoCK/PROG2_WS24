from abc import ABC, abstractmethod

class Werkzeug(ABC):
    @abstractmethod
    def benutze(self):
        pass

class Stock(Werkzeug):
    def benutze(self):
        print("Hau drauf")

class Schaufel(Werkzeug):
    def benutze(self):
        print("...graben...")

class Bagger(Werkzeug):
    def benutze(self):
        print("buddel buddel...")

class Knecht:
    def __init__(self, werkzeug: Werkzeug):
        self.werkzeug = werkzeug

    def nehme(self, werkzeug: Werkzeug):
        self.werkzeug = werkzeug

    def benutze_werkzeug(self):
        self.werkzeug.benutze()


stock = Stock()
schaufel = Schaufel()
bagger = Bagger()
hein = Knecht(bagger)
hein.benutze_werkzeug()
hein.nehme(schaufel)
hein.benutze_werkzeug()