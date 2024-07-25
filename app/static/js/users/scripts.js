// Assign Data Table to regions table
$(document).ready(function () {
    $('#users-table').DataTable(
        {
            "responsive": true,
            "autoWidth": true
        }
    );
});
// Assign Data Table to regions table

// Check if the checkbox is checked
document.addEventListener('DOMContentLoaded', () => {
    const userCheck = document.getElementById('users-check');
    const userForm = document.querySelector('form');

    // Add event listener to the form to verify if the checkbox is checked
    userForm.addEventListener('submit', (e) => {
        if (!userCheck.checked) {
            e.preventDefault();
            alert('Please accept the terms and conditions');
        }
    });
    // Add event listener to the form to verify if the checkbox is checked
});

// Check if the checkbox is checked

function deleteSelectedUsersModal(urlIn, urlOut) {
    document.getElementById('delete-selected').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        document.getElementById('total-selected').innerText = String(checkboxes.length);
    });

    document.getElementById('confirm-delete').addEventListener('click', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        const selectedIds = Array.from(checkboxes).map(cb => cb.id.replace('user-', ''));

        if (selectedIds.length > 0) {
            fetch(urlIn, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({users_ids: selectedIds})
                }
            ).then(response => {
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

function deleteAllUsersModal(urlIn, urlOut) {
    document.getElementById('confirm-delete-all').addEventListener('click', function () {
        if (document.querySelectorAll('input[type="checkbox"]').length === 0) {
            alert('No users to delete');
        } else {
            fetch(urlIn, {
                method: 'POST',
                headers: {
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