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
    const regionCheck = document.getElementById('region-check');
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

// Function to set the region id and name in the modal
function delete_region(expression, name) {
    let modal_body = document.getElementById('modal-body-region');
    modal_body.innerHTML = "Are you sure you want to delete this region: <b>" + name + "</b>?";

    let modal_button = document.getElementById('button-delete-region');
    modal_button.href = expression;
}
// Function to set the region id and name in the modal
