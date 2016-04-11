import sys

class Searcher:
	def search(self, word, occ, fileList):
		count = 0
		results = []
		for i in range(0, len(fileList)):
			with open(fileList[i]) as f:
				for line in f:
					wordlist = line.split()
					for w in wordlist:
						if word in w:
							count += 1
			if count >= occ:
				results.append(fileList[i])
				count = 0
			else:
				count = 0
		while count < len(results):
			yield results[count]
			count +=1

if len(sys.argv) > 1:
	if len(sys.argv) < 3:
		print "Invalid input"
	numFiles = len(sys.argv) - 3
	word = sys.argv[1]
	occ = int(sys.argv[2])
	results = []
	count = 0
	files = []
	for i in range(3, numFiles + 3):
		files.append(sys.argv[i])
	searcher = Searcher()
	for c in searcher.search(word, occ, files):
		print c