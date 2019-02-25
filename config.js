// https://www.npmjs.com/package/jest-fetch-mock#installation-and-setup

window.confirm = (msg) => { return true };

global.fetch = require('jest-fetch-mock');

let DOMContentLoaded_event = document.createEvent("Event")
DOMContentLoaded_event.initEvent("DOMContentLoaded", true, true)
window.document.dispatchEvent(DOMContentLoaded_event)