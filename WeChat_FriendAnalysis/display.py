#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pyecharts import Pie,Bar,Geo,Map


class displayResult(object):

    # Show the sex with pie chart
    def sex_display(self,friends):
        sex = friends.iloc[:,4]
        male = female = other = 0
        sex_result = sex.value_counts()

        sex_dict = {'Other':sex_result[0],'Male':sex_result[1],'Female':sex_result[2]}
        sex_pie = Pie("Gender Counting Result")
        sex_pie.add("",sex_dict.keys(),sex_dict.values(),is_random=True,is_label_show=True)

        sex_pie.show_config()
        sex_pie.render(r"pie_chart_sex.html")
        print "Successfully written to file"


    # Show the city with bar chart and geo chart
    def city_display(self,friends):
        city = friends.iloc[:,1]
        #city_result = city.value_counts()
        #city_df = city_result.to_frame()
        #expand_list = lambda x: [y for l in x for y in expand_list(l)] if type(x) is list else [x]
        city_name = city.value_counts().index.tolist()
        city_num = city.value_counts().values.tolist()
        '''
        SOME KEY CONCEPTS
        friends(dataframe) -> value_counts(series) -> dataframe -> dict -> two lists
        This is the original idea, cumbersome and unefficient
        friends(dataframe) -> value_counts(series) -> two lists
        pyechart has encapsulate operations on Numpy and Pandas, which means
        pyechart can take the list directly from series
        '''
        # Bar chart with city
        bar = Bar("City of my friends")
        bar.add("city",city_name,city_num,width=1200,height=600,is_label_show=True,is_datazoom_show=True)
        bar.show_config()
        bar.render(r"bar_chart_city.html")
        print "Successfully written to file"

        # Geo chart with city
        city_name.append("city")
        city_num.append(0)
        geo = Geo("City of my friends", title_color="#fff",width=1200,height=600,background_color='#404a59')
        geo.add("city",city_name,city_num,visual_range=[0,200],visual_text_color="#fff",symbol_size=15,is_visualmap=True)
        geo.show_config()
        geo.render(r"geo_chart_city.html")
        print "Successfully written to file"


    def province_display(self,friends):
        province = friends.iloc[:,3]
        province_name = province.value_counts().index.tolist()
        province_num = province.value_counts().values.tolist()
        # Bar chart with province
        bar = Bar("Province of my friends")
        bar.add("province",province_name,province_num,width=1200,height=600,is_label_show=True,is_datazoom_show=True)
        bar.show_config()
        bar.render(r"bar_chart_province.html")
        print "Successfully written to file"
        # Geo chart with province
        map = Map("Province of my friends",width=1200,height=600)
        map.add("",province_name,province_num,maptype='china',is_visualmap=True,visual_text_color="#000")
        map.show_config()
        map.render(r"geo_chart_province.html")
        print "Successfully written to file"


    def run(self):
        try:
            friends = pd.read_csv("friend analysis.csv")
            self.sex_display(friends)
            self.city_display(friends)
            self.province_display(friends)

        except:
            print "RUN TIME ERROR WHEN LOADING DATA"


if __name__ == "__main__":
    begin = displayResult()
    begin.run()
