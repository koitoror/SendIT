/*jshint esversion: 6 */


// Get the login modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Get the signup modal
var modal = document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

document.getElementById("#login_instead").click(function() {
    document.getElementById("#id02").modal('hide');
    document.getElementById("#id01").modal('show');
});

// Get the change modal
var modal = document.getElementById('id03');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Get the change2 modal
var modal = document.getElementById('id04');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

document.getElementById("#_instead").click(function() {
    document.getElementById("#id04").modal('hide');
    document.getElementById("#id03").modal('show');
});
