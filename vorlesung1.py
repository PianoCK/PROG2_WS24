##### Aufgabe 12 (16 Punkte) Parkplatzverwaltungssystem

''' In dieser Aufgabe sollen Sie zwei Klassen erstellen, die zusammenarbeiten, um ein Parkplatzverwaltungssystem zu modellieren. Die Klassen sind Fahrzeug und Parkplatz.

Klasse **Fahrzeug**:

Attribute:

* **kennzeichen**: str - Das Kennzeichen des Fahrzeugs.
* **fahrzeugtyp**: str - Der Typ des Fahrzeugs (z.B. "PKW", "LKW", "Motorrad").
* **geparkt**: bool - Zeigt an, ob das Fahrzeug aktuell geparkt ist (Standardwert: False).

Konstruktor: Alle Attribute sollen bei der Instanzierung der Klasse gesetzt werden. Zusätzlich soll eine Überprüfung stattfinden, ob das Kennzeichen und Fahrzeugtyp gesetzt wurden.

Klasse **Parkplatz**:

Attribute:

* **standort** str
* **kapazitaet**: int - Die maximale Anzahl an Fahrzeugen, die gleichzeitig parken können.
* **fahrzeuge**: list[Fahrzeug] - Eine Liste, die die aktuell geparkten Fahrzeuge enthält (zunächst leer).

Methoden:

* **parken(fahrzeug: Fahrzeug)**: Parkt ein Fahrzeug auf dem Parkplatz, wenn noch Kapazität vorhanden ist. Die Methode soll sicherstellen, dass kein Fahrzeug mit dem gleichen Kennzeichen mehrfach geparkt wird. Bei einem Versuch, ein solches Fahrzeug zu parken, soll eine klare Warnmeldung ausgegeben und das Fahrzeug nicht hinzugefügt werden.
* **verlassen(kennzeichen: str)**: Entfernt ein Fahrzeug anhand des Kennzeichens vom Parkplatz. Wenn das Fahrzeug gefunden und entfernt wird, soll eine Bestätigung ausgegeben werden. Andernfalls wird eine Fehlermeldung angezeigt.

'''

