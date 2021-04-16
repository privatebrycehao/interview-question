let add = function(){
      let counter = 0;
      return function(){
             return(++counter);
      }
};
add()();   //counter为1
add()();   //counter为1
add()();   //counter为1


let add = (function(){
      let counter = 0;
      return function(){
             return(++counter);
      }
})();
add();   //counter为1
add();   //counter为1
add();   //counter为1
