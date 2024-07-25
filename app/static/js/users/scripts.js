// Assign Data Table to regions table
$(document).ready(function () {
    $('#users-table').DataTable(
        {
            responsive: true
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