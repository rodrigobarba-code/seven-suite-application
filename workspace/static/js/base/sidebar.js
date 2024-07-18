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


    // Check if the sidebar is being closed and hide the user-action dropdown
    if (sidebar.classList.contains("close")) {
        const userActions = document.querySelector('.user-actions');
        if (userActions.classList.contains('visible')) {
            userActions.classList.remove('visible');
            setTimeout(() => {
                userActions.style.display = 'none';
            }, 500); // Adjust this duration to match your CSS transition
        }
    }
});

// Toggle sidebar


document.querySelector('.profile-content img').addEventListener('click', function (e) {
    e.stopPropagation(); // Prevents any parent event handlers from being executed

    const sidebar = document.querySelector('.sidebar');
    const userActions = document.querySelector('.user-actions');

    // If user-actions is visible and sidebar is open, close both
    if (userActions.classList.contains('visible') && !sidebar.classList.contains('close')) {
        sidebar.classList.add('close');
        userActions.classList.remove('visible');
        setTimeout(() => {
            userActions.style.display = 'none';
        }, 500); // Adjust this duration to match your CSS transition
    } else {
        // If the sidebar is closed, open it and show user-actions
        if (sidebar.classList.contains('close')) {
            sidebar.classList.remove('close');
            userActions.style.display = 'flex';
            requestAnimationFrame(() => {
                userActions.classList.add('visible');
            });
        } else if (!userActions.classList.contains('visible')) {
            // If sidebar is open but user-actions is not visible, just show user-actions
            userActions.style.display = 'flex';
            requestAnimationFrame(() => {
                userActions.classList.add('visible');
            });
        } else {
            // If user-actions is visible, hide it
            userActions.classList.remove('visible');
            setTimeout(() => {
                if (!userActions.classList.contains('visible')) {
                    userActions.style.display = 'none';
                }
            }, 500); // Adjust this duration to match your CSS transition
        }
    }
});