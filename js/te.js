'use strict';

class Person{
	constructor(name,age){
		this.name = name;
		this.age = age;
	}
	speak(){
		console.log("${this.name}: hello!")
	}
}

const ellie = new Person('ellie',20);
console.log(ellie.name);
console.log(ellie.age);

let person = {name:'taebin',
			age:10
			}

console.log(person.age)
console.log(person['age'])

