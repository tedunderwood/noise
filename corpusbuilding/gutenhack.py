#!/usr/bin/env python3

# gutenhack.py

# Extracts an author-title database from
# a human-readable file produced by
# Project Gutenberg.

import os

firstline = 'TITLE and AUTHOR'
started = False
ctr = 0

def getdigits(astring):
	numericpart = ''
	for i in range(-1, -10, -1):
		if astring[i].isdigit():
			numericpart = astring[i] + numericpart
		else:
			break

	astring = astring.replace(numericpart, '').strip()
	number = int(numericpart)

	return astring, number

outlines = []

with open('/Users/tunder/gutenberg/GUTINDEX.txt') as f:
	for line in f:

		found = len(outlines)
		if found % 100 == 1:
			print(found)

		line = line.strip()

		if line.startswith('TITLE and AUTHOR'):
			started = True
		elif ctr > 15:
			break
		elif started:
			if len(line) < 2:
				continue
			elif not(line[-1]).isdigit():
				ctr += 1
				# print(line)
				continue
			else:
				ctr = 0
				line, number = getdigits(line)

				if ', by' not in line:
					continue
				else:
					parts = line.split(', by')
					if len(parts) == 2:
						title = parts[0]
						author = parts[1]
					else:
						continue

					authnames = author.split()
					if len(authnames) > 1:
						author = authnames[-1] + ', ' + ' '.join(authnames[0:-1])
						title = title.replace('\t', ' ')
						outlines.append(title + '\t' + author + '\t' + str(number) + '\n')

with open('gutendata.tsv', mode = 'w') as f:
	f.write('title\tauthor\tebooknum\n')
	for l in outlines:
		f.write(l)



