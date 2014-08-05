# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Robin CHowdhury
# 2014-08-05
# Gör om 4 meningar till en rondelet



# Skriver ut välkomsttexten
def writeWelcomeText():
	print("DIKTOMATEN")


# Läser in de 4 meningarna
def getInputs():
	print("Skriv in fyra meningar och få ut en rondelet!")
	sentence.append(input("Skriv mening nr 1: "))
	sentence.append(input("Skriv mening nr 2: "))
	sentence.append(input("Skriv mening nr 3: "))
	sentence.append(input("Skriv mening nr 4: "))


# Förbestämmda meningar för testning
def testInput():
	sentence.append("Det fanns ingen fil när jag handlade på Konsum.")
	sentence.append("Bananerna var också slut.")
	sentence.append("Jag köpte bröd istället.")
	sentence.append("Nån sorts limpa med mycket fibrer.")

# Skriver ut allt i rondelet format
def printPoem():
	fourFirstWords = " ".join(sentence[0].split()[0:4]) # första fyra orden
	rest = " ".join(sentence[0].split()[4:]) # resten av första meningen
	print(fourFirstWords.upper()) # Gör om till versaler
	print()
	print(fourFirstWords)
	print(rest)
	print(fourFirstWords)
	print(sentence[1])	# mening 2
	print(sentence[2])	# mening 3
	print(sentence[3])	# mening 4
	print(fourFirstWords)


# Huvudprogrammet
sentence = []	
writeWelcomeText()
getInputs()
printPoem()