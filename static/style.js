document.addEventListener("DOMContentLoaded", function () {
  document.body.style.backgroundColor = "#0c1b3a"; 

  document.querySelectorAll("h3").forEach(el => {
    el.style.color = "#e0d4f7";
    el.style.textAlign = "center";
    el.style.fontSize = "1.5rem";
  });


  document.querySelectorAll("button").forEach(btn => {
    btn.style.borderRadius = "0.5rem";
    btn.style.padding = "0.75rem 1rem";
    btn.style.fontWeight = "600";
    btn.style.transition = "background-color 0.3s ease";
  });

    document.querySelectorAll("h4").forEach(el => {
    el.style.color = "#fca311"; // orangish color
    el.style.fontSize = "1.5rem";
    el.style.textAlign = "center";
    el.style.marginTop = "1rem";
    el.style.marginBottom = "1rem";
  });

  const nav = document.querySelector("nav");
  if (nav) {
    nav.style.backgroundColor = "#1f2937"; 
    nav.style.color = "#ffffff";
    nav.style.padding = "1rem";
    nav.style.fontSize = "1.2rem";
    nav.style.textAlign = "center";
  }


  document.querySelectorAll(".drawing-box, .bg-purple-900").forEach(card => {
    card.style.boxShadow = "0 4px 12px rgba(0,0,0,0.3)";
    card.style.border = "1px solid #2d3748";
    card.style.backgroundColor = "#1e293b";
  });
});
