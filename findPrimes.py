n = 3
primes = [2]
compteur = 1

while (True):
	
	if(compteur >= 500):
                break
	
	for k in primes:
		q = n / k
		r = n % k
               
	        if(r == 0):
                        #Augmenter n car celui-ci n'est pas prime
			break
		if(q <= k):
                        primes.append(n)
                        compteur = compteur + 1
                        print(n)
                        print("hitter is " + str(k))
                        print("Le compteur est " + str(compteur))
		        break

        n = n + 2




