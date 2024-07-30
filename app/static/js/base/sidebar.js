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
// Get the sidebar and user actions elements


// Function to toggle sidebar
function toggleSidebar() {
    sidebar.classList.toggle("close");
}

// Function to toggle sidebar

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

// Function to toggle user actions

// Toggle sidebar with menu button
let sidebarBtn = document.querySelector(".bx-menu");
sidebarBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleSidebar();

});
// Toggle sidebar with menu button


// Toggle user actions dropdown with profile image and open sidebar
document.querySelector('.profile-content img').addEventListener('click', function (e) {
    e.stopPropagation(); // Prevent parent event handlers from being executed
    toggleUserActions();
    if (sidebar.classList.contains('close')) {
        sidebar.classList.remove('close');
    }
});
// Toggle user actions dropdown with profile image and open sidebar


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
// Close sidebar and user actions dropdown when user clicks outside

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

// Handle swipe gestures for sidebar

// Add styles to home content when user scrolls down
document.addEventListener("scroll", function () {
    var homeContent = document.querySelector('.home-content');
    if (window.scrollY > 100) { // If user scrolls down 100px from the top of the document
        homeContent.style.borderRadius = "30px"; // Add border radius to bottom right
        homeContent.style.margin = "10px";
        // Translate the content to the bottom just a little bit
        homeContent.style.transform = "translateY(10px)";
        homeContent.style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.1)";
        homeContent.style.color = "white";
        homeContent.style.background = "#252a2f";
    } else {
        homeContent.style.borderRadius = "0"; // Remove border radius
        homeContent.style.margin = "0";
        homeContent.style.boxShadow = "none";
        homeContent.style.color = "black";
        homeContent.style.transform = "translateY(0px)";
        homeContent.style.background = "#E4E9F7";
    }
});