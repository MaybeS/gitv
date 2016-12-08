#-*- coding: utf-8 -*-
from argparse import ArgumentParser
from commands import getstatusoutput as getout

parser = ArgumentParser(description='Process')
parser.add_argument('command', metavar='command', type=str, help='command to execute')
parser.add_argument('file_pattern', type=str, help='file pattern to find') 
parser.add_argument('grep_pattern', type=str, help='pattern to grep with') 

def printf(file, index, line):
	print file +':' +index+':' + line

def findgrep(command='findgrep', file_pattern='', grep_pattern=''):
	print 'searching ' + grep_pattern + ' in ' + file_pattern + ' ...'
	files = getout('git ls-files ' + getout('git rev-parse --show-toplevel')[1])[1].split('\n')
	files = [ file for file in files if file_pattern in file ]
	lines = [ printf(file, str(index + 1), line.rstrip('\n').lstrip())  for file in files for index, line in enumerate(open(file)) if grep_pattern.lower() in line.lower() ]	

commands = {'findgrep': findgrep}
args = parser.parse_args()

if __name__ == '__main__':
	if args.command:
		command = commands[args.command]
		command(**vars(args))
	else:
		print 'input command'
else:
	print 'must run itself!'
