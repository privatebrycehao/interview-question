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
console.log(add(2,3) === 5); // true
console.log(add2(2,3) === 5) // true
console.log(add2(2)) // [Function: bound add]
console.log(numbers.map(add3)) // [3,4,5,6,7,8]
console.log(numbers.map(number => add3(number))); //  same as above
function multiply(a,b) {
    return a*b;
}
function multiply2(a,b) {
    if(!b) {
        return multiply.bind(null, a);
    }
}
const multiply3 = multiply2(2)
const curNumber = 10;
console.log(multiply3(curNumber));