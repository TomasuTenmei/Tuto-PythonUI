# Guide d'utilisation de Python avec Qt et création d'un exécutable pour le projet

## Pour créer un environnement :

```cmd
python.exe -m venv env
```

Si vous avez une installation de Python particulière :

```cmd
& c:/Votre/chemin/vers/leDossier/python.exe -m venv env
```

**Pour lancer l'environnement, exécutez la commande :**

```cmd
.\env\Script\activate
```

## Pour installer une bibliothèque dans l'environnement :

**Pour rechercher les dépendances de la bibliothèque :**

Ouvrez dans `WinPython` -> `WinPython Command Prompt`.

Tapez la commande : 
```cmd
pip show lib
```

Notez la `Version` et les `Requires`.

> [!NOTE]
> Si la commande `pip show` retourne :
> `WARNING: Package(s) not found: "la librairie"`,
> cela signifie soit que la librairie est une bibliothèque standard de Python qui
> n'a pas besoin d'être ajoutée, soit qu'elle n'est pas encore installée dans votre
> système. Dans ce dernier cas, vous devrez rechercher vous-même les dépendances et
> les versions compatibles avec votre installation.

**S'il y a des `Requires` :**

Recherchez le(s) dépendance(s) jusqu'à ce qu'il n'y en ait plus.

**S'il n'y a pas de `Requires` :**

Téléchargez depuis [L'index des paquets Python](https://pypi.org) la librairie,
choisissez la bonne `Version` dans l'onglet `Historique des versions` et
téléchargez _la librairie_ que vous ajouterez au dossier `bdd_lib`.

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
> Notez que des ressources en format `.svg` sont plus adaptées aux interfaces
> graphiques car elles sont en vectoriels donc redimensionnables.

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