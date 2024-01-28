function validateCode() {
    var codeInputValue = document.getElementById("codeInput").value;
    if (codeInputValue==="AngelIsland") {
        window.open('/win');
    } else {
        alert("INCORRECT CODE");
    }
}