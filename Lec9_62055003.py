#62055003ตั๊ก
import pandas as pd
from matplotlib import pyplot as plt


#step1
movies_df = pd.read_csv('C:\\Users\\user\OneDrive\Desktop\Phython\imdb2.csv',index_col="Title")
martin_df = (movies_df['director']) == 'Martin Scorsese' 
print(martin_df.shape)

#Step2
print(movies_df[movies_df['director'] == 'Martin Scorsese' ])

# #step3
def metascore_function(x): 
    if x == 79.0: 
        return "Silence " 
    elif x == 75.0: 
        return "The Wolf of Wall Street"
    elif x == 85.0: 
        return "The Departed t"
    elif x == 63.0: 
        return "Shutter Island "
    elif x == 83.0: 
        return "Hugo "

movies_df["Martin Scorsese"] = movies_df["metascore"].apply(metascore_function) 
movies_df['Martin Scorsese'].value_counts().plot(kind='bar', title='Scorsese Movies Revenue');
plt.show()