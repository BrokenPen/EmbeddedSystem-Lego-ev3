

-- 2016/12/22 23:11 updated
--   fix : use DHT global variable 

-- DHT web page
srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
    conn:on("receive", function(client,request)
        local buf = "<html><head><title>DHT11 Sensor</title></head><body>";
        buf = buf.."DHT11 current values"
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");
        end
        local _GET = {}
        if (vars ~= nil)then
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*h") do
                _GET[k] = v
            end
        end

 
        
        if(DHT_STATUS == dht.ERROR_TIMEOUT) then
          buf = buf.."<br /> Error : DHT Checksum error.<br /> "
        elseif(DHT_STATUS == dht.ERROR_TIMEOUT) then
          buf = buf.."<br /> Error : DHT Time out.<br /> "
        elseif(DHT_STATUS == dht.OK ) then
          buf = buf.."<br />Temperature : "..DHT_TEMP.."<br />Humidity : "..DHT_HUMI
        end

        buf = buf.."</body></html>"
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)



