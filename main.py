#!/usr/bin/env python3.6
import sys
import generetic

cc = [' ','\r','\n','\t']
def delspace(st):
	while True in list(map(lambda x:st.startswith(x),cc)):
		st = st[1:]
	while True in list(map(lambda x:st.endswith(x),cc)):
		st = st[:-1]
	return st

def split_(data):
	az = []
	for i in data.split('\n'):
		st = i
		st = delspace(st)
		az.append(st)
	return az

def main(argv):
	if len(argv) > 1:
		filename = argv[1]
	else:
		filename = 'input.csv'

	try:
		data = open(filename).read()
	except Exception as e:
		print('Exception while reading file: %s'%e)
		sys.exit(1)

	try:
		tmp = split_(data)
		data = []
		for i in tmp:
			az = []
			ss = list(map(lambda x:delspace(x),i.split(',')))
			for j in range(len(ss)//2):
				j*=2;
				az.append([float(ss[j]),int(ss[j+1])])
			data.append(az)
	except Exception as e:
		print('Exception while parsing file: %s'%e)
		sys.exit(1)
	print(generetic.run(data))

if __name__ == "__main__":
	main(sys.argv)