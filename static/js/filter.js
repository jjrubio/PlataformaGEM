$(document).ready( function() {
    init();

    function init(){
        var id = 1;
        $('#datos').children().remove();
        $.getJSON('/filtro_tabs/', {'id_estados':id},function(data){
            $.each(data, function(index, item){
                var div = '<div class="tab-content">'+
                            '<div class="tab-pane active" id="1">'+
                                '<div class="panel panel-danger">'+
                                    '<div class"panel-heading">'+
                                        '<p>'+'Incidencia Número: #'+item.fields.incidencia+'</p>'+
                                    '</div>'+
                                    '<div class="panel-body">'+
                                        '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                        '<div id="información">'+
                                            '<h4>'+'Informacion'+'</h4>'+
                                            '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                            '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                        '</div>'+
                                    '</div>'+
                                    '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                                '</div>'+
                            '</div>'+
                        '</div>';
                $('#datos').append(div);
            });
        });
    }

    $('#myTabs li').click(function () {
      var id = $(this).attr('id');
      $('#datos').children().remove();
      $.getJSON('/filtro_tabs/', {'id_estados':id},function(data){
        $.each(data, function(index, item){
            var div = '<div class="tab-content">'+
                        '<div class="tab-pane active" id="1">'+
                            '<div class="panel panel-danger">'+
                                '<div class"panel-heading">'+
                                    '<p>'+'Incidencia Número: #'+item.fields.incidencia+'</p>'+
                                '</div>'+
                                '<div class="panel-body">'+
                                    '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                    '<div id="información">'+
                                        '<h4>'+'Informacion'+'</h4>'+
                                        '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                        '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
            $('#datos').append(div);
        });
      });
    });
    //Select
    $('select').change(function(){
        var id_cat = $(this).val();
        var id_estado = $('#myTabs li.active').attr('id');
        $('#datos').children().remove();
        $.getJSON('/filtro_tabs_selec/', {'id_estado': id_estado, 'id_cat': id_cat},
        function(data){
            $.each(data, function(index, item){
                var div = '<div class="tab-content">'+
                            '<div class="tab-pane active" id="1">'+
                                '<div class="panel panel-danger">'+
                                    '<div class"panel-heading">'+
                                        '<p>'+'Incidencia Número #:'+item.fields.incidencia+'</p>'+
                                    '</div>'+
                                    '<div class="panel-body">'+
                                        '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                        '<div id="informacion">'+
                                            '<h4>'+'Información'+'</h4>'+
                                            '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                            '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                        '</div>'+
                                    '</div>'+
                                    '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                                '</div>'+
                            '</div>'+
                        '</div>';
                $('#datos').append(div);
            });
        });
    });
    //Boton
    $('body').on("click", ".btn", function (){
        var id_btn = $(this).attr('value');
        console.log(id_btn);
        $('.modal-body #admin_comment').val(id_btn);
        $('#test_modal').modal('show');
    });
    $('body').on("click", ".btn-primary", function (){
        $('#test_modal').modal('hide');
    });
    $('body').on("click", ".btn-default", function (){       
        $('#test_modal').modal('hide');
    });
});                                    
