#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals

# Encoding is significant due to Chinese character

import os
import re
import itchat
from pandas import DataFrame


class friendAnalysis(object):

    # Count the number with different sex
    def count_sex(self,friends):
        male = female = other = 0
        # Apart from himself [begin from 1]
        for friend in friends[1:]:
            sex = friend["Sex"]
            if sex == 1:
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1
        total = len(friends[1:])
        print("Male",male,"\nFemale",female,"\nOther",other,"\nTotal",total)

    # Get variable from friends
    def get_var(self,var,friends):
        variable = []
        for friend in friends:
            value = friend[var]
            variable.append(value)
        return variable


    def run(self):
        itchat.login()
        friends = itchat.get_friends(update=True)[0:]

        self.count_sex(friends)

        NickName = self.get_var("NickName",friends)
        Sex = self.get_var("Sex",friends)
        Province = self.get_var("Province",friends)
        City = self.get_var("City",friends)
        Signature = self.get_var("Signature",friends)

        data = {"NickName":NickName, "Sex":Sex, "Province":Province,
        "City":City,"Signature":Signature}
        frame = DataFrame(data)
        # Convert dict to dataframe for writting to csv

        # Remove csv file if already exists
        if os.path.isfile("friend analysis.csv"):
            os.remove("friend analysis.csv")
        frame.to_csv("friend analysis.csv",index=True,encoding="utf-8")


if __name__ == "__main__":
    begin = friendAnalysis()
    begin.run()
    print("Friends information has been successfully extracted")
    print("Run display.py next to get the graphs")
