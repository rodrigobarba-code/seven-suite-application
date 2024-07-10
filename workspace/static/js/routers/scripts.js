$(document).ready(function () {
    $('#routers-table').DataTable(
        {
            responsive: true
        }
    );
});

document.addEventListener('DOMContentLoaded', function () {
    var popoverTrigger = document.getElementById('textInput');
    var popover = new bootstrap.Popover(popoverTrigger);

    document.addEventListener('click', function (event) {
        if (!popoverTrigger.contains(event.target)) {
            popover.hide();
        }
    });

    popoverTrigger.addEventListener('click', function (event) {
        event.stopPropagation();  // Para evitar que el clic en el input cierre el popover inmediatamente
        popover.show();
    });
});
