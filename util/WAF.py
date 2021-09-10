#!/usr/bin/env python3


# open files
configFile = open("Config.txt", "r")
beforeFile = open("SMART-Before.txt", "r")
afterFile  = open("SMART-After.txt",  "r")
resultFile = open("Output.txt", "w")

		
		
def getLogicalWriteAmount(infile):
	key=0
	value=0
	thread=0
	num=0
	strList=[]
	for line in infile:
		curLineStrings=line.split(" ")
		#print(curLineStrings)
		for string in curLineStrings:
			if ("--key_size" in string):
				#print(string)
				key=int(string.split("=")[1])
				#print(key)
			if ("--value_size" in string):
				#print(string)
				value=int(string.split("=")[1])
				#print(value)			
			if ("--threads" in string):
				#print(string)
				thread=int(string.split("=")[1])
				#print(thread)
			if ("--num=" in string):
				#print(string)
				num=int(string.split("=")[1])
				#print(num)
	if ((key+value)*thread*num>0):
		return (key+value)*thread*num/1024.0
	else:
		return -1
	


def getPhysicalWriteAmount(infile):
	for line in infile:
		curLine=line.split(":")
		if (curLine[0]=="data_units_written			"):
			writeNum =int(curLine[1].replace('\n','').replace(',', ''))
			print(writeNum/2.0)
			return writeNum/2.0
	return -1
			

	
# main process

# get logical write amount in KB
logWriteAmount=getLogicalWriteAmount(configFile)

# get physical write amount in KB
writeCountBefore=getPhysicalWriteAmount(beforeFile)
writeCountAfter =getPhysicalWriteAmount(afterFile)

if (writeCountBefore==-1 or writeCountAfter==-1):
	print("Error")
	exit()
else:
	delta=writeCountAfter-writeCountBefore # *512KB
	if(logWriteAmount==0):
		WAF=0
	else:
		WAF=delta/logWriteAmount
	printLine="logWrite="+str(logWriteAmount)+"KB, phyWrite="+ str(delta) + "KB, WAF=" + str(WAF)
	print(printLine)
	resultFile.write(printLine)


# close files
configFile.close()
beforeFile.close()
afterFile.close()
resultFile.close()