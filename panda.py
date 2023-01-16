import pandas as pd
from matplotlib import pyplot as plt
file = pd.read_csv('BlackFriday.csv')
print(
    ((len(file[
        ((file['Age']=='36-45') | 
        (file['Age']=='46-50') | 
        (file['Age']=='51-55') | 
        (file['Age']=='55+')) &
        (file['Gender']=='F')
        ])) + 
    len(file[(file['Gender']=='M') & (file['Age']=='26-35')]))
    /
    len(file)
    )
