-- Advent of Code 2019 - Day 1

-- Fuel
local funcs = require "custom.functions"

mass = funcs.map(tonumber, funcs.readlines("modules.txt"))

function f(e) return math.floor(e / 3) - 2 end

fuel = funcs.map(f, mass)
fuelOfFuel = funcs.map(f, fuel)

while math.max(unpack(fuelOfFuel)) > 0 do
	for i in ipairs(fuel) do fuel[i] = fuel[i] + fuelOfFuel[i] end
	fuelOfFuel = funcs.map(function(x) if f(x) > 0 then return f(x) else return 0 end end, fuelOfFuel)
end

total_fuel = funcs.reduce(function(x) return x end, fuel)

print("Total fuel needed: " .. tostring(total_fuel))
