#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  timetable-per-hour.py
#  
#  Copyright 2013 Christoph Fink <chri@stoph.at>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys,os,re,math

def average(v):
        return sum(v)*1.0/len(v)

def main():
	try:
		ligne=str(int(sys.argv[1]))
	except:
		try:
			ligne=str(sys.argv[i])
		except:
			print("You must specify the number/denominator of the line on the command line")
			exit(-2)
	try:
		frequencies={}
		for i in range(24):
			frequencies[i]=[]
		
		l=sys.stdin.readline()
		while l: 
			departures={}
			for i in range(24):
				departures[i]=[]
			for departure in l.split(','):
				m=re.search('(?P<hour>[0-9]{2})\.(?P<minutes>[0-9]{2})',departure)
				if m is not None:
					if len(m.groups())==2:
						departures[int(m.group("hour"))].append(int(m.group("minutes")))
			for i in range(24):
				frequencies[i].append(len(departures[i]))

			l=sys.stdin.readline()
		for i in range(24):
			frequencies[i]="%0.2f" % (average(frequencies[i]))
		frequencies=(' ').join(frequencies.values())
		print("freq_ligne%s = [ %s ]" %(ligne,frequencies))
		#print (',').join(frequencies)
	except:
		print("something weird happened with line no %d" %(ligne,))
		exit(-1)
	


if __name__ == '__main__':
	main()
