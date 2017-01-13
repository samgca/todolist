$(document).ready(function(){

    var grid = $('.packery-container');

    grid.imagesLoaded( function () {
        grid.packery({
            columnWidth: '.item',
            itemSelector: '.item',
            percentPosition: true,
            transitionDuration: '0.5s',
            gutter: 0,
        });
    });

    $('.open_delete_modal').on('click', function(event) {
        note_id = $( this ).attr('data-link');
        $("#delete_note_link").attr('href', note_id);
        $('#delete_note_modal').modal('show');
    });

});
