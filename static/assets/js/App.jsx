// App.jsx
import React from "react";
import ReactCursorPosition from 'react-cursor-position';

export default class App extends React.Component {
  render() {
    return (
      <ReactCursorPosition className="floorplan">
        <MouseCoordinates />
      </ReactCursorPosition>
    );
  }
}

class MouseCoordinates extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recordedPoints: [],
      lastPosition: [],
      outsidePoints: []
    };
  }
  handleMouseMove(e) {
    var currentPosition = [this.props.position.x, this.props.position.y];

    this.setState({
      recordedPoints: this.state.recordedPoints.concat([currentPosition])
    });
  }
  drawPoints() {
    const points = this.state.recordedPoints.map((point) =>
      <circle cx={point[0]} cy={point[1]} r="25" stroke="black" stroke-width="1" fill="red" />

    );
    return points;
  }
  drawPolygon() {
    const points = this.state.recordedPoints.map((point) =>
      <circle points={this.getSquare(point)} />

    );
    //return (<polygon points={this.getSquare(position).toString()} />);
    return points;
  }
  getSquare(position) {
    var x = position[0];
    var y = position[1];
    return `${x - 20},${y + 20} ${x + 20},${y + 20} ${x + 20},${y - 20} ${x - 20},${y - 20}`;
  }
  render() {
    var currentPosition = [this.props.position.x, this.props.position.y];
    return (
      <div id="demo-wrapper">
            <h1 class="display-4">{"("+currentPosition[0]+", " + currentPosition[1] + ")"}</h1>
        <div id="heatmap"></div>
      </div>
    );
  }
}
