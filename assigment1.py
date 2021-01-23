import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

url="https://data.ny.gov/resource/skw8-wkzf.json"
request = requests.get(url)

data= json.loads(request.text)


dataset=[]
for i in range(len(data)):
    rows=[]
    for key,value in data[i].items():
        try:
            rows.append(float(value))
        except:
            rows.append(value)
    dataset.append(rows)

co2_data= pd.DataFrame(dataset,
    columns = [key for key,
    value in data[0].items()])

sns.relplot(x="year", 
    y="percent_of_total_co2_emissions",
    hue="fuel_type", kind="line", data = co2_data)
    

plt.title("Percentage of \
    $CO_2$ emission by different fuels")

#plt.show()
#plt.savefig("Pecentage_co2emission.png")
print(co2_data["year"])
print(co2_data["total_co2_emissions"])
print(co2_data["fuel_type"])

sns.relplot(x="year", 
    y = "total_co2_emission", 
    hue = "fuel_type")