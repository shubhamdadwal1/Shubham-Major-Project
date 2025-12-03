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
