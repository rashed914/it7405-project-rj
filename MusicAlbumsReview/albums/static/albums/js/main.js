// ---------------------- DEBUG ----------------------
console.log("Frontend loaded successfully.");


// ---------------------- SEARCH BAR (Auto-submit on Enter) ----------------------
const searchInput = document.querySelector(".search-bar input");

if (searchInput) {
    searchInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            this.form.submit();
        }
    });
}


// ---------------------- STAR RATING (Add Review Page) ----------------------
// This runs only on pages that include the star container
const starContainer = document.getElementById("starRating");
const ratingInput = document.getElementById("ratingInput");

if (starContainer && ratingInput) {
    const stars = starContainer.querySelectorAll("span");

    stars.forEach((star) => {
        // Hover effect
        star.addEventListener("mouseover", function () {
            let hoverValue = this.getAttribute("data-value");

            stars.forEach((s) => {
                s.classList.remove("active");
                if (s.getAttribute("data-value") <= hoverValue) {
                    s.classList.add("active");
                }
            });
        });

        // Click to select rating
        star.addEventListener("click", function () {
            let rating = this.getAttribute("data-value");
            ratingInput.value = rating;
            console.log("Rating selected:", rating);
        });
    });

    // Remove hover highlight when mouse leaves
    starContainer.addEventListener("mouseleave", function () {
        let selectedRating = ratingInput.value;

        stars.forEach((s) => {
            s.classList.remove("active");
            if (s.getAttribute("data-value") <= selectedRating) {
                s.classList.add("active");
            }
        });
    });
}


// ---------------------- SMOOTH SCROLL TO TOP ----------------------
window.addEventListener("load", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup-message");
    if (popup) {
        popup.classList.add("show");

        // Hide after 3 seconds
        setTimeout(() => {
            popup.classList.remove("show");
        }, 3000);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup-message");
    if (popup) {
        setTimeout(() => {
            popup.style.display = "none";
        }, 3500);
    }
});
