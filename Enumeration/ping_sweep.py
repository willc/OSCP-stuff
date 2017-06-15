#!/usr/bin/python

import multiprocessing
import subprocess
import os
import sys


def pinger( job_q, results_q ):
	DEVNULL = open(os.devnull,'w')
	while True:
		ip = job_q.get()
		if ip is None: break

		try:
			subprocess.check_call(['ping','-c1',ip], stdout=DEVNULL)
			results_q.put(ip)
		except:
			pass


def main():

    	if len(sys.argv[1:]) != 1:
		print "Usage: ./ping_sweep.py <network>"
		print "Example: ./ping_sweep.py 10.10.1 \n"
		sys.exit(0)

	network = sys.argv[1]

	pool_size = 255

	jobs = multiprocessing.Queue()
	results = multiprocessing.Queue()

	pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
		for i in range(pool_size) ]

	for p in pool:
		p.start()

	for i in range(1, 255):
		jobs.put('{net}.{ip}'.format(net=network, ip=i))

	for p in pool:
		jobs.put(None)

	for p in pool:
		p.join()

	while not results.empty():
		ip = results.get()
		print(ip)

main()

