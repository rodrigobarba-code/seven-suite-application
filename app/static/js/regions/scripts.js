// Assign Data Table to regions table
$(document).ready(function () {
    $('#regions-table').DataTable(
        {
            responsive: true
        }
    );
});
// Assign Data Table to regions table

// Check if the checkbox is checked
document.addEventListener('DOMContentLoaded', () => {
    const regionCheck = document.getElementById('regions-check');
    const regionForm = document.querySelector('form');

    // Add event listener to the form to verify if the checkbox is checked
    regionForm.addEventListener('submit', (e) => {
        if (!regionCheck.checked) {
            e.preventDefault();
            alert('Please accept the terms and conditions');
        }
    });
    // Add event listener to the form to verify if the checkbox is checked
});
// Check if the checkbox is checked