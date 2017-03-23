/*
* @Author: jinjialiu
* @Date:   2017-03-23 09:09:39
* @Last Modified by:   Ray
* @Last Modified time: 2017-03-23 09:15:54
*/

'use strict';

var events = require('events');

var event = new events.EventEmitter();

var listen = function listen(){
    console.log('监听器 listen 执行');
}

var to_listen = function to_listen(){
    console.log('监听器 to_listen 执行');
}

event.addListener('connection', listen)
event.on('connection', to_listen)

var eventListeners = require('events').EventEmitter.listenerCount(event,'connection');
console.log(eventListeners + " 个监听器监听连接事件。");

event.emit('connection')

event.removeListener('connection', listen)

var eventListeners = require('events').EventEmitter.listenerCount(event,'connection');
console.log(eventListeners + " 个监听器监听连接事件。");

event.emit('connection')
