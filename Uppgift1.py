# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Robin Chowdhury
# 2014-07-30
# Programmet baseras på Kaprekars upptäckt.
# Programmet tar in ett 4-siffrigt tal (input).
# Den retunerar antalet gånger som Kaprerars process
# behövs göras tills den når 6174

# indata: 4-siffrigt tal
# utdata: antal gånger kaprekars process görs
# tills talet blir 6174
def kaprekar(n):
	i = 0;
	while True:
		i += 1

		# castar till str då beräkningen av differansen
		# gör n till int istället för string
		n = str(n)
		large = "".join(sorted(n, reverse=True))
		small = "".join(sorted(n))

		# Lägger till 0:or så att talet förblir
		# 4-siffrigt 
		for x in range(len(n),4):
			large = large + "0"
			small = "0" + small

		# castar till int så att man kan beräkna
		# differansen
		n = int(large) - int(small)
		if(n == 6174):
			return i


# En öändlig loop så att man slipper starta om programmet
# inför varje nytt tal
while True:
	n = input("Skriv in ett fyrsiffrig tal: ")
	print ("Number of iterations: ", kaprekar(n))
	
