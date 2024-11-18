using CSV
using DataFrames
using Statistics

csv_file = CSV.File("fmtemp.csv")
df = DataFrame(csv_file)


names(df)
returns = diff(Matrix(df); dims = 1) ./ Matrix(df[1:end-1, :])

r = vec(Statistics.mean(returns; dims = 1))
Q = Statistics.cov(returns)

using JuMP
import Ipopt
model = Model(Ipopt.Optimizer)

@variable(model, x[1:50] >= 0)
@objective(model, Min, x' * Q * x)
@constraint(model, sum(x) <= 100)
@constraint(model, r' * x >= 5)
optimize!(model)

@assert is_solved_and_feasible(model)
solution_summary(model)

value.(x)