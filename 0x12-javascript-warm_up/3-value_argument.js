#!/usr/bin/node
// print first argument if exist

if (process.argv[2]){
	console.log(process.argv[2]);
} else {
	console.log('No argument')
}
