var map = L.map('hospitals-map', {
    center: [-1.30323720, 36.77813964],
    zoom: 6
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 16,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// var health_facilities = L.geoJson();
// var health_facilities_data = "/api/healthfacilities?format=json";
// $.getJSON(health_facilities_data, function (data) {
//     health_facilities.addData(data)
// });
// map.addLayer(health_facilities);
