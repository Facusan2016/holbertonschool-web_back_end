export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqf() {
    return this._sqft;
  }

  static evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
