# Viz_DiceGame

This is intended to visualize the test results from a Dice Game. There are two strategies (GAIN & THROW) and each has different values. The statistics of games are stored in a text file and it reflects which strategy performs better. Specifically, the winning probability of one strategy depends on two parameters (Gain_val and Throw_val). Therefore, it is necessary to visualize the results with scatter 3D graphs, which is not clear in scatter 3D graphs especially when describing the pattern. There is a better choice of contour that uses different colours to indicate the winning probability. It is clear and straightforward. 

The data manipulation is completed within pandas and graphs are drawn within matplotlib. 

One of the examples is as follows.

![contour100](https://github.com/ZihengZZH/Project_Python/blob/master/Viz_DiceGame/graphs/contour100.png)
