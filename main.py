from PyQt5 import QtWidgets # import PyQt5 widgets
import sys

# Create the application object
app = QtWidgets.QApplication(sys.argv)

# Create the form object
first_window = QtWidgets.QWidget()

# Set window size
first_window.resize(400, 340)

# Set the form title
first_window.setWindowTitle("The second pyqt program")

# Show form
first_window.show()

# Run the program
sys.exit(app.exec())