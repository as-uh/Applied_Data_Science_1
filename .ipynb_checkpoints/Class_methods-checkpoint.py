import requests
import pandas as pd 

class regional_data():

    def __init__(self, region, parameter):
        self.region=region
        self.parameter= parameter

    def get_url(self):
        request= requests.get(f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt")

    




