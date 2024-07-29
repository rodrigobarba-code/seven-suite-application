// Load sidebar
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement; // selecting home parent of arrow
        arrowParent.classList.toggle("showMenu");
    });
}
// Load sidebar

// Get the sidebar and user actions elements
const sidebar = document.querySelector(".sidebar");
const userActions = document.querySelector('.user-actions');

// Function to toggle sidebar
function toggleSidebar() {
    sidebar.classList.toggle("close");
}

// Function to toggle user actions
function toggleUserActions() {
    if (userActions.classList.contains('visible')) {
        userActions.classList.remove('visible');
        setTimeout(() => {
            userActions.style.display = 'none';
        }, 500); // Adjust this duration to match the CSS transition
    } else {
        userActions.style.display = 'flex';
        setTimeout(() => {
            userActions.classList.add('visible');
        }, 30); // A brief delay before adding 'visible'
    }
}

// Toggle sidebar with menu button
let sidebarBtn = document.querySelector(".bx-menu");
sidebarBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleSidebar();

});

// Toggle user actions dropdown with profile image and open sidebar
document.querySelector('.profile-content img').addEventListener('click', function (e) {
    e.stopPropagation(); // Prevent parent event handlers from being executed
    toggleUserActions();
    if (sidebar.classList.contains('close')) {
        sidebar.classList.remove('close');
    }
});

// Close sidebar and user actions dropdown when user clicks outside
document.addEventListener('click', function (e) {
    const isClickInsideSidebar = sidebar.contains(e.target);
    const isClickInsideUserActions = userActions.contains(e.target);
    const isClickInsideSidebarBtn = sidebarBtn.contains(e.target);
    const isClickInsideProfileImg = document.querySelector('.profile-content img').contains(e.target);

    if (!isClickInsideSidebar && !isClickInsideUserActions && !isClickInsideSidebarBtn && !isClickInsideProfileImg) {
        if (!sidebar.classList.contains('close')) {
            sidebar.classList.add('close');
        }
        if (userActions.classList.contains('visible')) {
            userActions.classList.remove('visible');
            setTimeout(() => {
                userActions.style.display = 'none';
            }, 500); // Adjust this duration to match the CSS transition
        }
    }
});

// Handle swipe gestures for sidebar
let touchStartX = 0;
let touchEndX = 0;

sidebar.addEventListener('touchstart', function (event) {
    touchStartX = event.changedTouches[0].screenX;
}, false);

sidebar.addEventListener('touchend', function (event) {
    touchEndX = event.changedTouches[0].screenX;
    handleSwipeGesture();
}, false);

function handleSwipeGesture() {
    if (touchEndX > touchStartX && touchEndX - touchStartX > 50) {
        sidebar.classList.remove('close');
        userActions.style.display = 'flex';
        setTimeout(() => {
            userActions.classList.add('visible');
        }, 30); // A brief delay before adding 'visible'
    } else if (touchStartX > touchEndX && touchStartX - touchEndX > 50) {
        sidebar.classList.add('close');
        userActions.classList.remove('visible');
        setTimeout(() => {
            userActions.style.display = 'none';
        }, 500); // Adjust this duration to match the CSS transition
    }
}
