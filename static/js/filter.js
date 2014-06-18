$(document).ready( function() {
    $('select').on('change',inicio);
        function inicio(){
            var id_cat = $(this).val();
            $('#datos').children().remove();
            $.getJSON('/filtro_ajax/', {'id_cat':id_cat},
            function(data){
                $.each(data, function(index, item){
                    console.log(item.pk);
                    div = '<div class="tab-content">'+
                                '<div class="tab-pane active" id="enReparacion">'+
                                    '<div class="panel panel-danger">'+
                                        '<div class"panel-heading">'+
                                            '<p>'+'Incidencia Número: '+item.fields.incidencia+'</p>'+
                                        '</div>'+
                                        '<div class="panel-body">'+
                                            '<img id="thumbnail" src='+MEDIA_URL+'/incidencias/imagen01.jpg />'+
                                            '<div id="informacion">'+
                                                '<h4>'+'Informacion'+'</h4>'+
                                                '<p>'+'Fecha de la Incidencia: '+item.fields.fecha+'</p>'+
                                                '<p>'+'Comentario del Usuario: '+item.fields.comentario+'</p>'+
                                            '</div>'+
                                        '</div>'+
                                        '<button type="button" value='+item.pk+' class="btn btn-info" >Ver Historial</button>'+
                                        '<button type="button" value='+item.pk+' class="btn btn-info" >Siguiente Estado</button>'+
                                    '</div>'+
                                '</div>'+
                            '</div>';
                    $('#datos').append(div);
                });
            });
        }
    $('body').on("click", ".btn", function (){
        var id_btn = $(this).attr('value');
        console.log(id_btn);
    });
});