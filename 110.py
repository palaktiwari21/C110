import random
import plotly_express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

df=pd.read_csv('data.csv')
data=df['temp'].tolist()
#fig=ff.create_distplot([data],['temp'],show_hist=False)
#fig.show()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print('Population Mean Is : ',population_mean)
print('Population Standard Deviation is : ',std_deviation)
def random_set_of_mean(counter):

    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
 
def show_fig(mean_list):
    df=mean_list
    std_deviation=statistics.stdev(mean_list)
    print('Standard deviation of Sampling distribution is : ',std_deviation)
    fig=ff.create_distplot([df],['temp'],show_hist=False)
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()


    
