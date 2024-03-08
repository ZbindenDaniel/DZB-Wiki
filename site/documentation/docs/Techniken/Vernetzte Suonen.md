Vernetzte Schieber die entlang der Suonen verteilt sind und soviel Wasser durchlassen wie weiter unten gebraucht wird. Suonen können durch Speicher ergänzt werden. Es entsteht ein 'smart Grid'.

Jeder Schieber misst wie viel Wasser fliesst.
Jeder Schieber regelt den Fluss anhand eines Sollwerts.
Der Sollwert wird so ausgelegt, das das Wasser möglichst lange am Berg bleibt und langsam fliesst.

Wasser kann somit in den Suonen gespeichert werden.

Dazu braucht es aber eines geeigneten Models. Verbraucher können ebenfalls modelliert werden.
Speicher(Suonen-Abschnitte) sind aneinander gereit(in Serie)
Am Ende jedes Abschnitts liegt eine Schleuse mit einem Regler.

Der Sollwert ist abhängig von
- max Kapazität [cM]
- Füllstand nächste Suone(n) [lN]
- Zufluss [i]
- Schedule (wo braucht es wann wie viel Wasser) [t(t)]
- Prediction (Was passiert mit dem Zufluss) [iP(t)]


Aufbau
Schieber mit Motor, LoRa, Solarzelle, Sandsäcke

Knackpunkt: Algorithmus

Entnahme
Am besten muss ein Überschuss dort verteilt werden wo er am besten gebraucht werden kann.
Das heisst die Entnahme muss dementsprechend gestaltet werden.
- automatische Entnahme anhand Füllstand (Überlaufprinzip)
- Regelung gemäss Verteilschema (Am Montag ist Wasser bei A verfügbar, am Dienstag bei B)
- Speicher immer voll halten.

Fragen:
- Wie viel Kapazität ist in den Suonen? (Schätzungsweise 20m^3/km)
- kann der Verbrauch modelliert werden?
- Ist es Gut wen das Wasser lange im Hang bleibt
- wie wird das Wasser optimal gebraucht?
- Ist der Bedarf da
- Kosten Nutzen

Eventuelle Benefits.
- Bestehende Infrastruktur kann als Speicher benutzt werden.
- Die Verteilung kann Fair geregelt und dem Bedarf angepasst werden.
- Bewässerung kann evtl. nachts statt finden um Verdunstung zu verringern
- Das System kann leicht ortsunabhängig erweitert werden.
- Die Infrastruktur eignet sich gut zur Fassung von Niederschlag. Wen die Verteilung optimiert wird wär das doch gut
- Kultur und Geschichte wieder aufleben lassen. Bestehendes Wieder nutzen.

