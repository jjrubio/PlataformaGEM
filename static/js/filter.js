$(document).ready( function() {
    init();
});

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
                                '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
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
        if(id < 3){
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
                            '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                            '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                        '</div>'+
                    '</div>'+
                '</div>';
            $('#datos').append(div);
        }else{
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
                            '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                        '</div>'+
                    '</div>'+
                '</div>';
            $('#datos').append(div);
        }
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
            if(id_estado < 3){
                var div = '<div class="tab-content">'+
                        '<div class="tab-pane active" id="1">'+
                            '<div class="panel panel-danger">'+
                                '<div class"panel-heading">'+
                                    '<p>'+'Incidencia Número #'+item.fields.incidencia+'</p>'+
                                '</div>'+
                                '<div class="panel-body">'+
                                    '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                    '<div id="informacion">'+
                                        '<h4>'+'Información'+'</h4>'+
                                        '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                        '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                                '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                $('#datos').append(div);
            }else{
                var div = '<div class="tab-content">'+
                        '<div class="tab-pane active" id="1">'+
                            '<div class="panel panel-danger">'+
                                '<div class"panel-heading">'+
                                    '<p>'+'Incidencia Número #'+item.fields.incidencia+'</p>'+
                                '</div>'+
                                '<div class="panel-body">'+
                                    '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                    '<div id="informacion">'+
                                        '<h4>'+'Información'+'</h4>'+
                                        '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                        '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                $('#datos').append(div);
            }
        });
    });
});
//Boton
$('body').on("click", ".btn-info", function (){
    var id_btn = $(this).attr('value');

    $('.modal-body #admin_comment').val(id_btn);

    var id_estado = $('#myTabs li.active').attr('id');
    //Fecha actual
    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();
    var output = d.getFullYear() + '-' + ((''+month).length<2 ? '0' : '') + month + '-' + ((''+day).length<2 ? '0' : '') + day;
    var usuario = "anonimo";

    $('.modal-body #id_incidencia').val(id_btn);
    $('.modal-body #id_estado').val(id_estado);
    $('.modal-body #fecha').val(output);
    $('.modal-body #id_usuario').val(usuario);
    $('#test_modal').modal('show');
});
$('body').on("click", ".btn-primary", function (){
    var id_incidencia = $('#id_incidencia').val();
    var id_estado = $('#id_estado').val();
    var fecha_incidencia = $('#fecha').val();
    var id_usuario = $('#id_usuario').val();
    var comentario = $('#comment').val();

    $.getJSON('/update_state/', {'id_incidencia':id_incidencia, 'id_estado':id_estado, 'fecha_incidencia':fecha_incidencia, 'id_usuario':id_usuario, 'comentario':comentario},
    function(data){
        $('#datos').children().remove();
        $.each(data, function(index, item){
            if(id_estado < 3){
                var div = '<div class="tab-content">'+
                        '<div class="tab-pane active" id="1">'+
                            '<div class="panel panel-danger">'+
                                '<div class"panel-heading">'+
                                    '<p>'+'Incidencia Número #'+item.fields.incidencia+'</p>'+
                                '</div>'+
                                '<div class="panel-body">'+
                                    '<img id="thumbnail" src='+MEDIA_URL+item.fields.imagen_path+'/>'+
                                    '<div id="informacion">'+
                                        '<h4>'+'Información'+'</h4>'+
                                        '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                        '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                                '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                $('#datos').append(div);
            }else{
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
                                '<a href="/historial/'+item.pk+'/"><button id="btn-historial" type="button" class="btn btn-info">Ver Historial</button></a>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                $('#datos').append(div);
            }
        });
    });

    $('#test_modal').modal('hide');
    $('.modal-body #comment').val("");
});

$('body').on("click", ".btn-default", function (){
    $('#test_modal').modal('hide');
});
$('body').on("click", "#btn-historial", function (){       
    $('#test_modal').modal('hide');
});
