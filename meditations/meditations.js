<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hierarchical Edge Bundling Visualization</title>
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
  <svg width="960" height="600"></svg>
  <script>
    d3.json("meditation_data.json").then(function(data) {
      const root = d3.hierarchy(data);
      const links = root.links();
      const layout = d3.cluster().size([2 * Math.PI, Math.min(700, 960) / 2 - 100]);
      layout(root);

      const svg = d3.select("svg");
      const g = svg.append("g")
          .attr("font-family", "sans-serif")
          .attr("font-size", 10)
          .attr("transform", "translate(480,300)");

      const link = g.append("g")
        .attr("fill", "none")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.4)
        .attr("stroke-width", 1.5)
      .selectAll("path")
      .data(links)
      .join("path")
        .each(function(d) { d.target.linkNode = this; })
        .attr("d", d3.linkRadial()
            .angle(d => d.x)
            .radius(d => d.y));

      const node = g.append("g")
          .attr("stroke-linejoin", "round")
          .attr("stroke-width", 3)
        .selectAll("g")
        .data(root.descendants().reverse())
        .join("g")
          .attr("transform", d => `
            rotate(${d.x * 180 / Math.PI - 90})
            translate(${d.y},0)
          `);

      node.append("circle")
          .attr("fill", d => d.children ? "#555" : "#999")
          .attr("r", 2.5);

      node.append("text")
          .attr("dy", "0.31em")
          .attr("x", d => d.x < Math.PI === !d.children ? 6 : -6)
          .attr("text-anchor", d => d.x < Math.PI === !d.children ? "start" : "end")
          .attr("transform", d => d.x >= Math.PI ? "rotate(180)" : null)
          .text(d => d.data.name)
        .clone(true).lower()
          .attr("stroke", "white");

      link.on("mouseover", highlightLink);
      link.on("mouseout", restoreLinks);

      function highlightLink(event, d) {
        link.attr("stroke", null);
        d3.select(d.target.linkNode).attr("stroke", "orange");
      }

      function restoreLinks() {
        link.attr("stroke", "#555");
      }
    });
  </script>
</body>
</html>
