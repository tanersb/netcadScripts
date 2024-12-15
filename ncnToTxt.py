import os

TxtFile = []
NcnFile = []

def main():
	for file in os.listdir():
		if file.endswith('.txt'):
			TxtFile.append(file)
		if file.endswith('.ncn'):
			NcnFile.append(file)	
			

def TxtToNcn():
	main()
	for file in TxtFile:
		txtname = file
		os.rename(txtname, f"{txtname.split('.')[0]}.ncn")
		print("TXT To NCN")
		print(txtname)
		

def NcnToTxt():
	main()
	for file in NcnFile:
		ncnname = file
		os.rename(ncnname, f"{ncnname.split('.')[0]}.txt")
		print("NCN To TXT")
		print(ncnname)
		
		
NcnToTxt()
