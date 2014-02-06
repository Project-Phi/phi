#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import Template
from datetime import date
import os

# relase dir
relase_dir="../../../build-bitcoin-qt-Desktop_Qt_5_2_0_clang_64bit-Release/"
#Mac Deploy Tool for dep.
mac_dep="/Users/kral/Qt5.2.0/5.2.0/clang_64/bin/macdeployqt"


# Open MMc info.plist
File    = relase_dir+"Phicoin-Qt.app/Contents/Info.plist"
version    = "unknown";
# Read Qt config File grab version
fileForGrabbingVersion = "../../bitcoin-qt.pro"
for line in open(fileForGrabbingVersion):
        lineArr = line.replace(" ", "").split("=");
        if lineArr[0].startswith("VERSION"):
                version = lineArr[1].replace("\n", "");

fIn = open(File, "r")
fileContent = fIn.read()
s = Template(fileContent)
#Change VERSION and YEAR
newFileContent = s.substitute(VERSION=version,YEAR=date.today().year)
# Save new config
fo = open(File, "w")
fo.write(newFileContent);

print "Info.plist reload"


# Mac Deploy
#os.system(mac_dep+' '+relase_dir+'Phicoin-Qt.app -verbose=3')



#otool -l ../../../build-bitcoin-qt-Desktop_Qt_5_2_0_clang_64bit-Release/Phicoin-Qt.app/Contents/MacOS/Phicoin-Qt

#/Users/kral/Qt5.2.0/5.2.0/clang_64/bin/macdeployqt ../../../build-bitcoin-qt-Desktop_Qt_5_2_0_clang_64bit-Release/Phicoin-Qt.app
