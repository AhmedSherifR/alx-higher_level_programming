#!/usr/bin/node
// add the two arguments if numbers 

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b){
	return (a + b) ;
}
console.log(add(a, b));
