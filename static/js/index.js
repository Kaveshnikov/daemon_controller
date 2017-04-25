

window.onload = function () {
    var bStart = document.getElementById('start');
    bStart.onclick = function (ev) {
        request('start', '/');
    };

    var bStop = document.getElementById('stop');
    bStop.onclick = function (ev) {
        request('stop', '/');
    };

    var bRestart = document.getElementById('restart');
    bRestart.onclick = function (ev) {
        request('restart', '/');
    };

    var cTurn_on = document.getElementById('turn_on');
    cTurn_on.onclick = function (ev) {
        if (ev.currentTarget.checked) {
            bStart.disabled = bStop.disabled = bRestart.disabled = false;
        }else {
            bStart.disabled = bStop.disabled = bRestart.disabled = true;
        }

        turn_on(ev.currentTarget.checked);
    };
};

//Выполняет запрос на выполнение команды
function request(command, url) {
    var status = document.getElementById('status');
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);

    xhr.onload = function () {
        if (xhr.status === 200) {
            status.innerHTML = xhr.responseText;
        }
    };

    xhr.onerror = function () {
        console.error(xhr.status);
    };

    xhr.timeout = 8000;

    xhr.ontimeout = function () {
        xhr.abort();
        console.warn("Request timed out");
    };

    xhr.send(command);
}

// Выполняем отправку текущего состояния
// флажка "Включить сервис"
function turn_on(condition) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'turn_on');

    xhr.onerror = function () {
        console.error(xhr.status);
    };

    xhr.timeout = 8000;

    xhr.ontimeout = function () {
        xhr.abort();
        console.warn("Request timed out");
    };

    xhr.send(condition);
}

