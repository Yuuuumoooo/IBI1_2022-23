#store and sort costs
costs=[1,8,15,7,5,14,43,40]
costs=sorted(costs)
print(costs)
#output: [1, 5, 7, 8, 14, 15, 40, 43]

#draw a bar plot
import matplotlib.pyplot as plt
color=["orange","lightcoral","palevioletred","orchid","gold","lightblue","orangered","sandybrown"]
x=["Los Angeles 1984","Sydney 2000","Atlanta 1996","Seoul 1988","Athens 2003","Barcelona 1992","London 2012","Beijing 2008"]
plt.bar(x,costs,color=color)
plt.xticks(rotation=20,fontsize=8)
plt.ylabel("Costs(in $ billions)")
plt.title("Olympic Costs")
plt.show()
