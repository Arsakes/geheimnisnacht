#!/bin/python2
from lib import *


colors = pickle.load(open('uniqueList', 'rb'))
#createSubDefCSV(colors, 'definition.csv', 'definitionNEW.csv')

fixTheCSV(colors)

