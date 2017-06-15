import requests
import threading
import Queue
import urllib


threads = 50

'''
Setting up the resume variable allows us to resume a brute-forcing session if our
network connectivity is interrupted or the target site goes down.
'''
resume = None

def build_wordlist(wordlist_file):
	with open(wordlist_file, 'rb') as f:
		raw_words = f.readlines()
		f.close()

	found_resume = False
	words = Queue.Queue()
	
	for word in raw_words:
		word = word.rstrip()
		
		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print "[*] Resuming word list from: {}".format(resume)

		else:
			words.put(word)

	return words


def dir_bruter(word_queue, extensions=None):
	while not word_queue.empty():
		attempt = word_queue.get()

		attempt_list = []

		'''
		Checking to see if there is a file extension. If not, we know it's a 
		directory path we're brute-forcing.
		'''
		if "." not in attempt:
			attempt_list.append("/{}/".format(attempt))
		else:
			attempt_list.append("/{}".format(attempt))

		# Brute-forcing extensions
		if extensions:
			for extension in extensions:
				attempt_list.append("/{}{}".format(attempt, extension))

		# Iterating over our list of attempts
		for brute in attempt_list:
			url = "{}{}".format(target, urllib.quote(brute))

			try:
				req = requests.get(url)
				
				if req.status_code == requests.codes.ok:
					print "[{}] => {}".format(req.status_code, url)

			except:
				pass


def main():

	global target, wordlist_file

	target = raw_input("Enter the target URL (E.g., http://testphp.vulnweb.com)\n: ")

	# The word list used for brute-forcing
	wordlist_file = raw_input("Enter the word list filepath(E.g., /opt/SVNDigger/all.txt)\n: ")

	word_queue = build_wordlist(wordlist_file)
	extensions = [".php", ".bak", ".orig", ".inc"]

	for i in range(threads):
		t = threading.Thread(target=dir_bruter, args=(word_queue, extensions))
		t.start()

main()
				
