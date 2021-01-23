

# Creating month list
months=['January','Feburary','March','April',
    'May','June','July','August','September',
    'October','November','December']

for i in range(1,13):
    # Index of Maximum temperature in column of data frame
    index=np.argmax(temp_df[i])
    
    # Year of that Maximum temerature
    year= temp_df[0][index]

    # Month for which maximum temperature is calculated
    month= months[i-1]
    print(f"The maximum temperature in %s is in year %s"
        %(month,year))
    

# Claculating rolling average
# Creating an empty dictinary
rolling_average ={}

# Setting window size to 3
window_size=3
for i in range(1,13):
    # Data of specific month 
    month_data= temp_df[i]
    
    # calulation of rolling average using given window size 
    rolling_average[months[i-1]]=  month_data.\
        rolling(window_size).sum()

# Converting dictionary to dataframe
rolling=pd.DataFrame(rolling_average)

for i in range()
rainfall= np.array(rolling[1])

# Saving Data frame into txt file
rolling.to_csv("rolling_average.txt", header=True, index= False,
     sep= "\t")

# Saving Dataframe into binary file
rolling.to_stata("rolling_average.dta")