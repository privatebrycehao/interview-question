// what is bind
// 1. Bind an object to a function
// 2. reference it using 'this'
let c1 = {
    x: 5,
    y: 10
};
let c2 = {
    x: 75,
    y: 235
}
function printCoordinates() {
    console.log(this);
    console.log(this.x, this.y);
}
// printCoordinates(); // window(this)
let c1_func = printCoordinates.bind(c1);
c1_func();
let c2_func = printCoordinates.bind(c2);
c2_func()