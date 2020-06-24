// Give an array, find the id equal to 1 object, change the name to EWR


const airport =  [{id: 1, name: 'lax'}, {id:2, name: 'IAD'}]
function change(airport, id, name){
	const ans = airport.map(item => {
  	const tmp = Object.assign({}, item)
    if (item.id === id) {
    	tmp.name = name;
    }
  	return tmp;
  })
  return ans;
}
const newAirport = (airport, id, name) => {
	return airport.map(item => {
  	 const tmp = Object.assign({}, item);
     if (tmp.id === id){
     		tmp.name = name
     }
     return tmp
  })
}
const newAirportName = newAirport(airport,1,'EWR');

console.log(change(airport, 1, 'EWR'))
console.log(airport)
console.log(newAirportName)
