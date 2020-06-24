function add(a,b) {
    return a+b;
}
// below currying
function add2(a,b) {
    if(!b) {
        return add.bind(null, a)
        // as same as above return (b) => add(a,b);
    }
    return a+b;
}
const add3 = add2(2)
const numbers = [1,2,3,4,5,6]
console.log(numbers.map(add3))
console.log(add(2,3) === 5);
console.log(add2(2,3) === 5)
console.log(add2(2))
console.log(numbers.map(number => add3(number)));