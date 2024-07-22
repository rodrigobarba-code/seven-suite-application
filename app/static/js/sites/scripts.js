// Assign the data table to the table with the id sites-table
$(document).ready(function () {
    $('#sites-table').DataTable(
        {
            responsive: true
        }
    );
});
// Assign the data table to the table with the id sites-table

// Check if the checkbox is checked
    document.addEventListener('DOMContentLoaded', () => {
        const siteCheck = document.getElementById('site-check');
        const siteForm = document.querySelector('form');

        // Add event listener to the form to verify if the checkbox is checked
        siteForm.addEventListener('submit', (e) => {
            if (!siteCheck.checked) {
                e.preventDefault();
                alert('Please accept the terms and conditions');
            }
        });
        // Add event listener to the form to verify if the checkbox is checked
    });
// Check if the checkbox is checked