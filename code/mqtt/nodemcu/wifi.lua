wifi.sta.disconnect()

print("set up wifi mode")
wifi.setmode(wifi.STATION)
wifi.sta.config("BROKENPEN-RPI","rpiBROKENPEN",0)
wifi.sta.connect()
tmr.alarm(1, 1000, tmr.ALARM_AUTO, function() 
    if wifi.sta.getip()== nil then 
        print("IP unavaiable, Waiting...") 
    else 
        tmr.stop(1)
        print("Config done, IP is "..wifi.sta.getip())
        print("You have 5 seconds to abort Startup")
        print("Waiting...")
        tmr.alarm(0,5000,tmr.ALARM_SINGLE,startup)
    end 
 end)

