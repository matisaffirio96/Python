import sys
from PySide6 import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250,250)
wid.setWindowTitle('Nombre_Ventana')
wid.show()

sys.exit(app.exec_())