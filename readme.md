# Diel-Vertical Migration in Marine Zooplankton

Non-directional photoreceptors are the evolutionary precursors of all animal eyes; they enable the monitoring of ambient light intensity and regulate feeding, movement and reproduction. While the first animals were most likely benthic, they evolved larval stages very early on, thus conquering a new ecological niche: the pelagic. In this realm, the evolutionary pressure to prey but not be preyed upon became stronger. This implied strong selection for better sensory systems, including photoreception.

How were the photoreceptor systems of the earliest primary larvae arranged? Did this system mediate vertical migration, the largest movement of biomass on Earth? To try to answer these questions, we chose the zooplanktonic larva of three ambulacrarian species: the sea urchin *Strongylocentrotus purpuratus*, the starfish *Luidia sarsi*, and the hemichordate Schizocardium spp., as a model. A comprehensive array of techniques was applied, covering levels of organization from genes to behaviour. Opsin-positive cells of *S. purpuratus* were characterized in terms of molecular fingerprint and morphology. A custom-built behavioural set-up is used to investigate the vertical migration of these larvae under different light conditions. Based on our findings, a novel mechanistic model for understanding simple photodetection will be proposed.

## Aims and presentation of the custom-built set-up

The main goal of this project is to apply the contents explored during this MAMED course held at Villefranche-sur-Mer. 

More in concrete, I will try to adapt a JavaScripts visualization program previously develop in D3js.org for tracing the populational movements of three marine zooplaktonic larvae (echinopluteus, tornaria and auricularia) in a diel-vertical migration custom-built set-up. 

This set-up is being created in collaboration with Dan-Eric Nilsson (Vision Group, Lund University), and allows to analize the movements of a population of marine invertebrate larvae located in a 400X10X10mm water column during time. For this first assay, the light coming from the surface will be UV. The light cycle will be 12/12h (UV/Dark conditions) and changes in light intensity will be done by means of a gaussian function. Future hardware implementations will allow to change the different light conditions available in the set-up.

![Figure 1] (https://github.com/AlbertoValero/neptune_final_project/blob/master/Poster%20sep2015.jpg)

_**Figure 1.** A custom made behavioural set-up created in the Vision Group (Lund University; Sweden)_

Once I am able to convert my data into a .tsv file I will create a Multi-Series Line Chart extracted from bl.ocks.org. Further, I will benefit of markdown to format my text file and include images and references. If time permits, I will try to add the spectral properties that I measure of each of the LEDs associated to this system. In the future, the movements of the larvae will be plotted in a dinamic time-lapse sequence like the one that you can find in: https://fbe94b5b83362330a8429bb16098a3285147bcbf.googledrive.com/host/0Bz6WHrWac3FrZUtuOExWdlRGVG8/sportskills.html.

## Classes of Photoreceptive Sensory Tasks

While the vast majority of studies had been focus on directional photoreceptors – systems comprising at least one cell with a photosensitive opsin and shading pigments that enable it to discriminate light directionality – less is known about non-directional photoreception, which is considered the earliest evolving type of photoreception. 

Non-directional photoreceptors, which can be difficult to detect without molecular tools, allow to monitor the ambient light intensity. They are widely used as an input to the circadian clock system and also for a wide variety of other tasks. For instance, non-directional photoreceptors can be used for detecting shadows or harmful levels of UV radiation or be involved in the regulation of feeding, movement and reproduction rhythms (Bennett, 1979; Paul and Gwynn-Jones, 2003; Leech et al., 2005; Nilsson, 2009; 2013).

![Figure 2] (https://github.com/AlbertoValero/neptune_final_project/blob/master/Screen%20Shot%202016-03-03%20at%2017.23.09.png)

_**Figure 2.** Different photoreception classes defined by Nilsson (2009) and visual task associated with each of them._

## Importance of Marine Zooplankton for understanding the Origin of Vision

To elucidate the origins of animal vision, an event that most probably happened in the Precambrian, a better understanding of the mechanisms of non-directional photoreception is required. While ancestral adult metazoans were likely benthic, it is probable that a pelagic larval stage evolved very early on in animal evolution (Nielsen, 2008). This idea had led to investigate the directional simple eyespots of marine ciliated larvae in search of something resembling a ‘proto-eye’ (Smith, 1935; Thorson, 1964; Brandenburger et al., 1973; Marsden, 1984; Pires and Woollacott, 1997; Leys and Degnan, 2001; Nordström et al., 2003; Jékely et al., 2008; Gühmann et al., 2015). Such simple eyespots or ocelli constitute class II photoreceptors in accordance with the classification of Nilsson (2013). However, to our knowledge, in only a few cases have non-directional (class I) photoreceptors been documented (Arendt et al., 2004; Passamaneck et al., 2011; Voecking et al., 2015).

The current study represents the first attempt to identify unpigmented photoreceptor cells in a zooplanktonic larva of the deuterostome lineage. In my work I try to better-understand and compare the phototactic behaviour of the echinopluteus of *Strongylocentrotus purpuratus* (Echinoidea), the auricularia of *Luidia sarsi* (Asteroidea), and the tornaria of Schizocardium spp (Hemichordata).

## What diel-vertical migration is

Every day, zooplankton make their way to deep water and rise. This process, known as diel vertical migration, is carried out all over the world by marine and freshwater plankton alike. The reason for this has long been attributed to the trade-off between obtaining tasty morsels in the surface ocean and avoiding becoming a tasty morsel for predators while they're there.

## Material and Methods

This is the native code used for generating Fig. 3

	index.html#

	<!DOCTYPE html>
	<meta charset="utf-8">
	<style>

	body {
	  font: 10px sans-serif;
	}

	.axis path,
	.axis line {
	  fill: none;
	  stroke: #000;
	  shape-rendering: crispEdges;
	}

	.x.axis path {
	  display: none;
	}

	.line {
	  fill: none;
	  stroke: steelblue;
	  stroke-width: 1.5px;
	}

	</style>
	<body>
	<script src="//d3js.org/d3.v3.min.js"></script>
	<script>

	var margin = {top: 20, right: 80, bottom: 30, left: 50},
	    width = 960 - margin.left - margin.right,
	    height = 500 - margin.top - margin.bottom;

	var parseDate = d3.time.format("%Y%m%d").parse;

	var x = d3.time.scale()
	    .range([0, width]);

	var y = d3.scale.linear()
	    .range([height, 0]);

	var color = d3.scale.category10();

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");

	var line = d3.svg.line()
	    .interpolate("basis")
	    .x(function(d) { return x(d.date); })
	    .y(function(d) { return y(d.temperature); });

	var svg = d3.select("body").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	d3.tsv("data.tsv", function(error, data) {
	  if (error) throw error;

	  color.domain(d3.keys(data[0]).filter(function(key) { return key !== "date"; }));

	  data.forEach(function(d) {
	    d.date = parseDate(d.date);
	  });

	  var cities = color.domain().map(function(name) {
	    return {
	      name: name,
	      values: data.map(function(d) {
	        return {date: d.date, temperature: +d[name]};
	      })
	    };
	  });

	  x.domain(d3.extent(data, function(d) { return d.date; }));

	  y.domain([
	    d3.min(cities, function(c) { return d3.min(c.values, function(v) { return v.temperature; }); }),
	    d3.max(cities, function(c) { return d3.max(c.values, function(v) { return v.temperature; }); })
	  ]);

	  svg.append("g")
	      .attr("class", "x axis")
	      .attr("transform", "translate(0," + height + ")")
	      .call(xAxis);

	  svg.append("g")
	      .attr("class", "y axis")
	      .call(yAxis)
	    .append("text")
	      .attr("transform", "rotate(-90)")
	      .attr("y", 6)
	      .attr("dy", ".71em")
	      .style("text-anchor", "end")
	      .text("Temperature (ºF)");

	  var city = svg.selectAll(".city")
	      .data(cities)
	    .enter().append("g")
	      .attr("class", "city");

	  city.append("path")
	      .attr("class", "line")
	      .attr("d", function(d) { return line(d.values); })
	      .style("stroke", function(d) { return color(d.name); });

	  city.append("text")
	      .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
	      .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.temperature) + ")"; })
	      .attr("x", 3)
	      .attr("dy", ".35em")
	      .text(function(d) { return d.name; });
	});

	</script>

The tools I used were... See analysis files at (links to analysis files).

## Results

![Figure 3] (Screen%20Shot%202016-06-09%20at%2012.37.33.png)

In Figure 1 you can compare the occurence of these zooplanktonic larvae during time.

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


