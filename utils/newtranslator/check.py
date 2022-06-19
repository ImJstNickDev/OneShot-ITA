#!/usr/bin/python

import sys
from os import system, name
from getch import pause, getch
from time import sleep
import polib

itpo = polib.pofile('it.po')
espo = polib.pofile('es.po')

itidlst = []
esidlst = []

for entry in itpo:
    itidlst.append(entry.msgid)
for entry in espo:
    esidlst.append(entry.msgid)

for entity in esidlst:
    if (entity not in itidlst):
        print("Entity from es.po: \"{}\" not found".format(entity))
        getch()