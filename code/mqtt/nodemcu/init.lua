-- Track what timer id I have used
--[[
  In init.lua : readDHT() use ID : 2
  In dht_mqtt : use ID : 1 3
]]--


-- part of setup
dofile("nodemcu_info.lua") -- first display the info
dofile("wifi.lua") -- second connect...


-- include some function
dofile("dir.lua") -- listFiles() 
dofile("dht.lua") -- function() read dht11 temp+humdi.. + webserver
dofile("del_all.lua") -- for del all lua.. except del_all.lua

function startup()
    if file.open("init.lua") == nil then
      print("init.lua deleted")
    else
      print("Running")
      file.close("init.lua")

      print("Detect the DHT sensor value every second, on timer 2.")
      tmr.alarm(0, 1 * 1000, tmr.ALARM_AUTO, 
            function() temp = readDHT()
      end)
      
      
      dofile("web.lua") -- the web page     
      dofile("dht_mqtt.lua")
      end
end




