build_DD()

function build_DD() {
    var dd_stuff = Plotly.d3.select("selDataset")
    var dd_url = "/names";
    Plotly.d3.json(dd_url, function (error, response) {
        // if error
        // loop & append
        for (var i = 0; i < response.length; i++){
            // create option tag
            // get the element
            // add text
            // add value to option tag
            // append to dropdown
            dd_stuff.appe 
            for(var i = 0; i< response.length;i++){
                var elements = document.createElement("option");
                var arr = response[i];
                elements.textContent = arr;
                elements.value = arr;
                dropdown.appendChild(elements);
        };
        }

    })
}



function buildPlot() {
    /* data route */
    var url = "/api/pals";
    Plotly.d3.json(url, function (error, response) {

        console.log(response);

        var data = response

        var layout = {
            scope: "usa",
            title: "Pet Pals",
            showlegend: false,
            height: 600,
            // width: 980,
            geo: {
                scope: "usa",
                projection: {
                    type: "albers usa"
                },
                showland: true,
                landcolor: "rgb(217, 217, 217)",
                subunitwidth: 1,
                countrywidth: 1,
                subunitcolor: "rgb(255,255,255)",
                countrycolor: "rgb(255,255,255)"
            },
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();
