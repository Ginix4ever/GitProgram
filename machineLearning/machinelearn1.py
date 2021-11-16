import pandas as pd
import os
from IPython.display import display

    
if __name__ == '__main__':
    
    print( os.getcwd());

    data3 = pd.read_excel('machineLearning/files/class1/data_3_course.xlsx')
    #data4 = pd.read_excel('machineLearning/files/class1/data_4_course.xlsx')
    #随机三行
    #display(data3.sample(3))
    #pd.options.display.max_rows = 6
    #display(data3)
    #display(data3.columns)
    #display(data3.dtypes)
    #display(data3.loc[2])

    #display(type(data3.loc[2]))
   # display(type(data3.loc[2]))

    display(data3.loc[2:4])
   