#!/bin/python2
import os
from scipy import misc
from sets import Set
import csv
import pickle



def createUniqueList(data, filename):
  """Creates a unique table of colors from bmp image"""
  # create a set
  newProvSet = Set()
  counter = 0
  for x in range(0,X):
    for y in range(0,Y):
      color = tuple(data[x,y,:])
      newProvSet.add(color)
      # increase counter
      if (counter < len(newProvSet)):
        counter = counter + 1
        print(counter)

  with open(filename, 'wb') as f: 
    pickle.dump(newProvSet, f)

  return

# Cretes subfile of definitions csv with only come colors
def createSubDefCSV(colors, filename, outfile):
  def_csv = open(filename, 'rb')
  bare_file = csv.reader(def_csv, delimiter=';')
  newList = []

  n = 0
  for row in bare_file:
    if (n == 0):
      n=1
    else:
      color = tuple([int(row[1]), int(row[2]), int(row[3])] )
      if (color in colors):
        entry = [n] + list(color) + row[4:6]
        newList.append(entry)
        n=n+1
        
  # list created time to crate proper csv
  fieldnames = ['province', 'red', 'green', 'blue', 'x', 'x']
  with open(outfile, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ';')
    writer.writerow(fieldnames) 
    for x in newList:
      writer.writerow(x)


# update adjacencies basing on 
def updateAdj():
  adjIn = 'adjacencies.csv'
  adjOut = 'adjacenciesNEW.csv'
  filename = 'definitionNEW.csv'
  # create id list
  with open(filename, 'rb') as csvSrc:
    base = csv.reader(csvSrc, delimiter=';')
    idList = Set()
    n = 0
    for row in base:
      if (n != 0):
        idList.add(int(row[0]))
      n = 1

  with open(adjIn, 'rb') as csvAdj:
    out = open(adjOut, 'wb')
    base = csv.reader(csvAdj, delimiter=';')
    csvOut = csv.writer(out, delimiter=';')
    # check from and To
    first = True
    for row in base:
      if ( first == False):
        idFrom = int(row[0])
        idTo = int(row[1])
        if(idFrom in idList or idTo in idList):
          print "yes"
          csvOut.writerow(row)
        else:
          print "not"
      else:
        first = False 
        csvOut.writerow(row)



#
# Main function fixes the csv file that mapfiller tool uses
# for generation
#
def fixTheCSV(colors):
  fin = 'provinceDef.csv'
  fout= 'provinceDefOUT.csv'
  with open(fin, 'rb') as csvIN:
    indata = csv.reader(csvIN, delimiter=';')
    csvOUT =  open(fout, 'wb')
    outdata = csv.writer(csvOUT, delimiter=';')
    n = 0
    for row in indata:
      if (n == 0):
        outdata.writerow(row)
      else:
        color = tuple([int(row[2]), int(row[3]), int(row[4])])
        if (color in colors):
          print('jest')
          outdata.writerow(row)
        else: 
          print('brak')
      n = n+1
      
