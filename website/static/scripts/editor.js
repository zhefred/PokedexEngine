document.addEventListener("DOMContentLoaded", function() {
    let button = document.createdElement("button");
    button.textContent = "Edit text";
    document.body.insertBefore(button, document.body.firstChild);

    button.addEventListener("click", function () {
        let textBoxes = [];
        document.querySelectorAll("p").forEach(paragraph => {
            let textBox = document.createElement("input");
            textBox.type = "text";
            textBox.value = paragraph.textContent;
            textBox.style.width = "100%"
        })
    })
})