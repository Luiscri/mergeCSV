import os
import csv

def mergeCSV(source_directory_path, output_file):
	if source_directory_path[-1] != '/':
		source_directory_path = source_directory_path + '/'

	# Remove this if you want to merge several directories into one file
	try:
		os.remove(output_file)
	except OSError:
		pass

	filenames = [os.path.join(source_directory_path, f) for f in os.listdir(source_directory_path) if os.path.isfile(os.path.join(source_directory_path, f))]
	with open(output_file, 'a') as f:
		# Copy fully the first CSV file, header included
		with open(filenames[0], 'r') as f1:
			for line in f1:
				f.write(line)
		
		# Copy remaining CSVs skipping the header
		for file in filenames[1:]:
			with open(file, 'r') as f2:
				for idx, line in enumerate(f2):
					if idx > 0:
						f.write(line)