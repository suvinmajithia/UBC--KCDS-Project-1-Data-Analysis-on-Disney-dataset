#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Suvin Majithia

"""

def avg_frame(frame_a,frame_b):
    """
    Given two dataframes, returns a dataframe that is combination of two dataframes along with
    avg values based upon revenue/count columns from respective dataframes
    
    Parameters
    ----------
    frame_a : pandas.core.frame.DataFrame
        The dataframe from where revenue comes
    frame_b : pandas.core.frame.DataFrame
        The dataframe from where genre count comes
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with frame_a and frame_b combined along with avg(revenue/count) column
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the frame_a does not contain inflation_adjusted_gross in the data columns
    AssertError
        If the frame_b does not contain index(count of genres) in the data columns
    
 
    """
    import pandas as pd
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(frame_a, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    if not isinstance(frame_b, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    # Tests that the the grouping column is in the dataframe
    assert 'inflation_adjusted_gross' in frame_a.columns, "The revenue column does not exist in the dataframe"
    
    # Tests that the the action column is in the dataframe
    assert 'index' in frame_b.columns, "The count column does not exist in the dataframe"
    
    # creating the main dataframe by setting up the index
    frame_revenue = frame_a.set_index('genre')
    frame_count = frame_b.set_index('genre')
    final_frame = pd.concat([frame_revenue['inflation_adjusted_gross'],frame_count['index']],axis=1)
    # Selecting the required columns from the dataframes
    frame_revenue = frame_revenue['inflation_adjusted_gross']
    frame_count = frame_count['index']
    # Calculating the average and adding the results as a column in main dataframe
    final_frame['avg_count'] = frame_revenue/frame_count
    # Returning the results                         
    return(final_frame)
    