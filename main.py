# from ifcondition import *
#from variables import *
#from datacampplots import *
#from datacampdict import *
#from datacamppandas import *
#from mathesisfor import *
#from mathesislists import *
#from mathesistest2 import *
#from mathesisdatechoices import *
#from mathesisfunctions import *
#from mathesistest3 import *
#from mathesisguessnum import *
#from datagypythonexcel01 import *
#from combineexcel import *
#from datagyautomateexcel import *
#from os import system
#system('pip install pyodbc')
import mathesisabs

while True :
    n = input('δώσε αριθμό:')
    if n == '' : break
    else :
      n =mathesisabs.abs(n)
      if n:print("η απόλυτη τιμή του είναι {}".format(n))
      else: print("δεν είναι αριθμός!!!")
