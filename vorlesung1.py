##### Aufgabe 12 (16 Punkte) Parkplatzverwaltungssystem

'''
In dieser Aufgabe sollen Sie zwei Klassen erstellen, die zusammenarbeiten, um ein Parkplatzverwaltungssystem zu modellieren. Die Klassen sind Fahrzeug und Parkplatz.

Klasse **Fahrzeug**:

Attribute:

* **kennzeichen**: str - Das Kennzeichen des Fahrzeugs.
* **fahrzeugtyp**: str - Der Typ des Fahrzeugs (z.B. "PKW", "LKW", "Motorrad").
* **geparkt**: bool - Zeigt an, ob das Fahrzeug aktuell geparkt ist (Standardwert: False).

Konstruktor: Alle Attribute sollen bei der Instanzierung der Klasse gesetzt werden. 
Zusätzlich soll eine Überprüfung stattfinden, ob das Kennzeichen und Fahrzeugtyp gesetzt wurden.

Klasse **Parkplatz**:

Attribute:

* **standort** str
* **kapazitaet**: int - Die maximale Anzahl an Fahrzeugen, die gleichzeitig parken können.
* **fahrzeuge**: list[Fahrzeug] - Eine Liste, die die aktuell geparkten Fahrzeuge enthält (zunächst leer).

Methoden:

* **parken(fahrzeug: Fahrzeug)**: Parkt ein Fahrzeug auf dem Parkplatz, wenn noch Kapazität vorhanden ist. 
Die Methode soll sicherstellen, dass kein Fahrzeug mit dem gleichen Kennzeichen mehrfach geparkt wird. 
Bei einem Versuch, ein solches Fahrzeug zu parken, soll eine klare Warnmeldung ausgegeben und das Fahrzeug nicht hinzugefügt werden.
* **verlassen(kennzeichen: str)**: Entfernt ein Fahrzeug anhand des Kennzeichens vom Parkplatz. 
Wenn das Fahrzeug gefunden und entfernt wird, soll eine Bestätigung ausgegeben werden. 
Andernfalls wird eine Fehlermeldung angezeigt.
'''

class Fahrzeug:
    def __init__(self, kennzeichen, fahrzeugtyp):
        self.kennzeichen = kennzeichen
        self.fahrzeugtyp = fahrzeugtyp
        self.geparkt = False

        if self.kennzeichen == "" or self.fahrzeugtyp == "":
            print("Die Daten sind nicht vollständig. Bitte ergänzen.")


class Parkplatz:
    def __init__(self, standort: str, kapazitaet: int):
        self.standort = standort
        self.kapazitaet = kapazitaet
        self.fahrzeuge = []

    def parken(self, fahrzeug: Fahrzeug):
        if len(self.fahrzeuge) >= self.kapazitaet:
            print("Das Parkhaus ist leider voll")
            return

        for geparktes_fahrzeug in self.fahrzeuge:
            if geparktes_fahrzeug.kennzeichen == fahrzeug.kennzeichen:
                print("Das Kennzeichen existiert schon.")
                return
            
        self.fahrzeuge.append(fahrzeug)
        fahrzeug.geparkt = True

    def verlassen(self, kennzeichen):
       for geparktes_fahrzeug in self.fahrzeuge:
            if geparktes_fahrzeug.kennzeichen == kennzeichen:
                self.fahrzeuge.remove(geparktes_fahrzeug)
                geparktes_fahrzeug.geparkt = False
                print(geparktes_fahrzeug.kennzeichen,"verlässt Parkplatz")
                return
                
# Testfälle
fahrzeug1 = Fahrzeug("KI-XY 123", "PKW")
fahrzeug2 = Fahrzeug("ECK-AA 999", "Motorrad")
fahrzeug3 = Fahrzeug("RD-QQ 121", "PKW")

parkplatz = Parkplatz("Zentrum", 2)

parkplatz.parken(fahrzeug1)
parkplatz.parken(fahrzeug1)  # Sollte Fehlermeldung ausgeben
parkplatz.parken(fahrzeug2)
parkplatz.parken(fahrzeug3)  # Sollte Fehlermeldung ausgeben

parkplatz.verlassen("KI-XY 123")
parkplatz.verlassen("M-UD 555")  # Sollte Fehlermeldung ausgeben



