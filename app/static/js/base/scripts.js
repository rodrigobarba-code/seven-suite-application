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

/**
 * Function to delete selected items in a table using a modal.
 *
 * @param   {string} urlIn - The URL to send the delete request to.
 * @param   {string} urlOut - The URL to redirect to after a successful delete
 * @param   {string} type - The type of item to delete.
 * @returns {void}
 */
function deleteSelectModal(urlIn, urlOut, type) {
    document.getElementById('delete-select').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        document.getElementById('total-select').innerText = String(checkboxes.length);
        document.getElementById('select-modal-type').innerText = type;
    });

    document.getElementById('confirm-delete-select').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        const selectedIds = Array.from(checkboxes).map(cb => cb.id.replace(type + '-', ''));

        if (selectedIds.length > 0) {
            fetch(urlIn, {
                method: 'POST', headers: {
                    'Content-Type': 'application/json'
                }, body: JSON.stringify({items_ids: selectedIds})
            }).then(response => {
                if (response.ok) {
                    location.href = urlOut;
                } else {
                    alert('Failed to delete users');
                }
            });
        } else {
            alert('No ' + type + 's to delete');
        }
    });
}
/* Function to delete selected items in a table using a modal. */

/**
 * Function to delete all items in a table using a modal.
 *
 * @param   {string} urlIn - The URL to send the delete request to.
 * @param   {string} urlOut - The URL to redirect to after a successful delete
 * @returns {void}
 */
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
/* Function to delete all items in a table using a modal. */