function checkStorage() {
    if (window.localStorage) {
        var key, value, field;
        for (var i = 0; i < localStorage.length; i++) {
            key = localStorage.key();
            field = document.getElementById(key);
            if (field) {
                value = unescape(localStorage.getItem(key));
                field.value = value;
            }
        }
    }
}

function changeField(formField) {
    if (window.localStorage) {
        var key, value;
        key = formField.id;
        value = escape(formField.value);
        try {
            localStorage.setItem(key, value)
        } catch (err) {
            if (err.code == QUOTA_EXCEEDED_ERR) {
                alert('za mało miejsca w localStorage!');
            }
        }
    } else {
        alert("localStorage nie jest obsługiwane!");
    }
}

window.addEventListener("load", checkStorage, false);