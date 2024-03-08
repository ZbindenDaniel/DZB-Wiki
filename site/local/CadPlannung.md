
## Idee
CAD Software könnte sich in der Planung als nützlich erweisen. Einzelne Strukturen und Gebäude können digital und in 3D Geplant werden, was Fehler reduziert und Flexibilität erhöht. Zudem können die Pläne, falls Topografische Karten vorhanden sind, in die Landschaft eingefügt werden. Dies ist ebenfalls zur Planung nützlich und somit kann eine Art [Digital Twin](https://en.wikipedia.org/wiki/Digital_twin) des Projekts erstellt werden. Dieser wiederum bietet folgende Möglichkeiten:
- zu Vorstellungszwecken
  - Aufbau des Projekts kann aus der Ferne betrachtet und analysiert werden  
- zur Planung
  - Verschiedene Versionen einer Idee können simuliert werden und so die Entscheidungsfindung verbessert werden
- als Interface
  - Prozesse & Inventar können in Echtzeit repräsentiert und gesteuert werden
- ........
    - GPS Messdaten erheben/organisieren -> [ArcGis](https://developers.arcgis.com/unity/)
    - In Unity oder anderem tool einfügen
    - Layer für die verschiedenen Aspekte erstellen [Here](https://www.tenthacrefarm.com/6-maps-permaculture-farm-design/)
      - 1 Map
      - 2 Satellitenaufnahme
      - 3/5 Physische Objekte  (Gebäude,Pflanzen, , Inventar, Produktionsanlagen)
      - 5-10 Geografie (5 Layers für verschiedene overlays)
      - 15-20 Permaculture zones 0-5
      - 21 Wasser
      - 22-26 environmental maps
        - snow
        - rain
        - wind
        - sun/shade
        - frost
      - 27 Vorher Nacher (Versionierung, Visualisierung Progress/Planungsschritte)
      - 28 SensorMap (Sensordaten)
      - 29 Interconnections of Systems
      - 
### Optionen
- Unity (Game Engine)
  - Bereits Erfahrung da
  - Extrem flexibel und gut möglich Digital Twin zu kreieren
  - Einfache ANbindungsmöglichkeit an andere Software
- QGis (Open source Tool für Spatial analysis)
  - Funktionalität für verschiedne Analysen vorhanden
  - Zugang zu Karten material
  - No Code
 -  Kombination
  - QGis zur generierung von Karten und anfänglicher Analyse
  - Unity zur Erstellung eines userinterface und DT   
- Obsidian Plugin for maps


## Problematik GIS
Standartmässig Karten in Unity einzufügen Mögliche stellt sich als schwierig heraus. Ich habe Karten von Swiss topo aber sie sind irgendwie im falschen Format (tiff anstatt .raw) auch habe ich Lidar Daten, aber das selbe Problem 

Die Daten können theoretisch konvertiert werde aber das einfügen hat sich bei Tests auch als schwieig herausgestellt da die Katen je nach dem unerkentlich verzerrt sind. Ich konnte die Daten vom XYZ Format in ein Mesh, wie sie unity verwendet parsen. Jedoch scheint irgendetwas noch nicht zu stimmen, die Darstellung ist stark verzerrt

[ ] Mögliche Lösung https://developers.arcgis.com/unity/get-started/
[ ] Evtl. Zu Hohe Anforderungen für Laptop
[ ] Evtl. Kompliziert zu bedienen oder Veränderungen vorzunehmen

### UPDATE
Auch nach einlesen der Daten vom schweizer publi service gibt es Probleme. Die Auflösung scheint zu gering zu sein um sinnvoll eingesett zu werden. Es stellt sich die Frage ob beim generieren des Mesh's ein fehler auftritt oder ob idee Daten zu ungenau sind. Vermutung: Fehler meinerseits
## Karten
- [Maps of Switzerland](https://www.swisstopo.admin.ch/en/geodata/maps.html)


## Überlegungen 2D/3D

was bedarf überhaupt eines CAD/3D models?
- Sun map (indirekt)
- Cad Plannung für Gebäude
- Orginalgeträue Visu

--> 2D reicht wohl für den Anfang aus. 
- **wichtig ist mal Sektorenplannung**

- praktisch wäre object map als management tool 
