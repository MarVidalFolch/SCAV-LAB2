# SCAV-LAB2

## Mar Vidal-Folch Angerri - NIA: 204751

In this lab we have worked with the Big Bunk Bunny video, Python and ffmpeg:

### Exercise 1
---
In this exercise, we have created a pyhton script that marks 3 elements from the metadata from the BBB.mp4 container. 
In order to see which data we wanted to get, we used the following command: ffmpeg -i BBB.mp4. The output can be seen in a screenshot of the folder ex1. 
In this case, we will get the size of the file, the duration of the first video stream and the file resolution, you can see the commands in the script of the folder ex1. In the same folder you can find a screenshot of the output when running the script called ex1.png. 

### Exercise 2
---
We have created a Python script able to rename 5 quality outputs of the BBB from last seminar. We have simply created a function and called it 5 times defining the new names of the files. You can find the script and the output files in folder ex2. 


### Exercise 3
---
We have created a script able to resize any input video given. To do it, we have reused the function from seminar 2 but doing some small changes. Now, the user can input the desired output resolution. The resized output and the script can bee found in folder ex3.

### Exercise 4
---
In this exercise we are transcoding the input video to an output with AV1 codec. In folder ex4 you can find the script where this is done with the command used. In the same folder, there is the given video output and a screenshot. In the screenshot we can see the output of the command ffmpeg -i output.mp4 of the output video. There, we can see that it has been transcoded correctly. 

### Exercise 5
---
We have created a python script with all previous exercises. We have added a menu so the user can choose which operation to do and we have modified the functions in order to make them more 'universal'. Now, the user inputs the different parameters as, for example, the name of the input video which we want to change. The script can be found in the ex5 folder.  
