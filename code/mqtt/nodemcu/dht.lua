
-- global variable...
DHT_PIN = 1 -- _G.DHT_PIN
DHT_STATUS = 0
DHT_TEMP = "NULL"
DHT_HUMI = "NULL"


function readDHT(dht_pin)
  dht_pin = dht_pin or DHT_PIN
  DHT_STATUS,temp,humi,temp_decimial,humi_decimial = dht.read(dht_pin)
  if( DHT_STATUS == dht.OK ) then
    DHT_TEMP = temp
    DHT_HUMI = humi
    --print("DHT Temperature = "..temp.." grdC  ".."Humidity = "..humi.." %")
    --print("DHT Temperature = "..DHT_TEMP.." grdC  ".."Humidity = "..DHT_HUMI.." %")
    return temp, humi
  elseif( DHT_STATUS == dht.ERROR_CHECKSUM ) then
    return false, "DHT Checksum error."
    --print( "DHT Checksum error." );
  elseif( DHT_STATUS == dht.ERROR_TIMEOUT ) then
    --print( "DHT Time out." );
    return false, "DHT Time out."
  end
end







