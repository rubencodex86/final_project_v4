function openTab(evt, tabName) {
    let i, tabcontent, tablinks;

    // Esconde o contúdo da tab
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove a classe active das tabs
    tablinks = document.getElementsByClassName("tab-link");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // A tab aberta passa a ter a classe active tornando-se visivel.
    document.getElementById(tabName).style.display = "flex";
    evt.currentTarget.className += " active";
}