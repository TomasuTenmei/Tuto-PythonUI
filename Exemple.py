import sys, os, traceback

from PySide6.QtWidgets import QMainWindow, QApplication
#from PySide6.QtGui import QPainter, Qt
from PySide6.QtCore import QThreadPool, Slot, Signal, QObject, QRunnable
#from PySide6.QtCharts import QChart, QChartView, QValueAxis

from ui_mainwindow import Ui_MainWindow

# Threads
class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):

        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        try:

            result = self.fn(*self.args, **self.kwargs)

        except:

            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:

            self.signals.result.emit(result)

        finally:

            self.signals.finished.emit()

# Main
class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connection des objets aux fonctions
        #self.ui.lineEdit_Addr.textChanged.connect(self.readAddr)
        #self.ui.pushButton_Connect.clicked.connect(self.connectScope)

        # Création du graphique
        #self.chart = QChart()

        # Création des Axes
        #self.axisX = QValueAxis()
        #self.axisY = QValueAxis()
        #self.axisX.setLabelFormat("%.1E s")
        #self.axisY.setLabelFormat("%.1E V")

        # Ajout des axes au graph
        #self.chart.addAxis(self.axisX, Qt.AlignBottom)
        #self.chart.addAxis(self.axisY, Qt.AlignLeft)

        # Affichage graph
        #self.chartView = QChartView(self.chart)
        #self.chartView.setRenderHint(QPainter.Antialiasing)
        #self.ui.gridLayout_Visual.addWidget(self.chartView, 1, 1, 1, 1)

        # Threadpool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    # Gestion Thread
    def progress_fn(self, n):

        # Code qui s'execute entre le thead par retour de progress_callback
        # Permet par exemple d'actualiser une progress bar
        pass

    def print_output(self, s):

        # Retour du thread d'une variable si besoin
        pass

    def thread_complete(self):

        # Execution à la fin d'un thread
        print('End thread')

    def exec_thread(self, fn):

        worker = Worker(fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    # Fonctions
    def hello(self):

        print("Hello, World!")

        # Lance dans la pool de thread la fonction choisie
        self.exec_thread(self.hello)


# Affichage du GUI
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Permet de choisir le style de l'interface
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())