-- Put this file anywhere in the lua path where the module loader can find it.
-- That may be: the folder where the script to execute is located, or
-- PATH_WHERE_LUA_IS_INSTALLED/5.1/lua/.
-- (Thanks lua for not being able of importing scripts on a parent folder.)
module(..., package.seeall)

function map(f, t)
	local t2 = {}
	for k, v in ipairs(t) do t2[k] = f(v) end
	return t2
end

function reduce(f, t)
	local r = 0
	for k, v in ipairs(t) do r = r + f(v) end
	return r
end

function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

function readlines(file)
  if not file_exists(file) then return {} end
  lines = {}
  for line in io.lines(file) do 
    lines[#lines + 1] = line
  end
  return lines
end