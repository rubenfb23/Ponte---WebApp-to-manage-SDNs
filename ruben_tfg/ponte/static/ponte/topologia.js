function createTopology(dispositivos) {
    
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
        .force("mindistance", d3.forceManyBody().distanceMin(100)) // Increase the repulsion force
        .force("center", d3.forceCenter(svg_width/2, svg_height/2))
        .force("collision", d3.forceCollide().radius(50)) // Add collision force with a radius of 50
        .force("x", d3.forceX(svg_width/2));

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
        .on("mouseover", function(d) {
            d3.select(this).select("circle").transition()
                .duration(250)
                .attr("r", 50)
                .attr("stroke", "red")
            d3.select(this).select("text").transition()
                .duration(250)
                .attr("font-size", 30)
        })
        .on("mouseout", function(d) {
            d3.select(this).select("circle").transition()
                .duration(250)
                .attr("r", 40)
                .attr("stroke", "blue")
            d3.select(this).select("text").transition()
                .duration(250)
                .attr("font-size", 20)
        })
        .on("click", function(d) {
            console.log("Node clicked:", d);
            // Open modal window here
            openModal(d);
        })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
        )
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
            // Open modal window here
            openModal(d);
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
        })
        .on("click", function(d) {
            console.log("Node clicked:", d);
            // Open modal window here
            openModal(d);
        });

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

    var autorefreshEnabled = false;

    // Create the toggle switch
    var toggleSwitchOutside = svg.append("g")
        .attr("class", "toggle-switch-outside")
        .attr("transform", "translate(" + (5) + ", 5)")

    var toggleSwitch = svg.append("g")
        .attr("class", "toggle-switch")
        .attr("transform", "translate(" + (35) + ", 10)")
        .on("click", toggleAutorefresh);

    toggleSwitchOutside.append("rect")
        .attr("width", 100)
        .attr("height", 40)
        .attr("rx", 15)
        .attr("ry", 15)
        .attr("fill", "beige");

    toggleSwitch.append("rect")
        .attr("width", 60)
        .attr("height", 30)
        .attr("rx", 15)
        .attr("ry", 15)
        .attr("fill", function() {
            if (autorefreshEnabled) {
                return "lightgreen";
            } else {
                return "lightcoral";
            }
        });

    toggleSwitch.append("circle")
        .attr("cx", function() {
            if (autorefreshEnabled) {
                return 45;
            } else {
                return 15;
            }
        })
        .attr("cy", 15)
        .attr("r", 12)
        .attr("fill", "white");

    toggleSwitch.append("text")
        .attr("x", -30)
        .attr("y", 27)
        .attr("class", "material-icons")
        .text("refresh");

    // Function to toggle autorefresh
    function toggleAutorefresh() {
        autorefreshEnabled = !autorefreshEnabled;
        if (autorefreshEnabled) {
            toggleSwitch.select("rect").transition()
                .duration(250)
                .attr("fill", "lightgreen");
            toggleSwitch.select("circle").transition()
                .duration(250)
                .attr("cx", 45);
        } else {
            toggleSwitch.select("rect").transition()
                .duration(250)
                .attr("fill", "lightcoral");
            toggleSwitch.select("circle").transition()
                .duration(250)
                .attr("cx", 15);
        }
    }

    // Function to open modal window
    function openModal(d) {
        // Check if a modal is already open
        var existingModal = document.querySelector(".modal");
        if (existingModal) {
            // Remove the existing modal
            existingModal.remove();
        }

        // Create a modal window
        var modal = document.createElement("div");
        modal.classList.add("modal");

        // Create modal content
        var modalContent = document.createElement("div");
        modalContent.classList.add("modal-content");

        // Create close button
        var closeButton = document.createElement("span");
        closeButton.classList.add("material-icons");
        closeButton.textContent = "close";

        // Add event listener to close the modal
        closeButton.addEventListener("click", function() {
            modal.remove();
        });

        // Append close button to modal content
        modalContent.appendChild(closeButton);

        // Create and append information to modal content
        var info = document.createElement("p");
        info.textContent = "This is the information you want to display.";
        modalContent.appendChild(info);

        // Append modal content to modal window
        modal.appendChild(modalContent);

        // Append modal window to the document body
        document.body.appendChild(modal);
    }
}