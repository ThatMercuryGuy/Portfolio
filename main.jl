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
import MultiObjectiveAlgorithms as MOA
import Ipopt

model = Model(() -> MOA.Optimizer(Ipopt.Optimizer))
set_optimizer_attribute(model, MOA.Algorithm(), MOA.EpsilonConstraint())
set_optimizer_attribute(model, MOA.SolutionLimit(), 50)
set_silent(model)

@variable(model, x[1:50] >= 0)
@constraint(model, sum(x) <= 1000)
@expression(model, variance, x' * Q * x)
@expression(model, expected_return, r' * x)
# We want to minimize variance and maximize expected return, but we must pick
# a single objective sense `Min`, and negate any `Max` objectives:
@objective(model, Min, [variance, -expected_return])
optimize!(model)
@assert termination_status(model) == OPTIMAL
solution_summary(model)

scalar_return = value(r' * x)
scalar_variance = value(x' * Q * x)

using Plots
using StatsPlots

objective_space = Plots.hline(
    [scalar_return];
    label = "Single-objective solution",
    linecolor = :red,
)
Plots.vline!(objective_space, [scalar_variance]; label = "", linecolor = :red)
Plots.scatter!(
    objective_space,
    [value(variance; result = i) for i in 1:result_count(model)],
    [value(expected_return; result = i) for i in 1:result_count(model)];
    xlabel = "Variance",
    ylabel = "Expected Return",
    label = "",
    title = "Objective space",
    markercolor = "white",
    markersize = 5,
    legend = :bottomright,
)
for i in 1:result_count(model)
    y = objective_value(model; result = i)
    Plots.annotate!(objective_space, y[1], -y[2], (i, 3))
end

decision_space = StatsPlots.groupedbar(
    vcat([value.(x; result = i)' for i in 1:result_count(model)]...);
    bar_position = :stack,
    label = names(df),
    xlabel = "Solution #",
    ylabel = "Investment (\$)",
    title = "Decision space",
)
Plots.plot(objective_space, decision_space; layout = (2, 1), size = (600, 600))