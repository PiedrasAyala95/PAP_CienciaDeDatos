# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:41:12 2020

@author: Piedras
"""

from wwo_hist import retrieve_hist_data
frequency = 1
start_date = "01-01-2009"
end_date = "21-02-2020"
api_key = "5499e7836a264d9597e165605202202"

location_list = ["Ameca"]

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)