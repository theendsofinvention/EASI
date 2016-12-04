# coding=utf-8

# noinspection PyUnresolvedReferences
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal, pyqtSlot, QAbstractItemModel, QAbstractListModel, QVariant, \
    QEvent, QPoint, QRect, QLine, QRegExp, QAbstractTableModel, QModelIndex, QSortFilterProxyModel, QSize, pyqtProperty,\
    QTimer
# noinspection PyUnresolvedReferences
from PyQt5.QtGui import QIcon, QPixmap, QFont, QBrush, QPainter, QPen, QRegExpValidator, QStandardItemModel, QColor,\
    QStandardItem, QCursor
# noinspection PyUnresolvedReferences
from PyQt5.QtWidgets import QMainWindow, QSplashScreen, QLabel, QProgressBar, QDialog, QApplication, QStyleFactory, \
    QComboBox, QAction, QMenu, QFileDialog, QDialogButtonBox, QLineEdit, QToolTip, QToolButton, QWidget, \
    QGraphicsDropShadowEffect, QStylePainter, QFormLayout, QTextBrowser, QWizardPage, QVBoxLayout, QWizard,\
    QPushButton, QTableView, QHBoxLayout, QFileSystemModel, QTreeWidgetItem, QHeaderView, QSpacerItem, QSizePolicy,\
    QTextEdit, QItemDelegate, QStyleOptionViewItem, QBoxLayout

from . import qt_resources

dialog_default_flags = flags=Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint
