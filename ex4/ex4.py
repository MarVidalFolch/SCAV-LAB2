# LAB 2 - EX 4

import subprocess


# define and call function to transcode the input into an output with another codec (in this case, AV1)
def new_codec(video, output):
    command = f"ffmpeg -i {video} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental {output}"
    subprocess.call(command, shell=True)


new_codec('10sec.mp4', 'output_ex4.mkv')
