# lego-sensor

MINDSTORMS Compatible Sensors
     
## connect the ev3 sensor

| port | kernel  | sensor |
|------|---------|--------|
| in1  | sensor0 | touch | 
| in2  | sensor1 | gyro |
| in3  | sensor2 | color |
| in4  | sensor3 | ultuasound |

### listing current connected sensor

     cd /sys/class/lego-sensor/
     ls 

![](./lego-sensor/01-connected-sensor.jpg)
![](./lego-sensor/03-sys-class-lego-sensor.png)

---

### sensor0 - touch sensor

let check  sensor0

     cd /sys/class/lego-sensor/sensor0
     ls
     grep "" *
     
![](./lego-sensor/07-sys-class-lego-sensor-sensor0-in4-ev3--touch.png)

arrocding to the `driver_name`, this sensor is `lego-ev3-touch` attach on `in4`, in `TOUCH` `mode` as `value`:`0` which mean pull up.

---

### sensor1 - gyro sensor

let check sensor1

     cd /sys/class/lego-sensor/sensor1
     ls
     grep "" *
     
![](./lego-sensor/09-sys-class-lego-sensor-sensor1-in3-ev3-gyro.png)

arrocding to the `driver_name`, this sensor is `lego-ev3-gyro` attach on `in3`, in `GYRO-ANG` `mode` as `value`:`-8` which mean negative 8 degree.

---

### sensor2 - color sensor

let check sensor2

     cd /sys/class/lego-sensor/sensor2
     ls
     grep "" *
     
![](./lego-sensor/11-sys-class-lego-sensor-sensor2-ev3-color.png)

arrocidng to the `driver_name`, this sensor is `lego-ev3-color` attach on `in2`, in `COLOR-REFLECT` `mode` as `value`:`1` and `unit` as `pict`

---

### sensor3 - ultrasound sensor

let check sensor3

   
    cd /sys/class/lego-sensor/sensor3
    ls
    grep "" *
    
![](./lego-sensor/13-sys-class-lego-sensor-sensor3-ev3-us.png)

arrocding to the `driver_name`, this sensor is `lego-ev3-us` which mean ultrasound sensor attach on `in1`, in `US-DIST-CM` `mode` as `value`: `2550` which mean nothing in front of the sensor. `2550` is the maximum value...

---

#### gyro sensor

change gyro sensor in different mode, change to gyro-cal

![](/home/alan/Programming/git/EmbeddedSystem-Lego-ev3/picture/lego-sensor/31-sys-class-lego-sensor-gyro-cal.png) 

change mode to gyro-rate

![](/home/alan/Programming/git/EmbeddedSystem-Lego-ev3/picture/lego-sensor/33-sys-class-lego-sensor-gyro-rate.png) 

change mode 

![](/home/alan/Programming/git/EmbeddedSystem-Lego-ev3/picture/lego-sensor/35-sys-class-lego-sensor-gyro-all-01.png) 

![](/home/alan/Programming/git/EmbeddedSystem-Lego-ev3/picture/lego-sensor/37-sys-class-lego-sensor-gyro-all-02.png) 



#### ultrasound sensor

#### color sensor


## Useful link

http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensors.html

http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensors.html#sysfs

---

last modified : Saturday, 06. May 2017 06:22PM 

