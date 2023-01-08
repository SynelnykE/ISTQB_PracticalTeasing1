#that converts a date formatted as MM/DD/YYYY to YYYY-DD-MM

import datetime

def format_date(str_date): 
    if str_date ==  "%m/%d/%Y": 
        return datetime.datetime.strptime(str_date, "%m/%d/%Y").strftime("%Y-%d-%m")
    else:
        return datetime.datetime.strptime(str_date, "%d/%m/%Y").strftime("%Y-%d-%m")

print(format_date("13/05/2021"))

# format_date("11/12/2019") ➞ "2019-12-11"
# format_date("12/31/2019") ➞ "2019-31-12"
# format_date("01/15/2019") ➞ "2019-15-01"
# format_date("13/05/2021") == "2021-05-13"