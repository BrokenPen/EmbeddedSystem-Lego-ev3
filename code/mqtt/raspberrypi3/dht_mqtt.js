

var mqtt_url       = 'mqtt://192.168.42.1';
var mqtt_subscribe = ['/mcu/#'];
//var mqtt_subscribe = ['/mcu/nodemcu/sensor/dht11/#']

var mqtt_ = []
mqtt_['keeplive'] = 160
// mqtt_["reschedulePings"] = true
mqtt_['clienId'] = 'raspberrypi3_'+ Math.random().toString(16).substr(2, 8)
// mqtt_['protocolId']      = 'MQTT'
// mqtt_['protocolVersion'] = 4
// mqtt_['clean'] = true
// mqtt_['reconnectPeriod' = 1000
// mqtt_['connectPeriod']  = 1000
// mqtt_['connectTimeout'] = 30 * 1000
mqtt_['username'] = 'raspberrypi3'
mqtt_['password'] = 'formosa'
// mqtt_['incomingStore'] = 'file'
// mqtt_['outgoingStore'] = 'file2'
// mqtt_['queueQoSZero']  = true
mqtt_['will'] = []
mqtt_['will']['topic']   = 'sbc/raspberrypi3'
mqtt_['will']['payload'] = 'offline'
mqtt_['will']['qos']     = 1
mqtt_['will']['retain']  = true

var mqtt       = require('mqtt')
var client     = mqtt.connect(mqtt_url, mqtt_)

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '192.168.42.1',
  user     : 'raspberrypi3',
  password : 'formosa',
  database : 'mqtt'
});
connection.connect();

var microtime = require('microtime')
var lastInsert_humi = 0 
var lastInsert_temp = 0


client.on('connect', function () {
  client.subscribe(mqtt_subscribe[0])
  //client.publish('/sbc/raspberrypi3', 'Hello')
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log('Recevie at : '+Date())

  console.log(''+topic+':')
  console.log(message.toString())

  if(topic == '/mcu/nodemcu/sensor/dht11/humidity'){    
    insertIntoDB('humidity', message.toString()) 
  } else if(topic == '/mcu/nodemcu/sensor/dht11/temperature'){
    insertIntoDB('temperature', message.toString())
  }
  
  //client.end()
})


function insertIntoDB(table, value) {

  //insert every 5second
  if (table == 'humidity'){
    if (microtime.now() / 1000000 - lastInsert_humi < 15){
       return
    }
    else{
       lastInsert_humi = microtime.now() / 1000000
    }
  }

  if (table == 'temperature'){ 
    if (microtime.now() / 1000000 - lastInsert_temp < 15){
       return
    }
    else{
       lastInsert_temp = microtime.now() / 1000000
    }
  }

  console.log(Date())  
  var query = connection.query('INSERT INTO '+table+' (value) VALUES (?)', value, function(err, result) {
  // Neat!
});
  console.log(query.sql); 
  //connection.end();
}
