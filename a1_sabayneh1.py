#!/usr/bin/env python3
'''PS435 Assignment 1 - Winter 2020
Program: a1_sabayneh1.py
Author: "Samnder Abayneh"
The python code in this file (a1_sabayneh1.py) is original work written by
"Samnder Abayneh". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import os
import sys
#function that accepts no argument and returns usage of this script
def usage():
	if ((len(sys.argv) != 3) and len(sys.argv) != 4): 
		print (sys.argv[0] + ' --step(optional) YYYY-MM-DD num(days to add or substract)')
		exit()
def leap_year(year):
    
#This function will check if it is a leap year based on the year given. It will return true if it is and false if it isn't.

	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 ==0):
				resultofleapyear = True
			else:
				resultofleapyear = False
		else:
			resultofleapyear = True
	else:
		resultofleapyear = False
            
	return resultofleapyear
 
def days_in_mon(year):
	if leap_year(year):
		feb = 29
	else:
		feb = 28

	maxmonth = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return maxmonth

def valid_date(date):
	if (len(date) != 10):
		print("Error: wrong date entered")
		exit()
	else:
		year = int(date[0:4])
		month = int(date[5:7])
		day = int(date[8:])
		maxmonth = days_in_mon(year)

		if month not in maxmonth.keys():
			print("Error: wrong month entered")
			exit()
		else:
			maxday = maxmonth[month]
			if day not in range (1,maxday+1):    
				print("Error: wrong day entered")
				exit()

def after(date):
	valid_date(date)
	year = int(date[0:4])
	month = int(date[5:7])
	day = int(date[8:])
	maxmonth = days_in_mon(year)
    
	nextday = day + 1
    
	if nextday > maxmonth[month]: 
		nextday = 1
		month = month + 1
		if month > 12:
			month = 1
			year = year + 1

	next_date = str(year) + "-" + str(month).zfill(2) + "-" + str(nextday).zfill(2)
	return next_date
     
def before(date):
	valid_date(date)
	year = int(date[0:4])
	month = int(date[5:7])
	day = int(date[8:])
	maxmonth = days_in_mon(year)
	thedaybefore = day - 1
	if thedaybefore == 0:
		month = month - 1
		if month == 0:
			year = year -1
			month = 12
			thedaybefore = 31
		else:
			thedaybefore = maxmonth[month]

	prev_date = str(year).zfill(2) + "-" +str(month).zfill(2) + "-" + str(thedaybefore).zfill(2)
	return prev_date
		
def dbda(date,days):
	count = 0
	whole  = 0
	real_day = date
    
	if int(days) > 0: 
		while count < int(days):  
			count = count + 1
			if sys.argv[1] == '--step':
				real_day = after(real_day)
				print(real_day)
			else:
				real_day = after(real_day)                
               
	elif int(days) < 0:  
		while count > int(days):
			count = count - 1
			if sys.argv[1] == '--step':
				real_day = before(real_day)
				print(real_day)
			else:
				real_day = before(real_day)            
            
	else:
		real_day = real_day
    
	if sys.argv[1] == '--step':
		print('', end='')
	else:
		print(real_day) 
    
    #Bonus Question the year date calculator 
	if len(str(days)) == 10:
		valid_date(days)
		if date < days:
			while real_day < days:  
				whole  = tota1 + 1
				real_day = after(real_day)
		elif date > days:
			while real_day > days:  
				whole  = whole  + 1
				real_day = before(real_day)
		print(whole )     

if __name__ == "__main__":
	usage()
	if sys.argv[1] == '--step':
		date = sys.argv[2]
		days = sys.argv[3]
	else:
		date = sys.argv[1]
		days = sys.argv[2]

	dbda(date,days)       



