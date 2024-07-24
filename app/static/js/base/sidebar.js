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
// Toggle sidebar
let sidebarBtn = document.querySelector(".bx-menu");
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");

    // Asegurarse de manejar correctamente la visibilidad de 'user-actions'
    const userActions = document.querySelector('.user-actions');
    if (!sidebar.classList.contains("close") && !userActions.classList.contains('visible')) {
        userActions.style.display = 'flex';
        setTimeout(() => {
            userActions.classList.add('visible');
        }, 30); // Un breve retraso antes de agregar 'visible'
    } else if (sidebar.classList.contains("close") && userActions.classList.contains('visible')) {
        userActions.classList.remove('visible');
        setTimeout(() => {
            userActions.style.display = 'none';
        }, 500); // Ajustar esta duración para que coincida con la transición CSS
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

// Close user actions dropdown when user clicks outside
document.addEventListener('click', function (e) {
    const sidebar = document.querySelector('.sidebar');
    const useract = document.querySelector('.user-actions');
    const isClickInsideSidebar = sidebar.contains(e.target);

    if (!isClickInsideSidebar && !sidebar.classList.contains('close')) {
        // Aquí, asumimos que la clase 'close' es la que controla la visibilidad del sidebar.
        // Ajusta esta lógica según cómo manejes la apertura/cierre del sidebar en tu proyecto.
        sidebar.classList.add('close');
        useract.classList.remove('visible');
    }
});
// Close user actions dropdown when user clicks outside

let touchStartX = 0;
let touchEndX = 0;

// Elemento del sidebar y user-actions
const sidebar = document.querySelector('.sidebar');
const useract = document.querySelector('.user-actions');

// Detectar inicio del toque
sidebar.addEventListener('touchstart', function (event) {
    touchStartX = event.changedTouches[0].screenX;
}, false);

// Detectar fin del toque
sidebar.addEventListener('touchend', function (event) {
    touchEndX = event.changedTouches[0].screenX;
    handleSwipeGesture();
}, false);

// Función para manejar el gesto de deslizamiento
// Función para manejar el gesto de deslizamiento
function handleSwipeGesture() {
    // Deslizamiento hacia la derecha para abrir el sidebar
    if (touchEndX > touchStartX) {
        // Umbral para determinar si el deslizamiento es significativo
        if (touchEndX - touchStartX > 50) {
            // Abrir el sidebar
            sidebar.classList.remove('close');
            useract.classList.add('visible');
        }
    }
    // Deslizamiento hacia la izquierda para cerrar el sidebar
    else if (touchStartX > touchEndX) {
        if (touchStartX - touchEndX > 50) {
            // Cerrar el sidebar
            sidebar.classList.add('close');
            useract.classList.remove('visible');
        }
    }
}