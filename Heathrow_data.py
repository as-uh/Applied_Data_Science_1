import requests
import numpy as np 
import pandas as pd 

url= "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt"

request = requests.get(url)
data= request.text
lines= data.split('\n')

temp_data=[]
for line in lines[7:-1]:
    temp_data.append(line.split())
    
temp_df= pd.DataFrame(temp_data)

months=['January','Feburary','March','April',
    'May','June','July','August','September',
    'October','November','December']
for i in range(1,13):
    index=np.argmax(temp_df[i])
    year= temp_df[0][index]
    month= months[i-1]
    print(f"The maximum temperature in %s is in year %s"
        %(month,year))
    

# Claculating 






    