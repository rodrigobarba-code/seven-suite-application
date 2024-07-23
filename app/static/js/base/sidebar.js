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


// Add border radius to home content when user scrolls down
// document.addEventListener("scroll", function () {
//     var homeContent = document.querySelector('.home-content');
//     if (window.scrollY > 100) { // If user scrolls down 100px from the top of the document
//         homeContent.style.borderBottomLeftRadius = "15px"; // Add border radius to bottom left
//         homeContent.style.borderBottomRightRadius = "15px"; // Add border radius to bottom right
//     } else {
//         homeContent.style.borderBottomLeftRadius = ""; // Remove border radius from bottom left
//         homeContent.style.borderBottomRightRadius = ""; // Remove border radius from bottom right
//     }
// });
// Add border radius to home content when user scrolls down


let isAnimating = false; // Track if animation is in progress


// Toggle user actions dropdown
document.querySelector('.profile-content img').addEventListener('click', function (e) {
    if (isAnimating) return; // Exit if an animation is already in progress
    isAnimating = true; // Lock further interactions until the current animation completes

    e.stopPropagation(); // Prevent parent event handlers from being executed

    const sidebar = document.querySelector('.sidebar');
    const userActions = document.querySelector('.user-actions');

    // Toggle visibility based on current state
    if (!sidebar.classList.contains('close') || userActions.classList.contains('visible')) {
        sidebar.classList.add('close');
        userActions.classList.remove('visible');
        setTimeout(() => {
            userActions.style.display = 'none';
            isAnimating = false; // Unlock interactions
        }, 500); // Match this duration with your CSS transition
    } else {
        sidebar.classList.remove('close');
        userActions.style.display = 'flex';
        setTimeout(() => {
            userActions.classList.add('visible');
            isAnimating = false; // Unlock interactions
        }, 30); // A short delay before adding 'visible' to ensure it's seen as a change
    }
});