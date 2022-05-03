# 以时间重命名wav文件
import os,time,sys
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
os.rename("test.wav",now+str(".wav"))
