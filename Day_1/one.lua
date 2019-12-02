-- Advent of Code 2019 - Day 1

-- Fuel
local funcs = require "custom.functions"

mass = funcs.map(tonumber, funcs.readlines("modules.txt"))
fuel = funcs.map(function(e) return math.floor(e / 3) - 2 end, mass)
total_fuel = funcs.reduce(function(x) return x end, fuel)

print("Total fuel needed: " .. tostring(total_fuel))
