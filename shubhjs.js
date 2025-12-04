// Variant Button Selection
let buttons = document.querySelectorAll(".variant-btn");

buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        buttons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    });
});

// Add to Cart Function
document.querySelector(".add-btn").onclick = function () {
    alert("Product Added to Cart!");
};



// Get existing cart count or set to 0
let count = localStorage.getItem("cartCount") || 0;

// Update button click event
document.querySelector(".add-btn").addEventListener("click", function () {
    count++; // increase count
    localStorage.setItem("cartCount", count); // update storage
});
document.querySelector(".add-btn").addEventListener("click", function() {
    window.location.href = "index3.html";
});
