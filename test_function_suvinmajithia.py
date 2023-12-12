#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Suvin Majithia

This function creates a helper data to test the sample script created for 
the sample solution to the Python Programming for Data Science project.
"""

from project_function import avg_frame
import pandas as pd

def test_custom_agg():

    # Create helper data and write tests for the function
    raw_1 = {'genre': ['Action', 'Adventure'], 
           'index': [5, 10] }

    raw_2 = {'genre': ['Action', 'Adventure'], 
           'inflation_adjusted_gross': [100000,50000] }
    
    helper_data1 = pd.DataFrame.from_dict(raw_1)
    helper_data2 = pd.DataFrame.from_dict(raw_2)
    res = avg_frame(helper_data2,helper_data1)

    assert res.shape == (2,3)
    assert list(res['avg_count']) == [20000, 5000]
   