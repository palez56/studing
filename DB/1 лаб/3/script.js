x = prompt("Введите число")
function fact(x){
    if(x == 1) return 1;
    return x * fact(x-1);
}

function ar_mean(x){
    let sum = 0;
    for(let i = 0; i <= x; i++){
        sum += i;
    }
    return sum/x;
}

if (x % 2 == 0){
    document.write(fact(x));
}else{
    document.write(ar_mean(x));
}
