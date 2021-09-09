#!/usr/bin/env python3


infile1 = open("before.txt", "r")
infile2 = open("after.txt",  "r")
outfile = open("Output.txt", "w")



def findWriteNum(infile):
	for line in infile:
		curLine=line.split(":")
		if (curLine[0]=="data_units_written			"):
			writeNum =int(curLine[1].replace('\n','').replace(',', ''))
			print("writeNum=", writeNum)
			return writeNum
	return -1
			
	
before=findWriteNum(infile1)
after=findWriteNum(infile2)
if (before==-1 or after==-1):
	print("Error")
else:
	delta=(after-before)/2.0
	print(delta, "KB")
	printLine="delta="+ str(delta)+"KB"
	outfile.write(printLine)
	
infile1.close()
infile2.close()
outfile.close()