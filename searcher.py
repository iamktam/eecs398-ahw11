import glob
import topic
searcher = topic.Searcher()
for filename in searcher.search('algorithm', 2, glob.glob('*.txt')):
	print (filename)