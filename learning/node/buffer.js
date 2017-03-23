/*
* @Author: Ray
* @Date:   2017-03-23 09:18:33
* @Last Modified by:   Ray
* @Last Modified time: 2017-03-23 09:28:24
*/

'use strict';

var buf = new Buffer(10);

console.log(buf);

var buf = new Buffer([10, 20, 30, 40]);
console.log(buf);

var buf = new Buffer("Raymond", "utf-8");
console.log(buf);

var len = buf.write("20000000")
console.log("写入字节数为：" + len);

var buf = Buffer(26);
for (var i = 0; i < 26; i ++){
    buf[i] = i + 97
    console.log(i);
    console.log(buf);
}

console.log(buf.toString('utf-8'));
console.log(buf.toJSON());

var buffer1 = new Buffer('菜鸟教程 ');
var buffer2 = new Buffer('www.runoob.com');
var buffer3 = Buffer.concat([buffer1,buffer2]);
console.log("buffer3 内容: " + buffer3.toString());
console.log(buffer3.compare(buffer2))


var buffer1 = new Buffer('ABC');
var buffer2 = new Buffer('ABCD');
var result = buffer1.compare(buffer2);

if(result < 0) {
   console.log(buffer1 + " 在 " + buffer2 + "之前");
}else if(result == 0){
   console.log(buffer1 + " 与 " + buffer2 + "相同");
}else {
   console.log(buffer1 + " 在 " + buffer2 + "之后");
}

