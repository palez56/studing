//объект учащийся
let student = {
    secondName: "Harden",
    name: "James",
    surname: "O'neal",
    yearOfBirth: 2008,
    class: 7,
    trainingPeriod: 11,
    favoriteDisciplines: ["Mathematic", "English Language"],
    placeOfRegistration: {
        country: "USA",
        city: "Miami",
        houseNumber: 19,
        apartamentNumber: 14
    },
    placeOfResidence: {
        country: "USA",
        city: "Washington",
        houseNumber: 44,
        apartamentNumber: 32
    },
    checkTrainingPeriod: function(){
        this.class += 1;
        if(this.class > this.trainingPeriod){
            this.class = "Максимальный класс достигнут";
        }
    },
    //методы, выводящие информацию о его прописке и месте проживания
    placeOfRegistrationInfo: function(){
        return this.placeOfRegistration.country + ", " + this.placeOfRegistration.city + ", " + this.placeOfRegistration.houseNumber + ", " + this.placeOfRegistration.apartamentNumber;
    },
    placeOfResidenceInfo: function(){
        return this.placeOfResidence.country + ", " + this.placeOfResidence.city + ", " + this.placeOfResidence.houseNumber + ", " + this.placeOfResidence.apartamentNumber;
    },
    //метод, проверки года(8 пункт)
    checkYear: function(){
        let year = prompt("Введите год рождения");
        if((2022 - 200) < year && year < 2020){
            student.yearOfBirth = year;
        }else{
            alert("Введен неверный год")
        }
    },
    //метод, выводящий полную информацию об учащемся
    fullInformation: function(){
        return "Имя: " + this.name + 
        "<br>Фамилия: " + this.secondName + 
        "<br>Отчество: " + this.surname +
        "<br>Год рождения: " + this.yearOfBirth + 
        "<br>Класс: " + this.class + 
        "<br>Срок обучения: " + this.trainingPeriod +
        "<br>Любимые дисциплины: " + this.favoriteDisciplines + 
        "<br>Место регистрации(страна, город, номер дома, номер квартиры): " + this.placeOfRegistrationInfo() +
        "<br>Место проживания(страна, город, номер дома, номер квартиры): " + this.placeOfResidenceInfo();
    }
}

student.checkYear();
student.checkTrainingPeriod();
document.write(student.fullInformation());