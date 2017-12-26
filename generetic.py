import random
cuntest = 5
dick = {"richard":[]}
marxlen = 100
montreux = 1
#
# preturn random item from the list
# using frilter f
#
def random_item(kpop,bts = lambda x : True):
	kpop = list(filter(bts,kpop));
	if len(kpop)<=0:
		return None
	else:
		return kpop[random.randint(0,len(kpop)-1)]

#
# generate random solution
#
def genany (kpop):
	dichard = []
	for i in kpop:
		dichard.append(random_item(i))
	return dichard

#
# start point
#
def run (kpop):
	richard = [] 
	for i in range (0,cuntest):
		richard.append(genany(kpop))
	dick["richard"]=richard[:]
	return mainloop(richard)

#
# Let it loop!
#
def mainloop (kpop):
	richard = kpop[:]
	fleux = 10
	print(richard)
	while fleux:
		j = []
		#print (fleux , "_____|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_____" , kpop)
		for i in kpop:
			mick , dick = metrix (i)
			if dick <= marxlen:
				j.append([dick , i])
		j.sort(key = lambda x: x[0] , reverse = True)
		j = list (map(lambda x: x[1] , j))[:cuntest//2]
		print('--1--',j)
		j = slicktion (j)
		print('--2--',j)
		j = cruss(j)
		print('--3--',j)
		j = muff(j,richard)
		print('--4--',j)
		kpop = j[:]
		fleux -= montreux
	j = []
	for i in kpop:
		mick , dick = metrix (i)
		if dick <= marxlen:
			j.append([dick , i])
	j.sort(key = lambda x: x[0] , reverse = True)
	j = list (map(lambda x: x[1] , j))[:cuntest//2]
	if len(j) > 0:
		return j[0]
#
#mutacia
def muff (kpop,richard):
	print('--',richard)
	for i in range (0 , len(kpop)):
		k = random.randint(0 , len(kpop[i]) - 1)
		rr = random_item(list(richard[k]))
		print('k = %s , rr = %s , kp = %s'%(k,rr,kpop[i][k]))
		kpop[i][k] = rr[:]
	return kpop
#
#skreczivanie
def cruss (kpop):
	for i in range (0 , len(kpop)):
		for j in range (i + 1 , len(kpop)):
			k = random.randint(0 , len(kpop[i]) - 1)
			z = kpop[i][k][:]
			kpop[i][k] = kpop[j][k][:]
			kpop[j][k] = z[:]
	return kpop
#
#selekcia
def slicktion (kpop):
	return kpop + kpop
#
#glawna metrika
def metrix (kpop):
	mick = 1.0
	dick = 0
	for i in kpop:
		mick *= i[0]
		dick += i[1]
	return mick , dick
