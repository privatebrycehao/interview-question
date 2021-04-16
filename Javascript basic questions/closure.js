var add = (function(){
      var counter = 0;
      return function(){
             return(++counter);
      }
})();      //这里add已经是执行过后的函数了。即add指定了函数自我调用的返回值
add();   //counter为1
add();   //counter为2
add();   //counter为3
