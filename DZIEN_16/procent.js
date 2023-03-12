var sum = 0;
var currentProc = 0;
var maxLimit = 100000000;

for (var j = 0; j <= maxLimit; j++) {
    sum += j;
    var newProc = Math.round((j / maxLimit) * 100);
    if (newProc > currentProc) {
        postMessage('zadanie ukończono w ' + newProc + '%');
        currentProc = newProc;
    }
}

postMessage('suma elementów wynosi: ' + sum);