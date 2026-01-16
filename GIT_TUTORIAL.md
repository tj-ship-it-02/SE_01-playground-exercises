# Git Basics - Einfache Anleitung

## Was ist Git?
Git ist ein Versionskontrollsystem - es speichert alle Versionen deines Codes, damit du:
- Änderungen nachverfolgen kannst
- Zu früheren Versionen zurückkehren kannst
- Mit anderen zusammenarbeiten kannst

## Die 3 wichtigsten Befehle (80% der Zeit):

### 1. `git status`
**Was macht es?** Zeigt dir, welche Dateien geändert wurden
```bash
git status
```

### 2. `git add .`
**Was macht es?** "Staged" alle Änderungen (bereitet sie zum Speichern vor)
```bash
git add .          # Alle Dateien
git add datei.py   # Nur eine bestimmte Datei
```

### 3. `git commit -m "Nachricht"`
**Was macht es?** Speichert die Änderungen mit einer Nachricht
```bash
git commit -m "Counter-Fehler behoben"
```

## Der typische Workflow:

```
1. Code schreiben/ändern
2. git status          → Siehst was geändert wurde
3. git add .           → Bereite Änderungen vor
4. git commit -m "..." → Speichere mit Nachricht
5. Wiederholen!
```

## Weitere nützliche Befehle:

### Repository initialisieren (einmalig):
```bash
git init
```

### Änderungsverlauf ansehen:
```bash
git log
```

### Zu einem Online-Repository hochladen (später):
```bash
git push
```

### Vom Online-Repository herunterladen:
```bash
git pull
```

## Tipps:
- **Commit-Nachrichten** sollten kurz und beschreibend sein: "Counter-Fehler behoben", "Rock-Paper-Scissors verbessert"
- **Commit oft!** Lieber viele kleine Commits als wenige große
- **`git status`** ist dein Freund - nutze es oft!
