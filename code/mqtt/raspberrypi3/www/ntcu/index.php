
    

    

<?php
  # http://canvasjs.com/download-html5-charting-graphing-library/
  # http://tablesorter.com/docs/#Download
  
  require(dirname(__FILE__).'/config.php');
  
  $pdo = new PDO(
    sprintf(
      'mysql:host=%s;dbname=%s;port=%s;charset=%s',
      $mysqlConfig['host'],
      $mysqlConfig['name'],
      $mysqlConfig['port'],
      $mysqlConfig['charset']
    ),
    $mysqlConfig['username'],
    $mysqlConfig['password']
  );

  $sensor = array('humidty', 'temperature');

  /*
   * view as group by GROUP BY (UNIX_TIMESTAMP(`temperature`.`datetime`) DIV 600)
   * which mean 10min
   * 24hour * 60min / 10min = 144
   * to show a day dht11 value chagne need 144 result
   */
   
  # NO NEED ORDER BY id ASC
  $sql[$sensor[0]] = "SELECT * FROM mqtt.humidity_view  limit 144;";
  $sql[$sensor[1]] = "SELECT * FROM mqtt.temperature_view  limit 144;";
  
  $results = array();
  
  for($i = 0; $i < count($sensor); $i++) {
    $statement = $pdo->prepare($sql[$sensor[$i]]);
    $statement->execute();
  
    $results[$sensor[$i]] = $statement->fetchAll(PDO::FETCH_ASSOC);
  }
  
 

echo <<<HTML

	<div id="chartContainer" style="height: 300px; width: 100%;">
	</div>
  
HTML;
  
  // Show mysql query result in sorttable
  // And array_push..
  $dht_json = array();
  for($k = 0; $k < count($results); $k++){
    $dht_json[$sensor[$k]] = array();
    echo "Query result for ". $sensor[$k];
    echo "<br />".count($results[$sensor[$k]])." results"; 
    echo '<table id="'.$sensor[$k].'Table" class="tablesorter">';
    echo '<thead>';
      echo '<tr>';
        echo '<th>id</th><th>datetime</th><th>value</th>';
      echo '</tr>';
    echo '</thead>';
    echo '<tbody>';
    foreach($results[$sensor[$k]] as $value){
      //array_push($dht_json[$sensor[$k]], "{x: new Date( '". $value['datetime']. "'), y: ".$value['value']."}");
      echo '<tr><td>'.$value['id'].'</td><td>'.$value['datetime'].'</td><td>'.$value['value'].'</td></tr>';
    }
    echo '</tbody>';
    echo '</table>';
    
  }
  

  // Json of dht/temperature data
  $json_humi = "";
  $toalValue = count($results[$sensor[0]]); // ofcouse I know is ..
  $i = 0;
  foreach($results[$sensor[0]] as $value){
    //echo date('H:i', strtotime($value['datetime']));
    $json_humi .= "{x: new Date( '". $value['datetime']. "'), y: ".$value['value']."}";
    $i++;
    if($i < $toalValue)
      $json_humi .=',';
  }
  

  
  // Json of dht/humidity data
  $json_temp = "";
  $toalValue = count($results[$sensor[1]]); // ofcouse I know is ..
  $i = 0;
  foreach($results[$sensor[1]] as $value){
    // echo date('H:i', strtotime($value['datetime']));
    $json_temp .= "{x: new Date( '". $value['datetime']. "'), y: ".$value['value']."}";
    $i++;
    if($i < $toalValue)
      $json_temp .=',';
  }
  

  
 echo <<<HTML
  
  	<script type="text/javascript">
    
  $(document).ready(function() {
     $("#humidtyTable").tablesorter( {sortList: [[0,0], [1,0]]} ); 
     $("#temperatureTable").tablesorter( {sortList: [[0,0], [1,0]]} ); 
     }
  ); 

    
	window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
		{

			title:{
				text: "DHT11",
				fontSize: 30
			},
      animationEnabled: true,
			axisX:{

				gridColor: "Silver",
				tickColor: "silver",
				valueFormatString: "DD/MMM HH:mm"

			},                        
      toolTip:{
        shared:true
      },
			theme: "theme2",
			axisY: {
				gridColor: "Silver",
				tickColor: "silver"
			},
			legend:{
				verticalAlign: "center",
				horizontalAlign: "right"
			},
			data: [
			{        
				type: "line",
				showInLegend: true,
				lineThickness: 2,
				name: "Humidity",
				markerType: "square",
				color: "#F08080",
				dataPoints: [
        
HTML;

echo $json_humi;

echo <<<HTML

				]
			},
			{        
				type: "line",
				showInLegend: true,
        lineThickness: 2,
				name: "Temperture",
				color: "#20B2AA",
				lineThickness: 2,

				dataPoints: [
        
HTML;

echo $json_temp;

echo <<<HTML

				]
			}

			
			],
          legend:{
            cursor:"pointer",
            itemclick:function(e){
              if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
              	e.dataSeries.visible = false;
              }
              else{
                e.dataSeries.visible = true;
              }
              chart.render();
            }
          }
		});

chart.render();
}
</script>

HTML;

