# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx")
# print(data.head())

# import pandas as pd
# col_string = "A,D:F"
# data = pd.read_excel("multi_sheet_example.xlsx", skiprows=2, usecols=col_string)
# print(data)
# print(data.columns)

# usecols=[0,2,4,5]
# usecols=["client_id","age"]

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx")
# print(type(data))
# print(data.head())
# print(data.keys())
# print(data.values)

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=1)
# print(data.head())

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name="Economics")
# print(data.head())

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=["Clients","Economics"])
# print(type(data))


# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=[0,"Economics"])
# print(data.keys())

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=None)
# print(data.keys())

# import pandas as pd
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=None)
# print(type(data))
# for key,val in data.items():
#     print("Key:", key)       
#     print("Value:", type(val)) 
#     print(val.head())   


# import pandas as pd
# all_responses = pd.DataFrame()
# data = pd.read_excel("multi_sheet_example.xlsx",sheet_name=None)
# for df in data.values():
#   print("Adding {} rows".format(df.shape[0]))
#   all_responses = pd.concat([all_responses,df])
# print(all_responses)


#multi_sheet_example.xlsx

# import pandas as pd
# all_responses = pd.DataFrame()
# data = pd.read_excel("two_sheets_example.xlsx",sheet_name=None)
# for key,val in data.items():
#   val["sheet_name"]=key
#   all_responses = pd.concat([all_responses,val])
# print(all_responses)
# print(all_responses.sheet_name)

#By default boolean values loads as float into excel sheet and in dataframe. Since defaulting to Booleans may have 
# undesired effects like turning NA values into Trues.

# import pandas as pd
# data = pd.read_excel("boolean_values.xlsx")
# print(data)
# print(data.isna().sum())

# import pandas as pd
# data = pd.read_excel("boolean_values.xlsx")
# print(data)
# data["Credit_Card_Stress"]=data["Credit_Card_Stress"].astype("boolean")
# print(data)
# print(data.groupby("Credit_Card_Stress").sum())


# import pandas as pd
# data = pd.read_excel("boolean_values.xlsx",true_values=["YES"],false_values=["NO"])
# print(data)


# import pandas as pd
# data = pd.read_excel("datetimes_example.xlsx")
# print(data.dtypes)
# print(data.Part1StartTime.head())

# import pandas as pd
# date_cols=["Part1StartTime"]
# data = pd.read_excel("datetimes_example.xlsx",parse_dates=date_cols)
# print(data.dtypes)
# print(data.Part1StartTime.head())


# import pandas as pd
# datetime_cols = {"Part2Start": ['Part2StartDate','Part2StartTime']}
# data = pd.read_excel("datetimes_example.xlsx",parse_dates=datetime_cols)
# print(data.dtypes)
# print(data)
# print(data.Part2Start.describe())

# import pandas as pd
# data = pd.read_excel("datetimes_example.xlsx")
# print(data.dtypes)
# print(data["Part2EndTime"])
# data["Part2EndTime"] = pd.to_datetime(data["Part2EndTime"],format="%m%d%Y %H:%M:%S")
# print(data["Part2EndTime"])
# print(data.dtypes)





