import sys
import re

def map_words_from_file(filename):
	words_to_counts = dict()
	with open(filename) as file_reader:
		line = file_reader.readline()
		while line:
			# Replaces punctuation in line with white space
			line = re.sub(r'[^\w\s]', ' ', line)
			# Removes next line character
			line = line[0:len(line) - 1]
			words = line.lower().split(' ')
			for word in words:
				if len(word) != 0:
					words_to_counts[word] = words_to_counts[word] + 1 if word in words_to_counts else 1
			line = file_reader.readline()
	return words_to_counts

def write_mapping_to_file(filename, mapping):
	sorted_words = sorted(mapping.keys())
	with open(filename, 'w+') as file_writer:
		for word in sorted_words:
			file_writer.write(word + ' ' + str(mapping[word]) + '\n')
		file_writer.close()		

def main():
	if len(sys.argv) != 3:
		print('Invalid number of arguments.')
		return
	words_to_counts = map_words_from_file(sys.argv[1])
	write_mapping_to_file(sys.argv[2], words_to_counts)
	
if __name__ == '__main__':
	main()
