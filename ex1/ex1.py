# LAB 2 - EX 1
import subprocess


# get size, duration and resolution
def parse(video):
    command1 = f"ffprobe -v error -show_entries format=size -of default=noprint_wrappers=1 {video}"  # get size
    command2 = f"ffprobe -v error -select_streams v:0 -show_entries stream=duration -of " \
               f"default=noprint_wrappers=1:nokey=1 {video}"  # get duration of the first video stream
    command3 = f"ffprobe -v error -select_streams v:0 -show_entries stream=height,width -of csv=s=x:p=0 {video}"  #
    # get resolution
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)
    subprocess.call(command3, shell=True)


parse('BBB.mp4')
