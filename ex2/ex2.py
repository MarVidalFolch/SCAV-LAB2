# LAB 2 - EX 2
import os


# define a function able to rename any type of file
def rename(file_path, old_name, new_name, file_type):
    os.rename(fr'{file_path}{old_name}{file_type}', fr'{file_path}{new_name}{file_type}')


# call the function in order to rename the video outputs from seminar2
rename('/home/mar/', 'ex1', 'semi2ex2_1', '.mp4')
rename('/home/mar/', 'ex3_160x120', 'semi2ex2_2', '.mp4')
rename('/home/mar/', 'ex3_360x240', 'semi2ex2_3', '.mp4')
rename('/home/mar/', 'ex3_480p', 'semi2ex2_4', '.mp4')
rename('/home/mar/', 'ex3_720p', 'semi2ex2_5', '.mp4')
