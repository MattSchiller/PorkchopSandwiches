"""Imports a local dictionary, requests up to 7 letters including blanks, and outputs all valid words"""
import time
import string
import re
import fnmatch
from Trie import trie

def importFile():
	#Imports a specified file for loading.
	global dictionary
	with open('C:/Users/Schiller/Desktop/PythonWork/dict.txt') as file:
		dictionary = file.read().splitlines()
		
def createTrie(myDictionary):
	global Trictionary
	Trictionary = trie()
	myStart = time.time()
	for i in myDictionary:
		Trictionary.add(i)
	print("Trie took {:.2f} seconds to load".format((time.time() - myStart)))
	#print(Trictionary)
	
def acceptLetters():
	#Gets the letters from the user
	global letters 
	while True:
		letters = input("Enter up to 7 letters (including _ for blank): ")
		if re.search("[^A-z*]+", letters):
			print("Invalid characters entered, try again.")
		#elif len(letters) > 7 or len(letters) < 1:
		#	print("Invalid number of characters entered >0 and >7 only.")
		else:
			letters = letters.lower()
			letters = ["?" if X is "_" else X for X in letters]
			break		
			
def preAppendFilter(word):
	#Massages out any "?"s pre-checking the trictionary
	questionMark = word.find("?")
	if questionMark >= 0:
		for i in string.ascii_lowercase:
			if questionMark is len(word):
				word = word[0:questionMark]+i
			else:
				word = word[0:questionMark]+i+word[questionMark+1:len(word)]
			appendIfLegal(word)
	else:
		appendIfLegal(word)
		
def appendIfLegal(word):
	#Checks if a word is legal against the dictionary and adds to found words
	global validWords
	if Trictionary.contains(word):
		validWords.append(word)
		
def alreadyChecked(word):
	#Checks to see if this path has been 'gone down' before for duplicate letters
	global checkedWords
	if word in checkedWords:
		return True
	else:
		checkedWords.append(word)
		return False
	
def permute(word, myLetters):
	#Divides a given string to find all combinations of words
	preAppendFilter(word)
	for i in range(len(myLetters)):
		if alreadyChecked(word + myLetters[i]):
			continue
		elif len(myLetters) is 1:
			permute(word + myLetters[i], "")
		else:
			permute(word + myLetters[i], myLetters[0:i] + myLetters[i+1:])

importFile()
createTrie(dictionary)
acceptLetters()
checkedWords = []
validWords = []
start_time = time.time()
permute("", letters)
validWords.sort()
print("Code took {:.2f} seconds to run".format((time.time() - start_time)))
print(len(validWords), "valid words: ", ", ".join(validWords))








