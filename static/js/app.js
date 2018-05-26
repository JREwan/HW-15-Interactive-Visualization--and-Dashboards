function build_DD() {
    //var dd_stuff = Plotly.d3.select("#selDataset")
    var dd_stuff = document.getElementById("selDataset")
    var dd_url = "/names";
    Plotly.d3.json(dd_url, function (error, response) {
        // if error
        // loop & append
        console.log(dd_stuff)
        for (var i = 0; i < response.length; i++){
            // create option tag
            var elements = document.createElement("option");
            // get the element
            var arr = response[i];
            // add text
            elements.textContent = arr;
            // add value to option tag
            elements.value = arr
            // append to dropdown
            console.log(elements)
            console.log(dd_stuff)
            dd_stuff.appendChild(elements);
            
        };
    })};

    build_DD()
