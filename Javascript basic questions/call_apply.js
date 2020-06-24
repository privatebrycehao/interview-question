let bob = function(num, str,x){
    console.log('bob', num, str, this,x);
    return true;
}
let bill = {
    name: 'bill murray',
    movie: ' lost in translation',
    myMethod: function(fn) {
        // fn(2, 'hello');
        let n = arguments[1];
        let s = arguments[2];
        fn.apply(bill, [n,s]);
        // fn.call(bill,n,s );
    }
}
bob(1, 'hello')
bill.myMethod(bob);
// call(this, any Agreement)
bob.call(bill,2, 'goodbye');
bob.apply(bill, [3, 'hi', 'test']);
bill.myMethod(bob,4, 'ciao')
let fred = bob.bind(bill, 5, 'hasta la vista')
fred('X')
let customer1 = { name: 'Leo', email: 'leo@gmail.com' };
let customer2 = { name: 'Nat', email: 'nat@hotmail.com' };

function greeting(text, text2) {
    console.log(`${text} ${this.name}`);
    console.log(text2);
}

greeting.call(customer1, 'Hello', 'test'); // Hello Leo test
greeting.call(customer2, 'Hello', 'test'); // Hello Nat test
greeting.apply(customer1, ['Hello' , 'test']) // hello Leo test
function myFunc(a, b, ...args) {
    console.log(a); // 22
    console.log(b); // 98
    console.log(args); // [43, 3, 26]
}
myFunc(22, 98, 43, 3, 26);