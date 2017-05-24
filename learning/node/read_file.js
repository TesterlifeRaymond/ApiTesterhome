/*
* @Author: Ray
* @Date:   2017-03-24 08:04:49
* @Last Modified by:   Ray
* @Last Modified time: 2017-03-24 10:08:17
*/

'use strict';
var fs = require('fs');
var zlib = require('zlib');


var path = 'txt/input.txt'

var data = ''

// 创建可读流
var file = fs.createReadStream(path); 

file.setEncoding('utf-8');

// for 循环获取 流中的buffer对象
for (var i = 0; i < 5; i++){
    console.log(i, file._readableState.buffer);
}


// 处理流事件

file.on('data', function(chunk){
    console.log(data += chunk);
})

file.on('end', function(){
    console.log(data);
})

file.on('error', function(err){
    console.log(err.stack);
})

// 这里虽然绑定了事件，但是并没有触发， 如果需要触发，可以尝试以下代码

file.emit('data', "传递给回调函数一个参数，就是这个字符串")

console.log("程序执行完毕");


// 创建写入流

var write = fs.createWriteStream('txt/output.txt');

var eamil = 'xxx@testerlife'

write.write(eamil, 'utf-8')

// 标记文件末尾
write.end()

write.on('finish', function(){
    console.log(' write over ! email is', eamil);
})

write.on('error', function(err){
    console.log(err.stack);
})

console.log('程序执行完毕');


var fs = require("fs");

// 创建一个可读流
var readerStream = fs.createReadStream(path);

// 创建一个可写流
var writerStream = fs.createWriteStream('txt/output.txt');

// 管道读写操作
// 读取 input.txt 文件内容，并将内容写入到 output.txt 文件中
readerStream.pipe(writerStream);

console.log("程序执行完毕");


fs.readFile(path, function(err, data){
    if (err){
        console.log(err.stack);
        return ;
    }
    console.log(data.toString());
})

var world = function(args){
    console.log('hello world !');
    console.log(args);
}


var func = function(args){
    console.log(args);
}

console.log(world(func("这是func函数的参数")));

// 链式流
fs.createReadStream(path).pipe(zlib.createGzip()).pipe(fs.createWriteStream('zip/input.txt.gz'))


fs.createReadStream(path).pipe(zlib.createGunzip()).pipe(fs.createWriteStream(path))


