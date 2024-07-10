// Load sidebar
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement;//selecting home parent of arrow
        arrowParent.classList.toggle("showMenu");
    });
}
// Load sidebar

// Toggle sidebar
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});
// Toggle sidebar

document.addEventListener('DOMContentLoaded', function() {
    var logoIcon = document.querySelector('.logo-icon');

    logoIcon.addEventListener('click', function() {
        window.location.href = document.getElementById('logo-link').href;
    });
});