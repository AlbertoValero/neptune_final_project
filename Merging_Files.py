#!/usr/bin/env python

for Line in InFile:
	Line = Line.strip()
​
	if LineNumber > 0:
		ElementList = Line.split( '\t' )
		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )
​
		latitude = decimalat( ElementList[ 2 ] )
​
	
	LineNumber = LineNumber + 1
​
print ( Line )

InFile.close()