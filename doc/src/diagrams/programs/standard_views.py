#!/usr/bin/env python
#############################################################################
##
## Copyright (C) 2015 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the documentation of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:LGPL21$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see http://www.qt.io/terms-conditions. For further
## information use the contact form at http://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 or version 3 as published by the Free
## Software Foundation and appearing in the file LICENSE.LGPLv21 and
## LICENSE.LGPLv3 included in the packaging of this file. Please review the
## following information to ensure the GNU Lesser General Public License
## requirements will be met: https://www.gnu.org/licenses/lgpl.html and
## http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## As a special exception, The Qt Company gives you certain additional
## rights. These rights are described in The Qt Company LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## $QT_END_LICENSE$
##
#############################################################################

import sys
from PyQt4.QtCore import QDir, Qt
from PyQt4.QtGui import *

app = QApplication(sys.argv)

background = QWidget()
palette = QPalette()
palette.setColor(QPalette.Window, QColor(Qt.white))
background.setPalette(palette)

model = QFileSystemModel()
model.setRootPath(QDir.currentPath())

treeView = QTreeView(background)
treeView.setModel(model)
treeView.setRootIndex(model.index(QDir.currentPath()))

listView = QListView(background)
listView.setModel(model)
listView.setRootIndex(model.index(QDir.currentPath()))

tableView = QTableView(background)
tableView.setModel(model)
tableView.setRootIndex(model.index(QDir.currentPath()))

selection = QItemSelectionModel(model)
treeView.setSelectionModel(selection)
listView.setSelectionModel(selection)
tableView.setSelectionModel(selection)

layout = QHBoxLayout(background)
layout.addWidget(listView)
layout.addSpacing(24)
layout.addWidget(treeView, 1)
layout.addSpacing(24)
layout.addWidget(tableView)
background.show()

sys.exit(app.exec_())
