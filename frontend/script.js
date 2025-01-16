// Toggle Left Menu
const toggleMenu = document.getElementById("toggleMenu");
const leftMenu = document.getElementById("leftMenu");

toggleMenu.addEventListener("click", () => {
  leftMenu.classList.toggle("d-none");
});

// Adjust Page Size Based on Screen Width
function adjustPageSize() {
  const screenWidth = window.innerWidth;

  if (screenWidth >= 992 && screenWidth <= 1600) {
    document.body.style.transform = "scale(0.9)";
  } else if (screenWidth >= 700 && screenWidth <= 767) {
    document.body.style.transform = "scale(0.8)";
  } else if (screenWidth >= 600 && screenWidth < 700) {
    document.body.style.transform = "scale(0.75)";
  } else if (screenWidth <= 600) {
    document.body.style.transform = "scale(0.5)";
  } else {
    document.body.style.transform = "scale(1)";
  }
}

window.addEventListener("resize", adjustPageSize);

adjustPageSize();
