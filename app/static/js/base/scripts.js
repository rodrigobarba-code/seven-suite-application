/**
 * Contains all the scripts for the base app running on the client side.
 *
 * @param   {object} event - The event object.
 * @returns {void}
 */
$(document).ready(function () {
    $('#delete-modal').on('show.bs.modal', function (event) {
       // Extract info from data-* attributes
       var button = $(event.relatedTarget);  // Button that triggered the modal
       // Extract info from data-* attributes
       var url = button.data('url');  // Extract info from data-url attribute
       var id = button.data('id');  // Extract info from data-id attribute
       var name = button.data('name');  // Extract info from data-name attribute
       var type = button.data('type');  // Extract info from data-type attribute
       // Extract info from data-* attributes

       // Update the modal's content
       var modal = $(this);  // Modal that triggered the event
       modal.find('#modal-type').text(type);  // Update the modal's type
       modal.find('#modal-name').text(name);  // Update the modal's name
       modal.find('#modal-id').text(id);  // Update the modal's id
       modal.find('#modal-delete-url').attr('href', url);  // Update the modal's delete url
       // Update the modal's content
    });
});
/* Contains all the scripts for the base app running on the client side. */

function deleteSelectModal(urlIn, urlOut) {
    document.getElementById('delete-selected').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        document.getElementById('total-selected').innerText = String(checkboxes.length);
    });

    document.getElementById('confirm-delete').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        const selectedIds = Array.from(checkboxes).map(cb => cb.id.replace('user-', ''));

        if (selectedIds.length > 0) {
            fetch(urlIn, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json'
                }, body: JSON.stringify({users_ids: selectedIds})
            }).then(response => {
                if (response.ok) {
                    location.href = urlOut;
                } else {
                    alert('Failed to delete users');
                }
            });
        } else {
            alert('No users selected');
        }
    });
}

function deleteAllModal(urlIn, urlOut) {
    document.getElementById('confirm-delete-all').addEventListener('click', function () {
        if (document.querySelectorAll('input[type="checkbox"]').length === 0) {
            alert('No users to delete');
        } else {
            fetch(urlIn, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json'
                }
            }).then(response => {
                if (response.ok) {
                    location.href = urlOut;
                } else {
                    alert('Failed to delete users');
                }
            });
        }
    });
}