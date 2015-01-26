
$(".form-control").change(function(e){

     var categoria = $('.form-control').val();

    $.getJSON('/data_stats/', {'categoria': categoria}, function(data) {
            var aceptadas = 0;
            var rechazadas = 0;
            var enviadas = 0;
            var reparadas = 0;
            var solucionadas = 0;
            $.each(data, function(index, item){
                if(item == 4){
                    rechazadas++;
                }else{
                    aceptadas++;
                }

                if(item == 1){
                    enviadas++;
                }else if(item == 2){
                    reparadas++;
                }else if(item == 3){
                    solucionadas++;
                }
            });
            var total1  = aceptadas + rechazadas;
            var pAceptadas = aceptadas / total1;
            var pRechazadas = rechazadas / total1;
            var resultado1 = [["Aceptadas", pAceptadas], ["Rechazadas", pRechazadas]];

            var total2 = enviadas+reparadas+solucionadas;
            var pEnviadas = enviadas / total2;
            var pReparadas = reparadas / total2;
            var pSolucionadas = solucionadas / total2;
            var resultado2 = [["Enviadas", pEnviadas], ["Reparadas", pReparadas], ["Solucionadas", pSolucionadas]];

            $('#grafico1').highcharts({
                chart: {
                    plotBackgroundColor: '#f7f3f0',
                    plotBorderWidth: 1,
                    plotShadow: false
                },
                title: {
                    text: 'Gráfico de Incidencias Aceptadas Vs Rechazadas'
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                            style: {
                                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                            }
                        }
                    }
                },
                series: [{
                    type: 'pie',
                    name: 'Porcentaje de incidencias',
                    data: resultado1,
                }]
            });

            $('#grafico2').highcharts({
                chart: {
                    plotBackgroundColor: '#f7f3f0',
                    plotBorderWidth: 1,
                    plotShadow: false
                },
                title: {
                    text: 'Estado de Incidencias Aceptadas'
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                            style: {
                                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                            }
                        }
                    }
                },
                series: [{
                    type: 'pie',
                    name: 'Porcentaje de incidencias',
                    data: resultado2,
                }]
            });
    });




});

