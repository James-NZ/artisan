"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup-mac35.py py2app
"""

# manually remove sample-data mpl subdirectory from Python installation:
# sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/matplotlib/mpl-data/sample_data

from distutils import sysconfig
their_parse_makefile = sysconfig.parse_makefile
def my_parse_makefile(filename, g):
    their_parse_makefile(filename, g)
    g['MACOSX_DEPLOYMENT_TARGET'] = '10.7'
sysconfig.parse_makefile = my_parse_makefile

import sys, os
from setuptools import setup

import string
from plistlib import Plist

import artisanlib

# current version of Artisan
VERSION = artisanlib.__version__
LICENSE = 'GNU General Public License (GPL)'

try:
    QTDIR = os.environ["QT_PATH"] + r'/'
except:
    QTDIR = r'/Users/luther/Qt5.7.1/5.7/clang_64/' # qt5

APP = ['artisan.py']

DATA_FILES = [
    "LICENSE.txt",
    ("../Resources/qt_plugins/iconengines", [QTDIR + r'/plugins/iconengines/libqsvgicon.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqdds.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqgif.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqicns.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqico.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqjp2.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqjpeg.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqmacjp2.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqmng.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqsvg.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqtga.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqtiff.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqwbmp.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqwebp.dylib']),
    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqcocoa.dylib']), # qt5
#    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqoffscreen.dylib']), # qt5
#    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqminimal.dylib']), # qt5
    ("../Resources/qt_plugins/printsupport", [QTDIR + r'/plugins/printsupport/libcocoaprintersupport.dylib']), # qt5/# standard     
# standard QT translation needed to get the Application menu bar and 
# the standard dialog elements translated
    ("../translations", [QTDIR + r'/translations/qt_ar.qm']),
    ("../translations", [QTDIR + r'/translations/qt_de.qm']),
    ("../translations", [QTDIR + r'/translations/qt_es.qm']),
    ("../translations", [QTDIR + r'/translations/qt_fi.qm']),
    ("../translations", [QTDIR + r'/translations/qt_fr.qm']),
    ("../translations", [QTDIR + r'/translations/qt_he.qm']),
    ("../translations", [QTDIR + r'/translations/qt_hu.qm']),
    ("../translations", [QTDIR + r'/translations/qt_it.qm']),
    ("../translations", [QTDIR + r'/translations/qt_ja.qm']),
    ("../translations", [QTDIR + r'/translations/qt_ko.qm']),
    ("../translations", [QTDIR + r'/translations/qt_pt.qm']),
    ("../translations", [QTDIR + r'/translations/qt_pl.qm']),
    ("../translations", [QTDIR + r'/translations/qt_ru.qm']),
    ("../translations", [QTDIR + r'/translations/qt_sv.qm']),
    ("../translations", [QTDIR + r'/translations/qt_zh_CN.qm']),
    ("../translations", [QTDIR + r'/translations/qt_zh_TW.qm']),
    ("../translations", [r'translations/artisan_ar.qm']), 
    ("../translations", [r"translations/artisan_de.qm"]),
    ("../translations", [r"translations/artisan_es.qm"]),
    ("../translations", [r"translations/artisan_fi.qm"]),
    ("../translations", [r"translations/artisan_fr.qm"]),
    ("../translations", [r"translations/artisan_he.qm"]),
    ("../translations", [r"translations/artisan_hu.qm"]),   
    ("../translations", [r"translations/artisan_it.qm"]),
    ("../translations", [r"translations/artisan_ja.qm"]),
    ("../translations", [r'translations/artisan_ko.qm']),
    ("../translations", [r'translations/artisan_pt.qm']),
    ("../translations", [r'translations/artisan_pl.qm']),
    ("../translations", [r'translations/artisan_ru.qm']),
    ("../translations", [r"translations/artisan_sv.qm"]),
    ("../translations", [r'translations/artisan_zh_CN.qm']),
    ("../translations", [r'translations/artisan_zh_TW.qm']),
    ("../translations", [r"translations/artisan_el.qm"]),
    ("../translations", [r"translations/artisan_no.qm"]),
    ("../translations", [r"translations/artisan_nl.qm"]),
    ("../translations", [r"translations/artisan_tr.qm"]),
    ("../translations", [r"translations/artisan_th.qm"]),
    ("../translations", [r"translations/artisan_id.qm"]),
    ("../Resources", [r"qt.conf"]),
    ("../Resources", [r"artisanProfile.icns"]),
    ("../Resources", [r"artisanAlarms.icns"]),
    ("../Resources", [r"artisanPalettes.icns"]),
    ("../Resources", [r"artisanSettings.icns"]),
    ("../Resources", [r"artisanWheel.icns"]),
    ("../Resources", [r"includes/alarmclock.eot"]),
    ("../Resources", [r"includes/alarmclock.svg"]),
    ("../Resources", [r"includes/alarmclock.ttf"]),
    ("../Resources", [r"includes/alarmclock.woff"]),
    ("../Resources", [r"includes/artisan.tpl"]),
    ("../Resources", [r"includes/bigtext.js"]),
    ("../Resources", [r"includes/sorttable.js"]),
    ("../Resources", [r"includes/report-template.htm"]),
    ("../Resources", [r"includes/roast-template.htm"]),
    ("../Resources", [r"includes/ranking-template.htm"]),
    ("../Resources", [r"includes/Humor-Sans.ttf"]),
    ("../Resources", [r"includes/jquery-1.11.1.min.js"]),
  ]
  
plist = Plist.fromFile('Info.plist')
plist.update({ 'CFBundleDisplayName': 'Artisan',
                    'CFBundleGetInfoString': 'Artisan, Roast Logger',
                    'CFBundleIdentifier': 'com.google.code.p.Artisan',
                    'CFBundleShortVersionString': VERSION,
                    'CFBundleVersion': 'Artisan ' + VERSION,
                    'LSMinimumSystemVersion': '10.7',
                    'LSMultipleInstancesProhibited': 'false',
                    'LSPrefersPPC': False,
                    'LSArchitecturePriority': 'x86_64',
                    'NSHumanReadableCopyright': LICENSE,
                    'NSHighResolutionCapable': True,
                })
  
OPTIONS = {
    'strip':True,
    'argv_emulation': False, # this would confuses GUI processing
# this does not work on Python3.4/PyQt5 for unknown reasons
#    'qt_plugins': [
#                    'iconengines/libqsvgicon.dylib',
#                    'imageformats/libqsvg.dylib',
#                    'imageformats/libqjpeg.dylib',
#                    'imageformats/libqgif.dylib',
#                    'imageformats/libqtiff.dylib',
#                    'platforms/libqcocoa.dylib',  # qt5
#                    'platforms/libqminimal.dylib',  # qt5
#                    'platforms/libqoffscreen.dylib'],  # qt5
    'semi_standalone': False,
    'site_packages': True,
    'dylib_excludes': ['phonon','QtDeclarative','QtDesigner',
                    'QtHelp','QtMultimedia','QtNetwork',
                    'QtOpenGL','QtScript','QtScriptTools',
                    'QtSql','QtTest','QtXmlPatterns','QtWebKit'],
    'packages': ['yoctopuce','gevent'],
    'optimize':  2,
    'compressed': True,
    'iconfile': 'artisan.icns',
    'arch': 'x86_64',
    'matplotlib_backends': '-', # '-' for imported or explicit 'qt4agg'
    'includes': ['serial',
                 'PyQt5',
                 'PyQt5.QtCore',
                 'PyQt5.QtGui',
                 'PyQt5.QtWidgets',
                 'PyQt5.QtSvg',
                 'PyQt5.QtXml',
                 'PyQt5.QtDBus',
                 'PyQt5.QtPrintSupport'
                 ],
    'excludes' :  ['_tkagg','_ps','_fltkagg','Tkinter','Tkconstants',
                      '_agg','_cairo','_gtk','gtkcairo','pydoc','sqlite3',
                      'bsddb','curses','tcl',
                      '_wxagg','_gtagg','_cocoaagg','_wx'],
    'plist'    : plist}

setup(
    name='Artisan',
    version=VERSION,
    author='YOUcouldbeTOO',
    author_email='zaub.ERASE.org@yahoo.com',
    license=LICENSE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

            
os.system(r'cp README.txt dist')
os.system(r'cp LICENSE.txt dist')
os.system(r'mkdir dist/Wheels')
os.system(r'mkdir dist/Wheels/Cupping')
os.system(r'mkdir dist/Wheels/Other')
os.system(r'mkdir dist/Wheels/Roasting')
os.system(r'cp Wheels/Cupping/* dist/Wheels/Cupping')
os.system(r'cp Wheels/Other/* dist/Wheels/Other')
os.system(r'cp Wheels/Roasting/* dist/Wheels/Roasting')
os.chdir('./dist')

# (independent) matplotlib (installed via pip) shared libs are not copied by py2app (both cp are needed!)
os.system(r'mkdir Artisan.app/Contents/Resources/lib/python3.5/lib-dynload/matplotlib/.dylibs')
os.system(r'cp -R /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Resources/lib/python3.5/lib-dynload/matplotlib/.dylibs')
os.system(r'cp /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Frameworks')
#
# temporary commented:

## for Qt5
#print('*** Removing unused Qt frameworks ***')
#for fw in [
#            'QtDeclarative.framework',
#            'QtHelp.framework',
#            'QtMultimedia.framework',
#            'QtNetwork.framework',
#            'QtOpenGL.framework',
#            'QtScript.framework',
#            'QtScriptTools.framework',
#            'QtSql.framework',
#            'QtDesigner.framework',
#            'QtTest.framework',
#            'QtWebKit.framework',
#            'QtWebKitWidgets.framework',
#            'QtXMLPatterns.framework',
#            'QtCLucene.framework',
#            'QtPositioning.framework',
#            'QtQml.framework',
#            'QtSensors.framework',
#            'QtWebChannel.framework',
#            'QtQuick.framework',
#            'QtMultimediaWidgets.framework',]:
#    for root,dirs,files in os.walk('./Artisan.app/Contents/Frameworks/' + fw):
#        for file in files:
##            print('Deleting', file)
#            os.remove(os.path.join(root,file))

print('*** Removing unused files ***')
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'debug' in file:
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.startswith('test_'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif '_tests' in file:
#            print('Deleting', file)            
            os.remove(os.path.join(root,file))               
        elif file.endswith('.pyc') and file != "site.pyc" and os.path.isfile(os.path.join(root,file[:-3] + 'pyo')):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        # remove also all .h .in .cpp .cc .html files 
        elif file.endswith('.h') and file != "pyconfig.h":
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.in'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cpp'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cc'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
# .afm files should not be removed as without matplotlib will fail on startup            
#        elif file.endswith('.afm'):
#            print('Deleting', file)
#            os.remove(os.path.join(root,file))
    # remove test files        
    for dir in dirs:
        if 'tests' in dir:
            for r,d,f in os.walk(os.path.join(root,dir)):
                for fl in f:
#                    print('Deleting', os.path.join(r,fl))
                    os.remove(os.path.join(r,fl))                
            
os.chdir('..')
os.system(r"rm artisan-mac-" + VERSION + r".dmg")
os.system(r'hdiutil create artisan-mac-' + VERSION + r'.dmg -volname "Artisan" -fs HFS+ -srcfolder "dist"')
# otool -L dist/Artisan.app/Contents/MacOS/Artisan

