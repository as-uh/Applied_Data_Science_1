import requests
import pandas as pd 

class regional_data:

    def __init__(self, region, parameter):
        self.region=region
        self.parameter= parameter

    def get_data(self):
        request= requests.get(f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{
        self.parameter}/date/{self.region}.txt") 
        data= request.txt
        lines = data.split("/n")
        {parameter}_data=[]
        for line in lines:
            
            
        
        
        
            
        