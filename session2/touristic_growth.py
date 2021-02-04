# encoding: utf-8

##################################################
# This script shows how to collect data from remote sources and create bar plots
# Find extra documentation for the source code here:
# https://github.com/diegopajarito/COVID19_datavis
# Note: the project does not have changes after mid 2019
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2021, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gdp_growth = pd.read_csv('../data/calendar.csv')

# Using the following list, we will create a subset to explore summary statistics
date = ('8/25/2020')


# First, we will create an histogram for the values in 2019

# matplotlib histogram
plt.hist(gdp_growth['price'], color='yellow', edgecolor='black', bins=10)
plt.show()

