import pandas

data = pandas.read_csv("french_words.csv")
new_data = data.to_dict(orient="records")
print(new_data)

