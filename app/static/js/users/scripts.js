// Assign Data Table to regions table
$(document).ready(function () {
    $('#users-table').DataTable({
        "responsive": true, "autoWidth": true
    });
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

function deleteSelectedUsersModal(urlIn, urlOut, type) {
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

function deleteAllUsersModal(urlIn, urlOut) {
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

function deleteByDateUserLogModal(urlIn, urlOut) {
    document.getElementById('delete-by-date').addEventListener('click', function () {
        const date = document.getElementById('date-user-log-delete').value;
        fetch(urlIn, {
            method: 'POST', headers: {
                'Content-Type': 'application/json'
            }, body: JSON.stringify({date: date})
        }).then(response => {
            if (response.ok) {
                location.href = urlOut;
            } else {
                alert('Failed to delete logs');
            }
        });
    });
}

$(document).ready(function() {
    const itemsPerPage = 5; // Number of items per page
    let currentPage = 1;

    function filterLogs() {
        let searchQuery = $('#searchbox-user-log').val().toLowerCase();
        let selectedAction = $('#selectbox-user-log').val();
        let selectedDate = $('#datebox-user-log').val().split('-').reverse().join('-');

        $('.timeline .event').each(function() {
            let logText = $(this).text().toLowerCase();
            let logDate = $(this).attr('data-date').split(' ')[0].replace(/\//g, '-');
            let logAction = $(this).find('.badge').text().toLowerCase();

            let matchesSearch = searchQuery === "" || logText.includes(searchQuery);
            let matchesAction = selectedAction === "all" || logAction.includes(selectedAction);
            let matchesDate = selectedDate === "" || logDate === selectedDate;

            if (matchesSearch && matchesAction && matchesDate) {
                $(this).show().addClass('filtered');
            } else {
                $(this).hide().removeClass('filtered');
            }
        });

        // Reset to first page after filtering
        currentPage = 1;
        showPage(currentPage);

        // If there is nothing to show, add a message
        if ($('.timeline .event.filtered').length === 0) {
            $('.timeline').hide()
            $('.not-item-found-user-log').show()
        } else {
            $('.timeline').show()
            $('.not-item-found-user-log').hide()
        }
    }

    function showPage(page) {
        const start = (page - 1) * itemsPerPage;
        const end = start + itemsPerPage;

        $('.timeline .event.filtered').hide().slice(start, end).show();

        $('#prev').prop('disabled', page === 1);
        $('#next').prop('disabled', end >= $('.timeline .event.filtered').length);
    }

    $('#searchbox-user-log, #selectbox-user-log, #datebox-user-log').on('input change', function() {
        filterLogs();
    });

    $('#prev').click(function() {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    $('#next').click(function() {
        if ((currentPage * itemsPerPage) < $('.timeline .event.filtered').length) {
            currentPage++;
            showPage(currentPage);
        }
    });

    filterLogs();
});