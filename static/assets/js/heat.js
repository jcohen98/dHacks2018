var heatmapInstance = h337.create({
      container: document.getElementById('heatmap'),
      radius: 15,
    });
    document.getElementById('demo-wrapper').onmousemove = function (ev) {
      heatmapInstance.addData({
        x: ev.layerX,
        y: ev.layerY,
        value: 1
      });
    };
