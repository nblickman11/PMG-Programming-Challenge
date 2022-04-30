#!/usr/bin/env python3

import csv
import sys

def create_writer_object(object):
	# return a writer which will be used to write data to object 
	# (in this case, object is not file but is sys.stdout, which is output to the terminal)
	return csv.writer(object)

def write_header(header, writer):
	writer.writerow(header)

def retrieve_filename(path):
	return path.split("/")[-1]

def write_record(record, writer):
	record.append(retrieve_filename(path))
	writer.writerow(record)

def write_file_contents(path, writer):
	with open(path) as file_wrapper:
		reader = csv.reader(file_wrapper)
		next(reader) # skips over the header
		for row in reader:
			write_record(row, writer)

if __name__ == '__main__':
	writer_object = create_writer_object(sys.stdout)
	write_header(["email_hash", "category", "filename"], writer_object)
	for path in [sys.argv[1], sys.argv[2]]:
		write_file_contents(path, writer_object)
