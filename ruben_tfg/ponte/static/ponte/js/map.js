function createMap() {
    const map = L.map('map').setView([42.755, -7.8661], 8);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 18,
        minZoom: -3,
        markerZoomAnimation: false,
        zoomControl: false,
    }).addTo(map);

    let marker;

    map.on('click', function(e) {
        const x = e.latlng.lat;
        const y = e.latlng.lng;

        // Delete previous marker if exists
        if (marker) {
            map.removeLayer(marker);
        }

        // Use default icon for marker
        marker = L.marker([x, y]).addTo(map);
        marker.bindPopup("<b>Coordinates</b><br/>" + x + ", " + y + "<br/><a href='/ponte/network/create_network/" + x + "," + y + "' class='buttonpop'><button>Create network here</button></a>"+ "<br/><a href='/ponte/anchor/create_anchor/" + x + "," + y + "' class='buttonpop'><button>Create anchor here</button></a>").openPopup();
        const container = document.getElementsByClassName('leaflet-control-container')[0];
        const customControl = L.DomUtil.create('div', 'leaflet-bar leaflet-control');
        container.appendChild(customControl);
    });

    return map;
}
