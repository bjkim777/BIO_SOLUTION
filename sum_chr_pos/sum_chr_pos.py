import os
import sys
import subprocess
import tempfile
import argparse

def getOpts():
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('-b', '--bed', type=str, required=True,  metavar= '<bed>', help= 'bed file')
	argv = parser.parse_args()
	return(argv)

def sumChrPos(BED):
	SUM={}
	
	with open(BED, 'r') as f:
		for line in f.readlines():
			col=line.strip().split('\t')
			
			chr=col[0]
			start=col[1]
			end=col[2]

			if str(chr) in SUM:
				SUM[str(chr)]+=int(end)-int(start)+1
			else:
				SUM[str(chr)]=int(end)-int(start)+1

	for key in SUM.keys():
		print (str(key) + '\t' + str(SUM[str(key)]))

### MAIN ###
def main (bed):
	sumChrPos(bed)

### ACTION ### 
if __name__ == "__main__":
	argv = getOpts()

	main(argv.bed)
	sys.exit(0)
