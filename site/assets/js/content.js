function getChart() {

		var Graph1 = {
			labels : ["January","February","March","April","May","June","July"],
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					data : [25,29,20,21,26,25,20]
				},
			]
			
		}

    var Graph2 = {
			labels : ["January","February","March","April","May","June","July"],
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					data : [35,39,30,31,36,35,30]
				},
			]
			
		}

   var Graph3 = {
			labels : ["January","February","March","April","May","June","July"],
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					data : [45,49,40,41,46,45,40]
				},
			]
			
		} 

	var BuildG1 = new Chart(document.getElementById("graph1").getContext("2d")).Line(Graph1);
  var BuildG2 = new Chart(document.getElementById("graph2").getContext("2d")).Line(Graph2);
  var BuildG3 = new Chart(document.getElementById("graph3").getContext("2d")).Line(Graph3);
}
