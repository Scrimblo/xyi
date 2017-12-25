import random
cuntest = 10
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
	return mainloop(richard)

#
# Let it loop!
#
def mainloop (kpop):
	pass

def muff (kpop):
	pass

def cruss (kpop):
	pass

def slicktion (kpop):
	pass