export default function createInt8TypedArray(length, position, value) {
  const unit8 = new ArrayBuffer(length);
  const view = new DataView(unit8);

  try {
    view.setInt8(position, value);
    return view;
  } catch (error) {
    throw new Error('Position outside range');
  }
}
