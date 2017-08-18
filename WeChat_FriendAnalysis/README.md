# Friend analysis through a WeChat API

Some external libraries need to be installed first to implement this project (These libraries can be installed with pip, quick and simple):
* Numpy & Pandas (To w/r csv file and provide key data structures)
* ItChat (To provide an incredible API to WeChat)
* pyechart (To generate interactive graphs with specific data)

This project is intended to read and visualise friends information from one specific WeChat account, which is authorised through scanning QR code. Friends information will be first extracted from account and stored as DataFrame (Pandas). These information will be then written to csv file for further visualisation. The reason why it is necessary to generate a intermediate csv is that there may be some other ways to visual information, either in R or in MATLAB. The display.py will read the csv file and then generate some interactive graphs that will be saved as individual html files. Pie chart, Bar chart and Map chart will be used for visualisation due to different characteristics.


NOTE: There is something that should be paid much attention: encoding. The default encoding in Python is ASCII, which does not support chinese character correctly. So, utf-8 encoding should be declared at the beginning of the code.
