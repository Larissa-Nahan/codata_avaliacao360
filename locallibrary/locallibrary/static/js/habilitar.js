$('#id_nivel').attr('disabled', 'disabled');
$(document).on('change', '#id_efetivo', function () {
    if ($(this).prop('checked')) {
        $('#id_nivel').removeAttr('disabled');
    } else {
        $('#id_nivel').attr('disabled', 'disabled');
    }
});