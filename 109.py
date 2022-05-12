import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv
import random

data = pd.read_csv("StudentsPerformance.csv")

a = data["reading score"].tolist()

mean = sum(a) / len(a)
std_deviation = statistics.stdev(a)
median = statistics.median(a)
mode = statistics.mode(a)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation,   mean + std_deviation

second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation),   mean + (2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation),   mean + (3*std_deviation)

fig= ff.create_distplot([a], ["reading scores"], show_hist=False )

fig.add_trace(go.Scatter(x= [mean, mean], y= [0,0.17], mode= "lines", name= "MEAN"))
fig.add_trace(go.Scatter(x= [first_std_deviation_start, first_std_deviation_start], y= [0,0.17], mode= "lines", name= "Standard Deviation 1"))
fig.add_trace(go.Scatter(x= [first_std_deviation_end, first_std_deviation_end], y= [0,0.17], mode= "lines", name= "Standard Deviation 1"))

fig.show()
