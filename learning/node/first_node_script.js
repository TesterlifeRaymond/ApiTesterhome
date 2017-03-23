
// learning node.js 
// http://www.runoob.com/nodejs/nodejs-tutorial.html

// console.log('Hello World !')

// var http = require('http')

// http.createServer(function (request, response) {
//     response.end('Hello World !')
// }).listen(5000)

// console.log('server is running http://127.0.0.1:5000')

var file = require('fs');

// 阻塞式编写

var data = file.readFileSync('txt/input.txt');

console.log(data.toString());
console.log('程序结束运行！');

// 非阻塞式编写 
// 看起来很像python的装饰器语法

/**
    def function(func):
        def wrap(*args, **kwargs):
            do some thing
            return some thing
        return wrap        
**/
file.readFile('txt/input.txt', function(err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});

console.log('程序结束运行！');

