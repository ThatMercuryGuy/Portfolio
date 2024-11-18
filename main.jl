using CSV
using DataFrames
using Statistics

csv_file = CSV.File("temp.csv")
df = DataFrame(csv_file)


names(df)