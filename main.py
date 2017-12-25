import sys

import generetic

def main(argv):
	if len(argv) > 0:
		filename = argv[1]
	else:
		filename = 'input.csv'

	try:
		data = open(filename).read()
	except Exception as e:
		print('Exception while reading file: %s'%e)
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv)