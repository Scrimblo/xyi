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
def genany (kpop):
	dichard = []
	for i in kpop:
		dichard.append(random_item(i))
	return dichard
def run (kpop):
	richard = [] 
	for i in range (0,cuntest):
		richard.append(genany(kpop))
	return mainloop(richard)
def mainloop (kpop):
	pass
#
#mutacia
def muff (kpop):
	pass
#
#skreczivanie
def cruss (kpop):
	pass
#
#selekcia
def slicktion (kpop):
	pass
#
#ocenka
def voolu (kpop):
	pass