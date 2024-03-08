---
Task: 0.5
Bereich: Landschaftsarbeiten
Voraussetzungen: 0.4
---
## Ausgangslage

Normalerweise gibt es Stunden für das ganze areal, wie viel Wasser pro Parzelle ist definiert
Ich hörte aber, dass alle machen was sie sie wollen. Deshalb gibt es nicht konstant Wasser
Im Sommer immer wieder gar kein Wasser in der Suone, da es schlicht zu wenig Wasser gibt.
> Die genaue Menge die entnommen werden kann ist immernoch unklar, der Verantwortliche nicht erreichbar.

Die Entnahme soll aber kein Problem darstellen.
Der Bach der Vertikal an den oberen Parzellen vorbei fliesst, führt nicht immer Wasser. Da es sich dabei um einen Überlauf handelt, fliesst nur bei Überschuss Wasser und im Herbst wird die Leitung getrennt.
Wasser sollte deshalb an der bestehenden Fassung abgenommen werden. Oder es muss dafür gesorgt werden, das immer etwas fliesst.

- [ ] Imhof Beat (tel. 0279239343) ist verantwortlich, anrufen und abklären
Parzellen: siehe [[Ausgangslage]]

## Überlegungen

Die Wasserfassung soll so konstruiert werden um Unterhaltsaufwand zu minimieren. 
Das heisst Verschmutzung, Verstopfung und Verschleiss soll vorgebeugt werden.
Gleichzeitig soll die gewünschte Menge Wasser gesammelt werden, unabhängig davon wie viel Wasser die Suone führt. Falls sehr wenig Wasser fliesst, sollte eine minimale Menge abfliessen. 

> Falls sich Sediment ansammelt kann es wiederverwertet werden.

### Hypothese

Die Fassung kann aus einem Rohr bestehen das 3-4 Mal dem Durchmesser der übrigen Leitungen entspricht. Dieses wird dicht mit der Ableitung verbunden und an einem günstigen Ort in die Suone gelegt und gegebenenfalls beschwert.

### Filter

Ein selbst reinigendes Filter kann eingesetzt werden. Dazu müssen ein oder mehrere Filter in einem 45° Winkel (oder in kurvenform) zum Zulauf montiert werden. Grössere Feststoffe wie Laub werden so durch das Sieb gefiltert und vom Fluss des Wassers abgeschieden. Alles was feiner ist als das Sieb gelangt zum Speicher-Tank und kann sich dort setzen.

## Unterhalt

Der Einsatz von Ventilen und Hähnen erhöht zwingend die Kosten sowie den Unterhalt der Anlage.
Falls die Möglichkeit besteht, das ohne externe Komponenten soviel Wasser fliesst wie gewünscht soll diese Möglichkeit bevorzugt werden.

> Es Bedarf also eines Systems das ohne bewegende Teile einen Regelkreis erzeugt.

## Anforderungen

Grundsätzlich gilt:
1. eine minimale Menge Wasser muss immer weiter die Suone herabfliessen.
2. Falls der Boden feucht genug ist bedarf es keines zusätzlichen Wasserzuflusses.
3. Der Fluss von Wasser muss komplett getrennt werden können
4. Der Einsatz von Speichern soll weiterhin möglich sein.

> Punkt 1 stellt keine Herausforderung dar. Fliesst immer ein Teil des Wassers an der Fassung vorbei ist die Bedingungen erfüllt.
> Punkt 3 ist ebenfalls ohne grossen Aufwand umsetzbar
> Punkt 4 wird nicht hoch Priorisiert, dieses System kann unabhängig konzipiert werden

Das Augenmerk wird also auf Punkt 2 gerichtet.
Fliesst X wasser so soll Y = a*(X-f_min) Zu einem Abscheider fliessen, der m * Y zum Gelände leitet.

X: Gesamtmenge Wasser die fliesst.
a: Prozentsatz der zur konstanten Bewässerung notwendig ist.
f_min: minimale Abflussmenge
Y: Menge die zum Abscheider fliesst.
m: Bedarf. Hier gilt m = 1/h, wobei h: Bodenfeuchte

## Konstruktion

- Rohr mit selbst reinigendem Filter in der Suone.
- Rohr hat eine Bohrung zum Durchlauf und eine zur Entnahme.
- In die Entnahmeleitung ist ein Hahn zur Dosierung verbaut. Sie führt zu einem Fass, in welches ein Entleerungs-Siphon verbaut ist.
- Somit wird das Fass, langsam und stetig gefüllt und schwallweise entleert.
- Das Wasser fliesst in die Konturlinien und bewässert so die ganze Fläche

### Überlauf

Falls etwas im System nicht funktioniert oder eine grosse Menge Niederschlag fällt soll das überfliessende Wasser sicher abgeleitet werden. 
Dazu kann eine Leitung dienen die das Wasser zurück zur Suone führt und/oder ein Graben der das überfliessende Wasser ableitet.

> Die Konturen benötigen einen Überlauf zur Suone hin

### Speicher

> Kann das absondern von Sediment verbessern

> Überbrückt die Zeit ohne Wasserzufuhr.

Wie viel Fassungsvermögen ist möglich, wie viel sinnvoll?
Pro Baum so 50l pro Woche?
? 10?

Wohin damit? - relativ nahe an Suone, hält Leitungen kurz, vereinfacht überlauf

### Berechnungen

Beispiel anhand der 1. Parzelle:[^1]
Die Grundformel zur Berechnung des Wasserbedarfs lautet:

> Wasserbedarf (V[Liter/Tag]) = ET x Fläche (A[m²]) × Bewässerungseffizienz (n_B)

Die Evapotranspiration (ET) kann aus lokalen meteorologischen Daten abgeleitet oder von [meteorologischen Diensten](https://www.meteoschweiz.admin.ch/service-und-publikationen/applikationen/ext/climate-drought-series.html) bereitgestellt werden. Die Bewässerungseffizienz hängt von der Bewässerungsmethode ab (z.B. Tropfbewässerung ist effizienter als Sprinklerbewässerung).

Um Ihnen ein spezifischeres Beispiel zu geben, nehmen wir an, dass die ET-Rate in Ihrer Region während der Wachstumsperiode etwa 5 mm/Tag beträgt und Sie eine Tropfbewässerung verwenden, die eine Effizienz von etwa 90% hat.

Wir können dann die benötigte Wassermenge für Ihre 300 m² große Fläche wie folgt berechnen:

Konvertiere ET von mm/Tag in Liter/Tag (1 mm Regen auf 1 m² entspricht 1 Liter Wasser).
Multipliziere die ET-Rate (in Liter) mit der Fläche.
Berücksichtige die Bewässerungseffizienz.
Lassen Sie uns die Berechnung durchführen:

Für Ihre 300 m² große Fläche benötigen Sie ungefähr 1667 Liter Wasser pro Tag, basierend auf einer Evapotranspiration (ET) von 5 mm/Tag und einer Bewässerungseffizienz von 90% durch Tropfbewässerung.
Hieraus würde sich ein konstanter Fluss von 1.15 l/min ergeben.

## Gefahren
1. Unfall
2. Hang rutscht ab
3. Zu wenig Wasser fliesst
4. Zu viel Wasser fliesst

### Massnahmen
1. [[Arbeitssicherheit]]
2. ?
3. ?
4. ?
 
## Materialliste

- [ ] Tank + Deckel
- [ ] Sand, Kies Steine für Fundament
- [ ] Fassung mit Filter
- [ ] x Meter Schlauch
- [ ] Schwimmer Ventil mit Gewinde, Mutter und Dichtung
- [ ] Hahn mit Gewinde, Mutter und Dichtung
- [ ] Verteiler mit Dichtungen und Zwischenstück zu Hahn
- [ ] Ventil mit Übergängen zu Verteiler und Bewässerung und Kabel
- [ ] Durchflusssensor mit Übergängen
- [ ] Schlauchverteiler für Bewässerung 
- [ ] Gewinde, Anschluss und Mutter für Überlauf
- [ ] Pvc Rohre mit Bögen für rigide Installationen
- [ ] 

## Werkzeuge

- [ ] Akkuschrauber
- [ ] Bohrset, Konus, Glockenbohrer
- [ ] Säge
- [ ] Messer
- [ ] Föhn
- [ ] Dichtungsmaterial
- [ ] Silikon
- [ ] Niveau
- [ ] Hammer
- [ ] Schrauben und Kleinmaterial



[^1]: [[1. Bepflanzungskonzept#Oberhalb der Strasse]]