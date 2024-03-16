# Doc utilisation de python avec Qt et création d'un exécutable du projet :

## Pour crée un environement :

```cmd
python.exe -m venv env
```

Si vous avez une installation de Python particuliaire :

```cmd
& c:/Votre/chemin/vers/leDossier/python.exe -m venv env
```

**Pour lancer l'environement fair la commande :**

```cmd
.\env\Script\activate
```

> [!NOTE]
> Sur `VSCode` vous pouvez (si il ne sait pas crée tout seul) créer un dossier 
> `.vscode` dans le qu'elle créer un fichier `settings.json`.
>
> Dans le fichier `settings.json` écrir :
> ```json
> {
>    "python.pythonPath": "env\\Scripts\\python.exe"
> }
> ```
> Cela lancera l'environement Python à l'ouverture du dossier de travail.

## Pour installer une librairie dans l'environement :

**Rechercher les dépendances de la lib.**

Ouvrir dans `WinPython` ouvrir `WinPython Command Prompt`.

Taper la commande : 
```cmd
pip show lib
```

Recuperé la `Version` et les `Requires`.

> [!NOTE]
> Si la commande `pip show` retourne :
> `WARNING: Package(s) not found: "la librairie"`, 
> c'est soit que _la librairie_ est un bibliothèque standard de python qui n'a 
> pas besoin d'être ajouté, soit qu'elle n'est pas déjà dans votre système donc 
> vous devez trouver vous même les dépendances et versions compatibles avec 
> votre installation.

**Si il y a des `Requires` :**

Rechercher le(s) dépendance(s) jusqu'à qu'il n'y en est plus

**Si il n'y a pas des `Requires` :**

Téléchargé sur [L'index des paquets Python](https://pypi.org) la lib,
prendre la bonne `Version` dans l'onglet `Historique des versions` et
télécharger _la librairie_ et l'ajouter au dossier `bdd_lib`.

> [!TIP]
> Choisir de préférence la distribution compilées (si disponible).

> [!WARNING]
> Les distributions compilées ne sont pas toutes compatible avec votre 
> environement.
> Il faut choisir la bonne version si elle n'est pas `any`.
> 
> Exemple : pour `numpy` sur `Windows 64 bits` avec `Python 3.9.10`, 
> il faut choisir la version `cp39-win_amd64`.

**Maintenant que tout les librairies sont dans le dossier pour les installer :**

```cmd
pip install lib --no-index --find-link file:bdd_lib/
```

Ne tapé que _la librairie_ que vous avez besoin, la commande trouvera elle même 
les dépendances de _la librairie_ dans le dossier.

## Pour créer et utiliser le fichier `requirements.txt` :

_Le fichier requirements.txt permet de partager le code à une autre personne._

**Pour créer la fichier `requirements.txt` executer la commande :**

```cmd
pip freeze > requirements.txt
```

Pour transmettre le code à une autre personne, il vous suffit de lui envoyer
tout sauf le dossier `env` et (si vous l'avez) le dossier `.vscode`.

**Pour installer les librairies grâce au fichier `requirements.txt` :**

```cmd
pip install -r requirements.txt --no-index --find-link file:bdd_lib/
```

> [!TIP]
> Si la personne à internet sur son poste de travail, elle a juste à taper :
> ```
> pip install -r requirements.txt
> ```
> ou à installer les librairies depuis 
>[L'index des paquets Python](https://pypi.org) avec la commande :
> ```
> pip install lib
> ```

## Pour créer une interface graphique en utilisant `Qt Designer` :

`Qt Designer` est une application de création d'interface graphique multi-langage
basé sur la bibliothèque Qt. Pour `Python` il existe deux librairies qui utilise 
la bibliothèque Qt, `PyQt` et `PySide`. Dans cette exemple nous utiliserons la
librairie `PySide6`. 

La documentation pour 
[Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html) 
et pour [PySide6](https://doc.qt.io/qtforpython-6/index.html).

### Création de l'interface graphique :

Dans `Qt Designer` crée un `New Form -> Main Window`. Ajouter tout les widgets 
Qt que vous avez besoin et penser à leurs donner un `objectName` cohérant car
c'est cette variable qui va nous permettre d'y accéder dans le programme Python.

Sauvegarder votre interface graphique dans le dossier de travail, sous le nom 
`MainWindow.ui`. Maintenant que nous avons notre interface, il faut la convertir
en Python. Pour cela vous allez taper la commande suivante :

```cmd
pyside6-uic MainWindow.ui -o ui_mainwindow.py
```

Cela va générer le code de votre interface graphique pour qu'il puisse être
utilisé par Python.

> [!NOTE]
> Si vous avez ajoutés des ressources dans votre interface depuis `Qt Designer`, 
> vous devriez avoir aussi un fichier avec l'extension `.qrc` (Voir doc 
> [Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html)). Dans ce cas là,
> il vous faudra aussi générer le code Python pour les ressources avec :
> ```cmd
> pyside6-rcc fichier.qrc -o rc_fichier.py
> ```
> Notez que des ressources en format `.svg` sont plus adaptées aux interfaces graphiques car elles sont en vectoriels donc redimensionnables.

### Utilisation de l'interface graphique :

Vous pouvez normalement lancer le fichier `Exemple.py`. Il contient le minimum 
de ce qu'il faut pour lancer votre interface. Il y est détaillé les commandes
et vous trouverez aussi le code pour utiliser les `Threads` Qt, qui vous 
permetrons de faire tourner du code _long_ sans figer l'interface.

À vous de jouez pour créer de nouvelles applications.

> [!TIP]
> Vous pouvez à tout moment changer l'interface graphique de votre application en
> ouvrant le fichier `MainWindow.ui` avec `Qt Designer`. Une fois les 
> modifications faites, sauvegardé au même endroit avec le même nom et réexecuté 
> la commande  pour convertir en Python l'interface. C'est bon vous n'avez plus 
> qu'à relancer votre code pour voir le résultat.

> [!NOTE]
> Tous vos objets Qt sont dans le code appelable après `self.ui.` et vous pouvez 
> aussi en rajouter à votre interface depuis le code sans passer par le fichier 
> `.ui`, il ne sera juste pas visible dans `Qt Designer`.

> [!TIP]
> Vous pouvez créer des paternes pour l'interface en créant des objets Qt 
> spécifique.
> 
> Exemple de création d'un objet Qt :
> ```python
> class DeleteButton(QPushButton):
> 
>     def __init__(self):
> 
>         super().__init__()
> 
>         sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
>         sizePolicy.setHorizontalStretch(0)
>         sizePolicy.setVerticalStretch(0)
>         sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
> 
>         self.setSizePolicy(sizePolicy)
> 
>         icon = QIcon()
>         icon.addFile(u":/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
> 
>         self.setIcon(icon)
>         self.setText("Supprimer de la liste")
> ```

> [!NOTE]
> Il est possible de faire passer en global un variable Python sans passer par la
> méthode `Global()`. Il vous suffit d'appeler votre variable `self.nomDeLaVar` 
> elle sera accessible depuis n'importe où dans la class.