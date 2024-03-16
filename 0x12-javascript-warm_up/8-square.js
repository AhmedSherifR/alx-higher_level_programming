#!/usr/bin/node
//print square


const size = process.argv[2];
if (isNaN(size)){
	console.log('Missing size');
} else {
	let i = 0 ;
	while (i < size){
		console.log('X'.repeat(size));
		i++;
		}
}
