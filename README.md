# Parsons Puzzles Generator

## Übersicht

Dieses Projekt besteht aus Python-Skripts, die `.txt`-Dateien mit Python-Code einlesen und aus diesen Parsons-Puzzles im TikZ-Format generieren. Darüber hinaus können `.pzl`-Dateien für das js-parsons-Projekt erstellt werden. 

## Funktionen

- **Einlesen von .txt-Dateien**: Diese Dateien enthalten Python-Code, aus dem Parsons-Puzzles generiert werden.
- **Modifier**:
  - **id_or**: ODER-Verknüpfung von Codezeilen mit dem Infix `#|`.
  - **id_opt**: Optionale Codezeilen mit dem Suffix `#*`.
- **Generierung von TikZ-Puzzles**: Erstellt visuell ansprechende Parsons-Puzzles in TikZ, die in LaTeX-Dokumente integriert werden können.
- **Einlesen von .pzl-Dateien**: Diese Dateien werden für das js-parsons-Projekt verwendet, um spezielle PPs zu generieren.

## Installation

Stellen Sie sicher, dass Sie Python 3.x installiert haben. Klonen Sie das Repository und installieren Sie die erforderlichen Pakete:

```bash
git clone https://github.com/jtormoehlen/tikz_puzzle.git
cd tikz_puzzle
pip install -r requirements.txt
```

## Verwendung

1. Erstellen Sie eine `.txt`-Datei mit dem gewünschten Python-Code. Beispiel:

    ```python
    def add(a, b):
        return a + b
        
    print(add(2, 3))
    ```

2. Optional können Sie Modifier zu Ihren Codezeilen hinzufügen:

    ```python
    print(add(2, 3)) #| print(add(3, 6))
    def add(a, b): #*
    ```

3. Um das Parsons-Puzzle in TikZ zu generieren, führen Sie das Skript aus:

    ```bash
    python tikz_puzzle.py input.txt output.tex
    ```

4. Für die Erzeugung einer .pzl-Datei aus einer .txt-Datei verwenden Sie:

    ```bash
    python widget.py input.txt output.pzl
    ```

## Beispiele

Sie finden einige Beispiele für `.txt`-Dateien und die entsprechenden `.tex`- und `.pzl`-Dateien im Verzeichnis `tikz_src` bzw. `tikz_tex` und `widget_src/in`.