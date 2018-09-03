import os,time

import datetime
import glob


def log_reader(file_name):
	line_num=0
	with open(log_to_parse) as f:
		for line in f:
			line_num = line_num+1
			if 'Exception' in line:
				print ('Exception found in %s file on line_number %d  as %s'%(log_to_parse,line_num,line))


def check_file_count(old_file):
	ts=datetime.datetime.utcnow().strftime("%Y-%m-%d")
        log_files=[]
        for file in glob.glob("aggregation_%s*.log"%ts):
                log_files.append(file)
	if len(log_files) != old_file:
		return True
	return False

ts=datetime.datetime.utcnow().strftime("%Y-%m-%d")
log_files=[]
for file in glob.glob("aggregation_%s*.log"%ts):
	log_files.append(file)
       	log_to_parse= log_files[-1]
print 'Exception in last log file'
log_reader(log_to_parse)

while True:

	ts=datetime.datetime.utcnow().strftime("%Y-%m-%d")
	log_files=[]
	for file in glob.glob("aggregation_%s*.log"%ts):
        	log_files.append(file)
	log_to_parse= log_files[-1]
	old_file = len(log_files)
	print 'Current count of file %d'%old_file
	if check_file_count(old_file):
		log_reader(log_to_parse)
	else:
		print('Sleeping for 60 seconds')
		time.sleep(60)
