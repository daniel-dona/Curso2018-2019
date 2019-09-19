$(document).ready(function () {
    initMap();
});

var map, my_pos;
var my_location_point, my_location_radius;
var stations;

function initMap() {
    // Styles a map in night mode.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.416673, lng: -3.703898},
        zoom: 16,
        mapTypeId: 'roadmap',
        streetViewControl: false,
    });

    my_pos = { lat: 40.416673, lng: -3.703898 };
    addYourLocationButton(map);
}

function addYourLocationButton(map) {
    var controlDiv = document.createElement('div');

    var firstChild = document.createElement('button');
    firstChild.style.backgroundColor = '#fff';
    firstChild.style.border = 'none';
    firstChild.style.outline = 'none';
    firstChild.style.width = '28px';
    firstChild.style.height = '28px';
    firstChild.style.borderRadius = '2px';
    firstChild.style.boxShadow = '0 1px 4px rgba(0,0,0,0.3)';
    firstChild.style.cursor = 'pointer';
    firstChild.style.marginRight = '10px';
    firstChild.style.padding = '0px';
    firstChild.title = 'Your Location';
    controlDiv.appendChild(firstChild);

    var secondChild = document.createElement('div');
    secondChild.style.margin = '5px';
    secondChild.style.width = '18px';
    secondChild.style.height = '18px';
    secondChild.style.backgroundImage = 'url(https://maps.gstatic.com/tactile/mylocation/mylocation-sprite-1x.png)';
    secondChild.style.backgroundSize = '180px 18px';
    secondChild.style.backgroundPosition = '0px 0px';
    secondChild.style.backgroundRepeat = 'no-repeat';
    secondChild.id = 'you_location_img';
    firstChild.appendChild(secondChild);

    google.maps.event.addListener(map, 'dragend', function() {
        $('#you_location_img').css('background-position', '0px 0px');
    });

    firstChild.addEventListener('click', function() {
        var imgX = '0';
        var animationInterval = setInterval(function(){
            if(imgX == '-18'){
                imgX = '0';
            }
            else{
                imgX = '-18';
            }
            $('#you_location_img').css('background-position', imgX + 'px 0px');
        }, 500);

        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                my_pos = { lat: position.coords.latitude,  lng: position.coords.longitude };
                map.setCenter(my_pos);
                clearInterval(animationInterval);
                $('#you_location_img').css('background-position', '-144px 0px');

                createRadius(my_pos);
                drawStations();
            }, function() {
                clearInterval(animationInterval);
                $('#you_location_img').css('background-position', '-144px 0px');
                createRadius(my_pos);
                drawStations();
            });
        } else {
            // Browser doesn't support Geolocation
            clearInterval(animationInterval);
            $('#you_location_img').css('background-position', '-144px 0px');
            createRadius(my_pos);
            drawStations();
        }
    });

    controlDiv.index = 1;
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(controlDiv);
}

function createRadius(pos){
    // Me
    if(!my_location_point){
        my_location_point = new google.maps.Circle({
            strokeColor: '#0066FF',
            strokeOpacity: 0.9,
            strokeWeight: 1,
            fillColor: '#0066FF',
            fillOpacity: 0.9,
            map: map,
            center: pos,
            radius: 10
        });
    }

    // Radius
    if(!my_location_radius){
        my_location_radius = new google.maps.Circle({
            strokeColor: "#0066FF",
            strokeOpacity: 0.8,
            strokeWeight: 0.5,
            fillColor: "#0066FF",
            fillOpacity: 0.25,
            map: map,
            center: pos,
            radius: 250
        });
    }

}

function drawStations(){
    if (stations){
        return;
    }
    $.ajax({
        type: 'GET',
        url: "/locator/stations",
        success: function(data) {
            stations = jQuery.parseJSON(data);
            $.each(stations , function(){
                createStationMarker(this);
            });
        }
    });
}

function createStationMarker(station) {
    var parking_icon = 'https://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png';
    var parking_marker = new google.maps.Marker({
        position: station.pos,
        icon: parking_icon,
        map: map,
        title: 'Estación - ' + station.id,
    });

    var distance = google.maps.geometry.spherical.computeDistanceBetween(
        new google.maps.LatLng(my_pos.lat, my_pos.lng),
        new google.maps.LatLng(station.pos.lat, station.pos.lng)
    );

    distance = parseInt(distance);
    if (distance > 1000){
        distance = distance / 1000;
        distance = distance + ' K';
    }

    var parking_message = '' +
        '<div id="device_info"> <b> Estación - ' + station.id + '</b><br/></br></div>' +
        '<div>' +
            'Estación situada en <a href="https://www.google.es/maps/dir/'+ my_pos.lat +','+ my_pos.lng +'/' + station.address + '/@' + station.pos.lat +','+ station.pos.lng + '/" target="_blank">' + station.address + '</a>' +
        '</div>' +
        '<div>' +
            'Distancia aproximada: ' + distance + 'm.' +
        '</div>';

    var parking_info = new google.maps.InfoWindow({
        content: parking_message
    });

    google.maps.event.addListener(parking_marker, 'click', function() {
        parking_info.open(map, parking_marker);
    });
}

