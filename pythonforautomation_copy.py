#why python
#simple syntax,rich ecosystem
#cross-platform suport
#use cases:
#-batch files 
#-web development
#-data analysis
#-artificial intelligence

#the os module

import os 
for file in os.listdir("."):
    if file.endswith(".py"):
        print(file)
#making a copy of a file
import shutil
shutil.copy("pythonforautomation.py","pythonforautomation_copy.py")
from datetime import date, datetime
now=datetime.now()
print(f"Current date and time: {now}")