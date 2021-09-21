https://jsfiddle.net/dt6c9jev/


        var ctx = document.getElementById("Chart").getContext("2d");
        var myChart = new Chart(ctx, {
            type: "scatter", // scatter, line ...
            data: {
                labels: {{labels | safe}},
                datasets: [
                    {
                        label: "Data points",
                        data: {{ values | safe}},
                        fill: false,
                        pointStyle: "circle",
                        borderColor: "rgb(75, 192, 192)",
                        lineTension: 0.1
                    }
                ]
            },
            options: {
				responsive: true,
				scales: {
					y: {
						title: {
							display: true,
							text: 'Height'
						}
					},
					x: {
						title: {
							display: true,
							text: 'Age'
						}
					},
				}
			}
        });


        var mixedChart = new Chart(ctx, {
			data: {
				datasets: [{
					type: 'bar',
					label: 'Bar Dataset',
					data: [10, 20, 30, 40],
					borderColor: 'rgb(255, 99, 132)',
    				backgroundColor: 'rgba(255, 99, 132, 0.2)'
				}, {
					type: 'line',
					label: 'Line Dataset',
					data: [50, 50, 50, 50],
					fill: false,
    				borderColor: 'rgb(54, 162, 235)'
				}],
				labels: ['January', 'February', 'March', 'April']
			},
			options: {
				responsive: true,
			}
		});



		var myChart = new Chart(ctx, {
			type: 'scatter',
			data: {
				datasets: [
					{
						label: 'Chart 1',
						data: [{x: 1, y: 2}, {x: 2, y: 4}, {x: 3, y: 8},{x: 4, y: 16}],
						showLine: true,
						fill: false,
						borderColor: 'rgba(0, 200, 0, 1)'
					},
					{
						label: 'Chart 2',
						data: [{x: 1, y: 3}, {x: 3, y: 4}, {x: 4, y: 6}, {x: 6, y: 9}],
						showLine: true,
						fill: false,
						borderColor: 'rgba(200, 0, 0, 1)'
					}
				]
			},
			options: {
				tooltips: {
				mode: 'index',
				intersect: false,
				},
				hover: {
				mode: 'nearest',
				intersect: true
				},
				scales: {
				yAxes: [{
					ticks: {
					beginAtZero:true
					}
				}]
				},
			}
		});

		









		data: [{x: 1, y: 2}, {x: 2, y: 4}, {x: 3, y: 8},{x: 4, y: 16}],

		data: [{x: 1, y: 3}, {x: 3, y: 4}, {x: 4, y: 6}, {x: 6, y: 9}],
		
		var mixedChart = new Chart(ctx, {
			data: {
				datasets: [{
					type: 'line',
					label: 'Bar Dataset',
					data: {{ values | safe}},
				}, {
					type: 'line',
					label: 'Line Dataset',
					data: {{ values | safe}},
					fill: false,
				}],
				labels: {{labels | safe}},
			},
			options: {
				responsive: true,
			}
		});
		
		
		
		
		var myChart = new Chart(ctx, {
			data: {
				labels: {{labels | safe}},
				datasets: [
					{
						type: "scatter", // scatter, line ...
						label: "Data points",
						data: {{ values | safe}},
						fill: false,
						pointStyle: "circle",
						borderColor: "rgb(75, 192, 192)",
						lineTension: 0.1
					},
					{
						type: "line", // scatter, line ...
						label: "Linear model",
						data: {{ y_line | safe}},
						fill: false,
						borderColor: "rgb(113, 232, 95)",
						lineTension: 0.1
					}					
				]
			},
			options: {
				responsive: true,
				legend  : {
					display: false
				},
				elements: {
					point: {
						radius : 3,
						display: true
					}
				},
				scales: {
					y: {
						title: {
							display: true,
							text: 'Height'
						}
					},
					x: {
						title: {
							display: true,
							text: 'Age'
						}
					},
				}
			}
		});		