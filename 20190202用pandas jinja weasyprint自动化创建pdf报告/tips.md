thank you for this great article!
By the way, putting any number of DataFrames on one excel sheet is not so complicated task and can be achieved by using Pandas only. It can be done like this:
writer = pd.ExcelWriter(file_name)
df1.to_excel(writer, sheet_name, startcol=0)
df2.to_excel(writer, sheet_name, startcol=5)
df3.to_excel(writer, sheet_name, startcol=10)
[writer.save](http://disq.us/url?url=http%3A%2F%2Fwriter.save%3AJ6aqk0Aic-Ex64lHU9GqiU6ANs0&cuid=3227818)()

"startcol" parameter is the one which allows us to position dataframe on excel sheet. You can calculate it based on number of columns in dataframes. It is possible to define "startrow" as well if needed.