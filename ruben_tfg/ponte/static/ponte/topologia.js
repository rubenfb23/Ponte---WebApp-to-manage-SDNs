function createTopology(dispositivos) {
    
    console.log(dispositivos);
    // Your d3 network chart code goes here
    // Example code for creating a network chart using d3.js
    // Replace this code with your own implementation

    // Set up the SVG container
    var svg = d3.select("#box")
        .append("svg")
        .attr("width", '100%')
        .attr("height", '100%');

    svg_height = svg.style("height").replace("px", "");
    svg_width = svg.style("width").replace("px", "");

    var nodes = [];
    var links = [];
    // Define the data for the network
    for (var i = 0; i < dispositivos.length; i++) {
        var nombre = dispositivos[i].nombre;
        var id = i;

        nodes.push({ name: nombre, id: id });
    }

    for (var j = 0; j < nodes.length - 1; j++) {
        links.push({ source: j, target: j+1});
    }
    
    console.log(nodes);
    console.log(links);
    // Create the force simulation
    var simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(function(d) { return d.id; }))
        .force("charge", d3.forceManyBody().strength(-200)) // Increase the repulsion force
        .force("mindistance", d3.forceManyBody().distanceMin(1)) // Increase the repulsion force
        .force("center", d3.forceCenter(svg_width/2, svg_height/2))
        .force("collision", d3.forceCollide().radius(50)); // Add collision force with a radius of 50

    // Create the links
    var link = svg.selectAll(".link")
        .data(links)
        .enter()
        .append("line")
        .attr("class", "link")
        .attr("stroke-width", 2)
        .attr("stroke", "blue");

    // Create the nodes
    var node = svg.selectAll(".node")
        .data(nodes)
        .enter()
        .append("g")
        .attr("class", "node")
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
        );

    // Append a circle to each node
    node.append("circle")
        .attr("r", 40)
        .attr("fill", "lightblue") 
        .attr("stroke", "blue")
        .on("click", function(d) {
            console.log("Node clicked:", d);
            // Handle node click event here
        });

    node.append("text")
        .attr("class", "material-icons")
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "central")
        .text(function(d) {
            switch (d.name) {
                case "PC":
                    return "computer";
                case "Raspberry":
                    return "developer_board";
                case "Router":
                    return "router";
                default:
                    return "device_unknown";
            }
        }
    );

    // Update the simulation on each tick
    simulation.on("tick", function() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) {
            return "translate(" + d.x + "," + d.y + ")";
        });
    });

    // Drag event handlers
    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
    
}