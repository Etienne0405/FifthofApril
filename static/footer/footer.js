fetch("/static/footer/footer.html")
    .then(response => response.text())
    .then(data => {
        document.querySelector("#footer-container").innerHTML = data;
        document.getElementById("year").textContent = new Date().getFullYear();
    });
