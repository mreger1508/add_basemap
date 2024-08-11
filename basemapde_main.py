from PyQt5.QtWidgets import *
from qgis.core import *
from PyQt5.QtGui import QIcon

class basemapde:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.toolbar = QToolBar("Basemap.de Toolbar")
        self.iface.addToolBar(self.toolbar)

        # Laden des Symbols für die Aktion
        icon_path = '/Users/martinreger/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/addBasemap/logo.png'  # Passe den Pfad zum Logo an
        icon = QIcon(icon_path)

        # Aktion zum Hinzufügen des Basemap.de
        self.addBasemapAction = QAction(icon, 'Add Basemap.de', self.iface.mainWindow())
        self.addBasemapAction.triggered.connect(self.addBasemapDE)
        self.toolbar.addAction(self.addBasemapAction)

    def unload(self):
        self.iface.mainWindow().removeToolBar(self.toolbar)

    def addBasemapDE(self):
        uri = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=de_basemapde_web_raster_grau&styles&tilePixelRatio=0&url=https://basemap.de/dienste/wms_capabilities_web_raster.xml'
        lyr = QgsRasterLayer(uri, 'Basemap.de', 'wms')
        QgsProject.instance().addMapLayer(lyr)

"""
    def initGui(self):
        self.startButton = QAction('Add Basemap.de', self.iface.mainWindow())
        self.iface.addPluginToMenu('Basemap.de', self.startButton)
        self.startButton.triggered.connect(self.addBasemapDE)

    def unload(self):
        self.iface.removePluginMenu('Basemap.de', self.startButton)
"""
        
    