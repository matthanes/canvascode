// ==UserScript==
// @name         Unhide Gauge
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Unhide Gauge in the global navigation
// @author       Matt Hanes
// @match        https://mcsd.instructure.com/*
// @grant        none
// ==/UserScript==

(function() {
    $(document).ready(function () {
      $('#menu #context_external_tool_788_menu_item').show(); //Change the tool number for your instance.
});

})();
