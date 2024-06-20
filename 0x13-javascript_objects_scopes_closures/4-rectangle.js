#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let st = '';
      for (let j = 0; j < this.width; j++) {
        st += 'X';
      }
      console.log(st);
    }
  }

  rotate () {
    const awx = this.width;
    this.width = this.height;
    this.height = awx;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
module.exports = Rectangle;
