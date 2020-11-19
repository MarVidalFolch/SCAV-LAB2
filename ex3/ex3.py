# LAB 2 - EX 3
import subprocess


# scale the cut video in different resolutions (ex3)
def resize():
    video = input('Enter the name of the video input file (+.file_type): ')
    w = input('Enter the width you desire for the new resolution: ')
    h = input('Enter the height you desire for the new resolution: ')
    output = input('Enter the name of the output video (+.file_type): ')
    command = f"ffmpeg -i {video} -vf scale={w}:{h} {output}"
    subprocess.call(command, shell=True)


resize()