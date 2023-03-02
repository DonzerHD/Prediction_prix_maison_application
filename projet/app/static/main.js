var mymap = L.map('mapid').setView([47.6062, -122.3321], 13);
/* Création de la carte avec les coordonnées de Seattle et le niveau de zoom */
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiNTkyMjAiLCJhIjoiY2xlanBnbTA3MDNjZjNzcXNtMWIzMGR6NCJ9.wQOP84DPwtP24hzqhXdg3Q', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

var marker = L.marker([47.6062, -122.3321]).addTo(mymap);

function onMapClick(e) {
    /* Fonction qui permet de récupérer les coordonnées de la position du clic sur la carte */
    marker.setLatLng(e.latlng);
    var lat = e.latlng.lat.toFixed(6);
    var long = e.latlng.lng.toFixed(6);
    document.getElementById("id_lat").value = lat;
    document.getElementById("id_long").value = long;
    
    var popup = L.popup()
    /* Affiche les coordonnées de la position du clic sur la carte */
        .setLatLng(e.latlng)
        .setContent("Latitude: " + lat + "<br>Longitude: " + long)
        .openOn(mymap);
}

/* Ajout d'un événement au clic sur la carte */
mymap.on('click', onMapClick);

