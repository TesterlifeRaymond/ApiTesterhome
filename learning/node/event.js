/*
* @Author: jinjialiu
* @Date:   2017-03-23 07:40:43
* @Last Modified by:   jinjialiu
* @Last Modified time: 2017-03-23 08:19:14
*/

'use strict';


var events = require('events')

var eventEmitter = new events.EventEmitter();

var connectionHandler = function connected(){
    console.log('连接成功');
    // 触发 data received 事件
    eventEmitter.emit('data received !');
}

// 绑定connection 事件处理程序

eventEmitter.on('connection', connectionHandler)

// 使用匿名函数绑定 data_received 事件

eventEmitter.on('data_received', function(){
    console.log('数据接收成功');
});

eventEmitter.emit('connection')
eventEmitter.emit('data_received')


eventEmitter.on('some_event', function(){
    console.log('some event 事件触发');
});

// setTimeout(function(){
//     eventEmitter.emit('some_event');
// }, 1000);

function eve_service(say_hello){
    console.log("this is eve_service", "Hello World !");
}

eve_service()
eventEmitter.addListener('listen', function(arg1, arg2){
    console.log('listen arg1, arg2 is ', arg1, arg2);
})

eventEmitter.on('listen', function(arg1, arg2){
    console.log('listen event arg1 and arg2 ', arg1, arg2);
})

eventEmitter.once('once_event', function(stream){
    console.log('once_event 事件触发');
})
eventEmitter.emit('once_event') // 只触发一次
eventEmitter.emit('once_event')

eventEmitter.emit('listen', 'args'  , 'kwargs') // 可多次触发
eventEmitter.emit('listen', 'args'  , 'kwargs')
eventEmitter.removeAllListeners('listen')   // 移除所有的listen事件
eventEmitter.emit('listen', 'args'  , 'kwargs') // 将不再触发

console.log('程序结束运行！');
