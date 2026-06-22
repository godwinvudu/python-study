def main():
    for i in range (54,82,2):
    #height is in inches
     for x in range (85,350,5):
     #weight is in pounds
    
       bmi=(x*703)/(i**2)
       print(round(bmi))
if __name__=="__main__": 
 main()