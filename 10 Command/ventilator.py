from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Any

class Ventilator:
    OFF = 0
    ON = 1
    FAST = 2

    def __init__(self):
        self.mode = self.OFF

    def aendere_mode(self, mode):
        if mode == self.OFF:
            print("Ventilator AUS")
        if mode == self.ON:
            print("Ventilator AN")
        if mode == self.FAST:
            print("Ventilator FAST")

class Command(ABC):
    def __init__(self, ventilator):
        self.ventilator = ventilator

    @abstractmethod
    def execute(self):
        pass

class CmdVentilatorAn(Command):
    def execute(self):
        self.ventilator.aendere_mode(venti.ON)

class CmdVentilatorAus(Command):
    def execute(self):
        self.ventilator.aendere_mode(venti.OFF)

class CmdVentilatorFast(Command):
    def execute(self):
        self.ventilator.aendere_mode(venti.FAST)

class Logitech:
    def __init__(self):
        self.tasteOben = None
        self.tasteMitte = None
        self.tasteUnten = None
        self.speicher = []

    def setTasteOben(self, cmd: Command):
        self.tasteOben = cmd

    def setTasteMitte(self, cmd: Command):
        self.tasteMitte = cmd

    def setTasteUnten(self, cmd: Command):
        self.tasteUnten = cmd

    def klickeTasteOben(self):
        self.speicher.append(self.tasteOben)
        self.tasteOben.execute()

    def klickeTasteMitte(self):
        self.speicher.append(self.tasteMitte)
        self.tasteMitte.execute()

    def klickeTasteUnten(self):
        self.speicher.append(self.tasteUnten)
        self.tasteUnten.execute()

    def replay(self):
        for cmd in self.speicher:
            cmd.execute()

    def undo(self):
        self.speicher.pop()
        self.speicher[-1].execute()


venti = Ventilator()
logitech = Logitech()
logitech.setTasteOben(CmdVentilatorAn(venti))
logitech.setTasteMitte(CmdVentilatorAus(venti))
logitech.setTasteUnten(CmdVentilatorFast(venti))

logitech.klickeTasteOben()
logitech.klickeTasteMitte()
logitech.klickeTasteUnten()
logitech.klickeTasteMitte()
logitech.klickeTasteUnten()

print("Replay:")
logitech.replay()
logitech.undo()