// main.js - Event Ticket Booking System with Bootstrap 5 Compatibility

document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Bootstrap-enhanced JS loaded");

  // 🔄 Form submit feedback (non-API)
  const forms = document.querySelectorAll("form");
  forms.forEach(form => {
    form.addEventListener("submit", (e) => {
      console.log("Form submitted:", form);
      // Optional: Add loading spinner or disable button here
    });
  });

  // 🌐 Navbar active link highlighting
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  const currentURL = window.location.pathname;

  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentURL) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  // 💬 Optional Bootstrap tooltip enable
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // ⚠️ Flash message auto-dismiss
  const flash = document.querySelector(".flash-message");
  if (flash) {
    setTimeout(() => {
      flash.style.display = "none";
    }, 5000);
  }

  // 🛒 Ticket Cart Placeholder (future enhancement)
  const cartBtn = document.getElementById("ticket-cart");
  if (cartBtn) {
    cartBtn.addEventListener("click", () => {
      alert("🛒 Ticket cart feature coming soon!");
    });
  }
});

  function showToast() {
    const toast = document.getElementById('successToast');
    toast.style.transform = 'translateX(0)';
    setTimeout(() => hideToast(), 3000);
  }

  function hideToast() {
    const toast = document.getElementById('successToast');
    toast.style.transform = 'translateX(120%)';
  }