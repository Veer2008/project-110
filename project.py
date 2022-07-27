import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("Population mean is ",population_mean)
print("std_deviation ",std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    std_deviation=statistics.stdev(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution is ",mean)
    std_deviation=statistics.stdev(mean_list)
    print("std_deviation of sampling distribution ",std_deviation)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
     
    show_fig(mean_list)
    
setup()