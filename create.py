import os


name = raw_input("name: ")
author = raw_input("author: ")
version = raw_input("version: ")
description = raw_input("description: ")
main = raw_input("main: ")





def MakeBasic():
	
	YMLString = "name: " + name + "\n" + "author: " + author + "\n" + "version: " + version + "\n" + "description: " + description + "\n" + "main: " + main
	clearconsole()
	print(YMLString)
	print("\n")
	makeAddition(YMLString)

def makeAddition(YMLString):
	additional = raw_input("wanna add additional Arguments (y or n): ")
	if additional == "n":
		clearconsole()
		print(YMLString)
		exit()
	elif additional == "y":
		clearconsole()
		print("[1] Website")
		print("[2] api-version")
		print("[3] prefix")

		choice = raw_input("Number to add: ")
		if choice == "1":
			website = raw_input("Website: ")
			YMLString = YMLString + "\n" + "website: " + website
			clearconsole()
			print(YMLString)
			print("\n")
			makeAddition(YMLString)


		if choice == "2":
			APIver = raw_input("api-version: ")
			YMLString = YMLString + "\n" + "api-version: " + APIver
			clearconsole()
			print(YMLString)
			print("\n")
			makeAddition(YMLString)


		if choice == "3":
			prefix = raw_input("prefix: ")
			YMLString = YMLString + "\n" + "prefix: " + prefix
			clearconsole()
			print(YMLString)
			print("\n")
			makeAddition(YMLString)
def clearconsole():
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")


MakeBasic()