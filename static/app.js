$(document).ready(function() {
    $('#punctuate-form').submit(function(event) {
        event.preventDefault();
        var text = $('#text-input').val();
        $.post('/punctuate', {text: text}, function(data) {
            $('#result').html(data);
        });
    });
});
