var map;
  var markersArray = [];
  var activeWindow;

  function RefreshMapControl(controlDiv, map) {

    controlDiv.style.padding = '5px';

    // Set CSS for the control border
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = 'white';
    controlUI.style.borderStyle = 'solid';
    controlUI.style.borderWidth = '2px';
    controlUI.style.cursor = 'pointer';
    controlUI.style.textAlign = 'center';
    controlUI.title = 'Click para recargar la el mapa';
    controlDiv.appendChild(controlUI);

    // Set CSS for the control interior
    var controlText = document.createElement('div');
    controlText.style.fontFamily = 'Arial,sans-serif';
    controlText.style.fontSize = '12px';
    controlText.style.paddingLeft = '4px';
    controlText.style.paddingRight = '4px';
    controlText.innerHTML = '<b>Recargar mapa</b>';
    controlUI.appendChild(controlText);

    google.maps.event.addDomListener(controlUI, 'click', function() {
          for (var i = 0; i < markersArray.length; i++) {
              markersArray[i].setMap(null);
            }
          markersArray = [];
          initialize();
    });

  }

  $(document).ready( function() {

      var myLatlng = new google.maps.LatLng(-2.20244372409651,-79.89777486508177);
      var mapOptions = {
          zoom: 14,
          center: myLatlng
      };

      map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

      var refreshMapControlDiv = document.createElement('div');
      var refreshMapControl = new RefreshMapControl(refreshMapControlDiv, map);

      refreshMapControlDiv.index = 1;
      map.controls[google.maps.ControlPosition.TOP_CENTER].push(refreshMapControlDiv);

      initialize();

  });


  function initialize(){
      $.get('/marcadores-sin-revisar/', function(data) {

          $.each(data, function(marker) {
              plotPoint(data[marker].inc_code,
                             data[marker].inc_usuario,
                             data[marker].inc_categoria,
                             data[marker].inc_coordenada,
                             data[marker].inc_direccion,
                             data[marker].inc_comentario,
                             data[marker].inc_fecha,
                             MEDIA_URL+data[marker].inc_evidencia,
                             data[marker].inc_estado);

          });

      });
  }


  //    Posiciona un marcador segun los datos enviados
  function plotPoint(codigo, usuario, categoria, coordenada, direccion, comentario, fecha, imagen, estado)
  {
      var iconMarker;
      var infoMarker;

      infoMarker = '<div class=\'bubbleMap\'>'+
                                 '<span><i>'+comentario+'</i></span>'+
                                 '<hr/>'+
                                 '<i class=\'fa fa-male\'> '+usuario+'</i>'+
                                 '<i class=\'fa fa-slack pull-right\'> '+codigo+'</i>'+
                          '</div>';

      switch (categoria) {
          case "Construcción":
              iconMarker = STATIC_URL + 'img/marcadores/construccion.png';
              break;
          case "Limpieza / Reciclaje":
              iconMarker = STATIC_URL + 'img/marcadores/reciclaje.png';
              break;
          case "Medio Ambiente":
              iconMarker = STATIC_URL + 'img/marcadores/ambiente.png';
              break;
          case "Servicio Técnico":
              iconMarker = STATIC_URL + 'img/marcadores/tecnico.png';
              break;
          case "Policía":
              iconMarker = STATIC_URL + 'img/marcadores/policia.png';
              break;
          case "Otros":
              iconMarker = STATIC_URL + 'img/marcadores/otros.png';
              console.log("aqui");
              break;
      }

      var myLatlng = new google.maps.LatLng(coordenada.split(",")[0], coordenada.split(",")[1]);
      var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          icon: iconMarker,
      });
      markersArray.push(marker);
      var infowindow = new google.maps.InfoWindow({
          content: infoMarker
      });
      google.maps.event.addListener(marker, 'click', function() {
          if(activeWindow != null){
              activeWindow.close();
          }
          infowindow.open(map,marker);
          // infowindow.attr("width",200);
          activeWindow = infowindow;
          $( "#img-map").removeClass( "col-lg-12" ).addClass( "col-lg-8" );
          $( "#incidence").removeClass( "hidden" ).addClass( "show" );
          $(".img-incidence").attr("src",imagen);
          $(".type-incidence").text(" " + categoria);
          $(".description-incidence i:first-child").text(" " + fecha);
          $(".description-incidence i:nth-child(2)").text(" " + usuario);
          $(".description-incidence span:nth-child(6)").text(" " + direccion);
          $(".description-incidence span:nth-child(10)").text(" " + comentario);
          $(".description-incidence span:nth-child(14)").text(" " + estado);
          $(".description-incidence i:last-child").text(" " + codigo);
      });
  }


  //    Cerrar descripción de la incidencia
  $(".close").on("click",function(){
      $( "#img-map").removeClass( "col-lg-8" ).addClass( "col-lg-12" );
      $( "#incidence").removeClass( "show" ).addClass( "hidden" );
      activeWindow.close();
      google.maps.visualRefresh = true;
  });