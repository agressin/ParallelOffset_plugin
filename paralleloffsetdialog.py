# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParallelOffsetDialog
                                 A QGIS plugin
 Creates a parallell line at a given distance
                             -------------------
        begin                : 2013-07-23
        copyright            : (C) 2013 by City and County of Swansea
        email                : steven.gardiner@swansea.gov.uk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic,QtCore, QtGui,QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui_paralleloffset.ui'))

# create the dialog for zoom to point


class ParallelOffsetDialog(QtWidgets.QDialog,FORM_CLASS):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
