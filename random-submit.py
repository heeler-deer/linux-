import os
import random
import time
list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

while(1):
  s1=random.choice(list)
  s2=random.choice(list)
  s3=random.choice(list)
  s4=random.choice(list)
  s5=random.choice(list)
  s6=random.choice(list)
  s7=random.choice(list)
  s8=random.choice(list)
  str=" 'somthing need to write"
  str=str+s1+s2+s3+s4+s5+s6+s7+s8+"'"
  #str=" '132.232.98.70:6363/checkSecret?id=202026010310&v=A01DD0F91A5A7DF0163C07&s=A853F587' "
  print(str)
  process=os.popen( "curl  %s" % str).readlines()
  #process=os.popen( " curl 'www.baidu.com' ").readlines()
  print(process)
  t='120'
  boole=t in process
  if boole==False:
    print("\n \n ")
  else:
    print(boole)
    break;
    
  time.sleep(3)
  