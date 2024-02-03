

function createMap() {
    const map = L.map('map').setView([42.755, -7.8661], 8);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 18
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
        marker.bindPopup("<b>Coordenadas</b><br/>" + x + ", " + y + "<br/><a href='/ponte/red/crear_red/" + x + "," + y + "' class='buttonpop'><button>Crear red aquí</button></a>"+ "<br/><a href='/ponte/ancla/crear_ancla/" + x + "," + y + "' class='buttonpop'><button>Crear ancla aquí</button></a>").openPopup();
        const container = document.getElementsByClassName('leaflet-control-container')[0];
        const customControl = L.DomUtil.create('div', 'leaflet-bar leaflet-control');
        container.appendChild(customControl);
    });

    return map;
}

    