# Classifier_tf2_first
Image Classification with Tensorflow 2.4 and Keras in jupyter notebook or PyCharm.

falls nicht schon in anderen Projekten erfolgt

# 1. Anaconda installieren
Download Anaconda von https://www.anaconda.com/products/individual
Hier wird Anaconda mit Python3.8 verwendet.

Anaconda Package installieren unter C:\Anaconda.

Beim Isnstallieren, sollte das Häcken für das automatische Setzen der systemeviroment Pfade, gesetzt werden.

Unter Suche in Windows die Systemungebungsvariabel, Klicke auf Umgebungsvariablen, unter den Systemvariabeln such "Path" doppelklick darauf, sollten folgende Einträge zu finde n sein. Fehlende einfach manuell nachtragen.

![image](https://user-images.githubusercontent.com/84871742/120812007-e1b73a00-c54c-11eb-8184-27be9191347a.png)

# 2. Bibliotheken anlegen/installieren
Anaconda prompt öffnen, dort sollte die Base-Enviroment automatisch geöffnet werden.
Oder über cmd die Base-Enviroment activieren, mit:
- activate base

Die Base-Enviroment enthält fast alle Bibliotheken die genutzt werden. Es muss nur Tensorflow und Keras zusätzlich installiert werden.  
Dazu die Befehle:
- pip install tensorflow==2.4.0
- pip install keras==

nutzen.

# 3. Clone Repository
Nun kann das Repository "Classifier_tf2_first" mit der gesamten Ordnerstrukturund, dem Jupyter Notebook und den Python-Scripten geclont werden.
Dazu z.B.

Zum Nutzen des Jupyter Notebooks, mit Anaconda-Prompt oder cmd in den angelegten Ordner manövrieren und Jupyter Notebook starten. z.B.:
- cd c:\Tensorflow2\Classifier_tf2_first
- jupyter notebook

Die Bilder der zu trainierenden Klassen müssen im Unterordner /Images/Train/  abgelegt werden. Dazu die Bilder in klassenorientierten Unterordner ablegen.


Im Jupyter Notebook sind weitere Hilfestellungen beschrieben, wenn Anpassungen nötig sind oder optional zur Verfügung stehen.

Anstatt Jupyter Notebook können auch die Python Scripte z.B. mit PyCharm editiert und ausgeführt werden.

# Viel Spaß.

