
function createMap() {
    const map = L.map('map').setView([42.755, -7.8661], 8);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 18
    }).addTo(map);

    map.on('click', function(e) {
        const x = e.latlng.lat;
        const y = e.latlng.lng;

        // Use different icons for different markers
        const marker = L.marker([x, y], { icon: redIcon }).addTo(map);
        marker.bindPopup("<b>Coordenadas</b><br/>" + x + ", " + y + "<br/><a href='/ponte/red/crear_red/" + x + "," + y + "' class='buttonpop'><button>Crear red aquí</button></a>").openPopup();
        const container = document.getElementsByClassName('leaflet-control-container')[0];
        const customControl = L.DomUtil.create('div', 'leaflet-bar leaflet-control');
        container.appendChild(customControl);
    });
    return map;
}
