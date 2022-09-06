const students = [
    ["Alex", "Alex", 2, 808],
    ["Tracy", "Carl", 1, 572],
    ["Remington", "Kyle", 4, 888],
    ["Johnson", "Michael", 2, 808],
    ["Lake", "Shon", 1, 572],
    ["Harden", "James", 3, 888]
];

let num = prompt("Введите номер направления");

for(let i = 0; i <= students.length - 1; i++){
    if(students[i].includes(parseInt(num))){
        document.write(students[i] + "<br>");
    }else{
        console.log(students[i]);
    }
}