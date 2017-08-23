#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#
# com.py
#
# Copyright (C) 2010,2011,2012
# Lorenzo Carbonell Cerezo <lorenzo.carbonell.cerezo@gmail.com>
# Miguel Angel Santamaría Rogado <leibag@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#

import os
import sys
import shutil
import locale
import gettext

######################################

def is_package():
	return __file__.find('src') < 0

######################################


APPNAME = 'Slimbook Touchad'
APP = 'slimbooktouchpad'
APPCONF = APP + '_synaptics' + '.conf'


PARAMS = {
			'first-time':True,
			'version':'',
			'is_working':False,
			'autostart':False,
			'disable_on_typing':False,
			'seconds':2,
			'show_notifications':True,
			'touchpad_enabled':True,
			'natural_scrolling':False,
			'VertEdgeScroll':True,
			'HorizEdgeScroll':True,
			'CircularScrolling':True,
			'VertTwoFingerScroll':True,
			'HorizTwoFingerScroll':True,
			'TapButton1':1,
			'TapButton2':3,
			'TapButton3':0
			}

# check if running from source
STATUS_ICON = {}
if is_package():
	#ROOTDIR = '/home/slimbook/Escritorio/touchpad_excalibur/touchpad/'
	ROOTDIR = '/usr/share/slimbooktouchpad/'
	APPDIR = os.path.join(ROOTDIR, APP)
	IMAGESDIR = os.path.join(ROOTDIR, 'images')
	CHANGELOG = os.path.join(ROOTDIR,'changelog')
else:
	ROOTDIR = os.path.dirname(__file__)
	APPDIR = ROOTDIR
	IMAGESDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/images'))
	DEBIANDIR = os.path.normpath(os.path.join(ROOTDIR, '../debian'))
	CHANGELOG = os.path.join(ROOTDIR, 'changelog')


CONFIG_DIR = os.path.join(os.path.expanduser('~'),'.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
CONFIG_FILE = os.path.join(CONFIG_APP_DIR, APPCONF)

AUTOSTART_DIR = os.path.join(CONFIG_DIR,'autostart')
FILE_AUTO_START = os.path.join(AUTOSTART_DIR,'slimbooktouchpad-autostart.desktop')

f = open(CHANGELOG,'r')
line = f.readline()
f.close()
pos=line.find('(')
posf=line.find(')',pos)
VERSION = line[pos+1:posf].strip()
if is_package():
	VERSION = VERSION + '-src'
