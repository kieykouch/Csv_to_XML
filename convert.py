import csv
import os
import sys

def main(CSV):

    XML = CSV[:len(CSV)-3]+'xml'

    CSVData = csv.reader(open(CSV))
    XMLData = open(XML, 'w')
    XMLData.write('<?xml version="1.0"?>' + "\n")
    XMLData.write('<colleges>' + "\n")

    firstTime = True
    Header = []

    for row in CSVData:
        if firstTime:
            tags = row
            for i in row:
                Header.append(i.replace(' ', '_'))
            firstTime = False
        else: 
            XMLData.write('<college>' + "\n")
            for i in range(len(row)):
                text = '\t' + '<' + Header[i] + '>' + row[i] + '</' + Header[i] + '>' + "\n"
                XMLData.write(text)
            XMLData.write('</college>' + "\n")

    XMLData.write('</colleges>' + "\n")
    XMLData.close()

if __name__ == '__main__' and len(sys.argv) == 2:
    print ("Converting CSV file "+ str(sys.argv[1]))
    main(sys.argv[1])