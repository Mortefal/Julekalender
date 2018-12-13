function isPrime(num) {
  for(var i = 2; i < num; i++)
    if(num % i === 0) return false;
  return num !== 1 && num !== 0;
}
const primes = [3]
const sek = [1,3]
function julesekvens(k) {
	// body...
	let temp = [];
	
	if (primes.length == 100){
		const add = (a, b) =>
			a + b;
		const sum = primes.reduce(add);
		return console.log(sum);
	}

	for (let i = 0; i < sek.length -1; i++) {
		for (let j = i+1; j < sek.length; j++) {
			if(sek[i] === sek[j]){
				continue;
			}
			if(sek[i] + sek[j] > sek.slice(-1)[0] + k || temp.length > 1){
				
				break;
			}
			if(sek[i] + sek[j] === sek.slice(-1)[0] + k){
				let x = sek[i] + sek[j];
				temp.push(x);
			}
		}
	}
	if(temp.length === 1){
		if(isPrime(temp[0])){
			primes.push(temp[0]);
		}
		sek.push(temp[0]);
		k = 1

		return julesekvens(k)
	}
	return(julesekvens(k+1));
}
julesekvens(1)