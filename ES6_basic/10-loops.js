export default function appendToEachArrayValue(array, appendString) {
  const nArr = [];

  for (const idx of array) {
    nArr.push(appendString + idx);
  }

  return nArr;
}
