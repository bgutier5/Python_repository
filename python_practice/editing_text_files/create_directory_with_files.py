import os

def create_dir_and_files(folder_name, file_name, total):
	os.system('mkdir {}'.format(folder_name))
	for i in range(total):
		full_file_name = './{}/{}_{}.py'.format(folder_name, file_name, i)
		f = open(full_file_name, 'a')
		f.write('term')
		f.close()


create_dir_and_files('delta_t1', 'term', 10)


