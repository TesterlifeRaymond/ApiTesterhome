/*
* @Author: Ray
* @Date:   2017-03-23 09:16:12
* @Last Modified by:   Ray
* @Last Modified time: 2017-03-23 09:17:41
*/

'use strict';

var events = require('events');

var event = new events.EventEmitter();

event.emit('error')