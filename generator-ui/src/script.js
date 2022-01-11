let saveFile = () => {
    const title = document.getElementById('post-title');
    const text = document.getElementById('post-text');
    const img = document.getElementById('post-image');
    const categoryIndex = document.getElementById('post-category').options.selectedIndex;
    const category = document.getElementById('post-category').options[categoryIndex];

    function sendFile(title, text, img, category) {
        let data =
            '\r Post title: ' + title.value + ' \r\n ' +
            'Post text: ' + text.value + ' \r\n ' +
            'Img: ' + img.value + ' \r\n ' +
            'Category: ' + category.value
        const textToBLOB = new Blob([data], {type: 'text/plain'});
        const sFileName = 'formData.txt';    // The file to save the data.

        let newLink = document.createElement("a");
        newLink.download = sFileName;

        if (window.webkitURL != null) {
            newLink.href = window.webkitURL.createObjectURL(textToBLOB);
        } else {
            newLink.href = window.URL.createObjectURL(textToBLOB);
            newLink.style.display = "none";
            document.body.appendChild(newLink);
        }

        newLink.click();
    }

    sendFile(title, text, img, category)
}