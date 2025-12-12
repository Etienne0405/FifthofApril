fetch("/static/navbar/navbar.html")
    .then(response => response.text())
    .then(data => {
        document.querySelector("#navbar-container").innerHTML = data;
    });
