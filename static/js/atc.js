const input = document.getElementById('filter-input');
const list = document.getElementById('objects-list');
import WebSocket from 'ws';

// Listen for changes to the input value.
input.addEventListener('input', function() {
    // Get the filtered list of objects.
    var filteredObjects = objects.filter(function(object) {
        return object.Callsign.toLowerCase().startsWith(input.value.toLowerCase());
    });
    console.log(input.value);
    // Clear the list.
    list.innerHTML = '';

    // Add the filtered objects to the list.
    filteredObjects.forEach(function(object) {
        list.innerHTML += '<li>' + object.Callsign + '</li>';
    });
});

list.addEventListener('click', function(event) {
    // Get the clicked item.
    var item = event.target;

    // Get the value of the item.
    var value = item.textContent;

    // Put the value into the input field.
    input.value = value;
});


const websocket = new WebSocket(
    "ws://"
    + window.location.host
    + 'ws/atc/'   
)

websocket.onmessaage = function(e) {
    var data = JSON.parse(e.data);
    console.log("data");
};

websocket.onclose = function(e) {
    console.log("Websocket closed");
};

websocket.onopen = function(e) {
    console.log("Websocket opened");
};

message = "Lufthansa 1342"
setTimeout(function(e) {
    websocket.send(JSON.stringify({"message" : message}))
}, 2000);