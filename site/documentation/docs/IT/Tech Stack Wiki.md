
## Wiki
Das WIki wird mittels Obsidian, VSC und MkDocs zusammengebaut.

Mit mkdocs build wird das wiki lokal gebuilded und unter /site abgelegt

```.\scripts\copyFilesForPublish.sh``` verschiebt die Dateien die in scripts/whitelist.txt eingetragen sind in das öffentliche Repo 'DZB-Wiki' und pushed diese auf GitHub. über einen Webhook wird die Website dazu aufgefordert die statische Website vom repo zu pullen.

### plugins

[[TODO]]: Dynamische Liste mit Plugins

## API

Unter https://api.dzb-projects.ch/swagger/ kann die API Dokumentation gefunden werden. Diese hat aber bisher keine Relevanz im Projekt.

## Kommentar System
https://docs.barkdull.org/hashover-v2 wird als Kommentar-System verwendet und läuft unter https://comments.dzb-projects.ch/  als PHP-Anwndung.

# Installation / Setup

[[Todo]]