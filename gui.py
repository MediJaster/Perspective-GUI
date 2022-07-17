from PyQt5 import QtWidgets
import sys, perspective

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.is_darkmode = False

        self.dark_theme = "/** QSS Qt Stylesheets Collection.* Created in 2013 by Khromathyon Software.* QSS Theme: Visual Studio(R) 2012 Dark Theme.* License: WTFPL*/QMainWindow {  background-color:#2d2d30;  color:#f1f1f1;}QMenuBar {  background-color:#2d2d30;  text-transform: uppercase;  color:#f1f1f1;}QMenuBar::item:selected{  background-color:#3e3e40;}QMenu {  border:0.5px solid #333337;  color:#f1f1f1;}QMenu::item:selected {  background-color:#2d2d30;  border-color:#333337;}QMenu::item {  background-color:#1b1b1c;  border-color:#333337;       padding: 2px 25px 2px 20px;}QMenu::separator{  background-color:#333337;  spacing:2px;}QTabBar::tab {  background-color:#2d2d30;  border: 1px solid transparent;  color:#f1f1f1;  padding:5px;}QTabBar::tab:hover{  background-color:#1c97ea;}QTabBar::tab:selected{  background-color:#007acc;}QTabWidget::pane {  border-top: 2px solid #007acc;  background-color:#2d2d30;}QDockWidget {    background: #2d2d30;    color:#f1f1f1;}QDockWidget::active {  border: 1px solid #007acc;}QDockWidget::title {  color:#f1f1f1;  background:#007acc;}QComboBox {  border-style:none;  background-color:#333337;  color:#b2b2b2;  border-style:none;}QComboBox:on {  background-color:#3f3f46;}QComboBox:down-arrow {  border-style:none;  border-left: 1px solid #007acc;}QComboBox:drop-down {  border-style:none;}/*Needs fix*/QScrollBar{  background:#3e3e42;  border-style:none;}QScrollbar::horizontal{     height: 15px;     margin: 0px 20px 0 20px;}QScrollBar:handle {  border-style:none;  background:#9d9d9d;  margin: inherited;}QPushButton {  border-style:none;  border-bottom:1px solid #007acc;  color:#f1f1f1;  background:#3e3e42;  padding:5px;}QPushButton::pressed {  border: 1px solid #007acc;  background:#3e3e42;}QToolButton {  border-style:none;  background:#2d2d30;  color:#f1f1f1;}QToolButton:pressed {  border: 1px solid #007acc;  background:#3e3e42;}QLabel {  color:#f1f1f1;}QLineEdit {  border: 1px solid #3e3e42;  background-color:#3f3f46;  color:#b2b2b2;  selection-background-color:#1c97ea;}QLineEdit:selected {  border-color:#007acc;}QToolBar {  background:#2d2d30;  border-style:none;}QToolBox{  background:#2d2d30;}QToolBox::tab{  background:#2d2d30;  color:#f1f1f1;  border-style:none;  border-bottom-style: solid;  border-bottom: 2px solid #007acc;}QToolBox::tab:selected {  border:1px solid #007acc;}QWidget{  background:#2d2d30;  color:#f1f1f1;}QTreeView {  background-color:#2d2d30;  border-style:none;}QTreeView::item:selected{  background:#007acc;}QTreeView::item:selected!active {  background: #3f3f46;}QTreeView::item:selected {  background: #3f3f46;}QListView {  background-color:#252526;  border-style:none;}"

        self.setGeometry(200,200,400,360)
        self.setWindowTitle("ASS Perspective Tool")
        self.setStyleSheet("")
        self.initUI()

    def switch_color_mode(self):
        if self.is_darkmode:
            self.setStyleSheet("")
            self.darkmode_checkmark.setText("Dark Mode")
            self.is_darkmode = False
        else:
            self.setStyleSheet(self.dark_theme)
            self.darkmode_checkmark.setText("Light Mode")
            self.is_darkmode = True

    def initUI(self):
        
        # Dark Mode Toggle

        self.darkmode_checkmark = QtWidgets.QPushButton(self)
        self.darkmode_checkmark.setGeometry(310,10,75,30)
        self.darkmode_checkmark.setText("Dark Mode")
        self.darkmode_checkmark.clicked.connect(self.switch_color_mode)

        # Coords Input

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Tetragon Data")
        self.label.setGeometry(20,10,90,30)

        self.coords_input = QtWidgets.QTextEdit(self)
        self.coords_input.setGeometry(20,50,360,30)

        # Origin Input

        self.origin_checkmark = QtWidgets.QCheckBox(self)
        self.origin_checkmark.setGeometry(20,100,50,30)
        self.origin_checkmark.setText("Origin")

        self.origin_input = QtWidgets.QTextEdit(self)
        self.origin_input.setGeometry(110,100,270,30)

        # Ratio Input

        self.ratio_checkmark = QtWidgets.QCheckBox(self)
        self.ratio_checkmark.setGeometry(20,140,50,30)
        self.ratio_checkmark.setText("Ratio")

        self.ratio_input = QtWidgets.QTextEdit(self)
        self.ratio_input.setGeometry(110,140,270,30)

        # Scale Input

        self.scale_checkmark = QtWidgets.QCheckBox(self)
        self.scale_checkmark.setGeometry(20,180,50,30)
        self.scale_checkmark.setText("Scale")

        self.scale_input = QtWidgets.QTextEdit(self)
        self.scale_input.setGeometry(110,180,270,30)

        # Result Output

        self.result_text = QtWidgets.QTextBrowser(self)
        self.result_text.setGeometry(20,240,255,100)
        
        self.calc_button = QtWidgets.QPushButton(self)
        self.calc_button.setText("Calculate")
        self.calc_button.setGeometry(300,240,80,100)
        self.calc_button.clicked.connect(self.calculate_perspective)

    def parse_inputs(self):
        coords = "<" + self.coords_input.toPlainText() + ">"
        origin = ""
        ratio = ""
        scale = 1

        if self.origin_checkmark.isChecked():
            try:
                origin = int(self.origin_input.toPlainText())
            except ValueError:
                origin = ""

        if self.ratio_checkmark.isChecked():
            try:
                ratio = int(self.ratio_input.toPlainText())
            except ValueError:
                ratio = ""

        if self.scale_checkmark.isChecked():
            try:
                scale = int(self.scale_input.toPlainText())
            except ValueError:
                scale = 1
        
        return {
            "coord" : coords,
            "origin" : origin,
            "ratio" : ratio,
            "scale" : scale
        }


    def calculate_perspective(self):
        self.result_text.setText(perspective.get_perspective(self.parse_inputs()))
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
