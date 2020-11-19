# LAB 2 - EX 5
import os
import subprocess


# get size, duration and resolution
def parse():
    video = input('Enter the name of the video input file (+.file_type): ')
    command1 = f"ffprobe -v error -show_entries format=size -of default=noprint_wrappers=1 {video}"  # get size
    command2 = f"ffprobe -v error -select_streams v:0 -show_entries stream=duration -of " \
               f"default=noprint_wrappers=1:nokey=1 {video}"  # get duration of the first video stream
    command3 = f"ffprobe -v error -select_streams v:0 -show_entries stream=height,width -of csv=s=x:p=0 {video}"  #
    # get resolution
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)
    subprocess.call(command3, shell=True)


# rename any type of file
def rename():
    file_path = input('Enter the file path: ')
    old_name = input('Enter the file name: ')
    new_name = input('Enter the new name of the file: ')
    file_type = input('Enter the file type: ')
    os.rename(fr'{file_path}{old_name}{file_type}', fr'{file_path}{new_name}{file_type}')


# resize the cut video in different resolutions (ex3)
def resize():
    video = input('Enter the name of the video input file (+.file_type): ')
    w = input('Enter the width you desire for the new resolution: ')
    h = input('Enter the height you desire for the new resolution: ')
    output = input('Enter the name of the output video (+.file_type): ')
    command = f"ffmpeg -i {video} -vf scale={w}:{h} {output}"
    subprocess.call(command, shell=True)


# define and call function to transcode the input into an output with another codec (in this case, AV1)
def new_codec():
    video = input('Enter the name of the video input file (+.file_type): ')
    output = input('Enter the name of the video output file (+.file_type): ')
    command = f"ffmpeg -i {video} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental {output}"
    subprocess.call(command, shell=True)


# create a menu for the user to choose the desired operation
option = input('Enter a number: \n"1" to parse BBB.mp4. \n"2" to rename file. \n"3" to resize file. \n"4" to convert '
               'to '
               'AV1 codec.')
if option == "1":
    parse()
elif option == "2":
    rename()
elif option == "3":
    resize()
elif option == "4":
    new_codec()
