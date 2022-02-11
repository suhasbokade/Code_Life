# Metplotlib library is used to plot diffn type of gragh. It usually acts as data visualization tool


import numpy as np
import matplotlib.pyplot as plt     # pyplot=sub library

x=np.array([10,20,30,40,50,60])
y=np.array([20,10,50,40,60,70])

plt.plot(x,y,marker=".")    # "*"  "o"  "." "x" "X" "D" "H" "v"   plt.plot(x,y,marker=".")--- show with line
# plt.plot(x,y,"*:k")           # r== red colour dot line graph  # :==doted line
# plt.plot(x,y,marker="o",ms=35,mec="r",mfc="g")    # ms = marker line size  # mec= edge colour # mfc= circle clr
plt.show()

#Different line type:-

# : dot line
# - solid line
# -- dash line
# -. dash & doted line

# Colour:-

# r= Red
# g= Green
# b= Blue
# c= Cyan
# m= magenta(Pink)
# y= yellow
# k= Black
# w= White

# Scatter Plot:-

# x1=np.array([100,200,300,400,500,600])
# y1=np.array([200,100,500,400,600,700])
#
# plt.scatter(x1,y1)
# plt.scatter(x,y)
# plt.show()


# Bar Chart:-

# x=np.array([20,30,48,50,60])
# y=np.array(["A","B","C","D","E"])
#
# name=["Quantity"]
# plt.bar(y,x)
# plt.bar(y,x,color="red")   # Color will change
# #plt.bar(y,x,color="red",width=0.3)
# plt.barh(y,x,height=0.3)
# plt.xlabel("Toy Name")    # Title for axis
# plt.ylabel("Quantity sold")    # Title for axis
# plt.legend(name,loc="upper right", title="sales")
# plt.title("Total Sale for Oct 2021")    # Title of the whole gragh
# plt.show()


## PIE CHART:-

# data=np.array([10,20,50,30,10])
# l=np.array(["A","B","C","D","E"])
# e=(0.2,0,0.1,0,0)
#
# plt.pie(data,labels=l,explode=e,autopct="%.2f",shadow=True)
# plt.legend(loc="upper left")
# plt.show()

## HISTOGRAM:-

# data=np.random.normal(200,20,250)    # Example(1)
# print(data)
#
#
# data=np.array([1,2,6,3,8,3,5,8,6,3,9,6,3,0,1,2,5,7,3,1,4,8,7,5,4,2,2,0])     # Example(2)
#
# plt.hist(data)
# plt.show()

## HEATMAP:-

# data=np.random.random((12,12))
# plt.imshow(data,cmap="autumn",interpolation="nearest")
# plt.show()           # color:- coolwarm,summer,autumn


## BOXPLOT:-

# data=np.random.normal(100,20,200)
# plt.boxplot(data)
# plt.show()


## SEABORN:-

# import numpy as np
# import seaborn as sns
# import matplotlib.pylab as plt
#
# data_set = np.random.rand(10,10)
# ax = sns.heatmap(data_set,linewidth=0.5, cmap='coolwarm')
#
# plt.title("2-D Heat Map")
# plt.show()