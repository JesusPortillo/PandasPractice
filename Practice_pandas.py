#Nombre: Jesus David Portillo Villa
#ID: 324718
#Email: jesus.portillo@upb.edu.co

import pandas as pd
#1
data = pd.read_csv("netflix_titles.csv")
print(data)
#2
print(data.tail())
#3
print(data.info())
#4
data.to_excel("Netflix_list.xlsx", sheet_name="títulos")
#5
segmented_df = data[["type", "duration", "description", "country"]]
print(segmented_df)
#6
movies = data[data["type"] == "Movie"]
separate_duration_movies = movies["duration"].str.split(expand=True).dropna()
movies.insert(4,"durationIntMovies", separate_duration_movies[0].astype(int))
filtered_by_more_than_100 = movies[movies["durationIntMovies"] > 100]
print(filtered_by_more_than_100)
#7
series = data[data["type"] == "TV Show"]
separate_duration_series = series["duration"].str.split(expand=True).dropna()
series.insert(5, "durationIntSeries", separate_duration_series[0].astype(int))
filtered_by_more_than_3 = series[series["durationIntSeries"] > 3]
print(filtered_by_more_than_3)
#8
print(data[["type", "title"]])
#9
print(data.loc[:, "director"])
print(data.iloc[:, 4])
#10
data["show_id"] = data["show_id"].replace({"s1":"1","s2":"2","s3":"3","s4":"4","s5":"5"})
data["show_id"] = data["show_id"].replace({"s8803":"8803","s8804":"8804","s8805":"8805","s8806":"8806","s8807":"8807"})
print(data)