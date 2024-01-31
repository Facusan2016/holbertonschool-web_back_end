const eqSet = (xs, ys) => xs.size === ys.size
    && [...xs].every((x) => ys.has(x));

export default function hasValuesFromArray(set, array) {
  const setArr = new Set(array);
  const intersect = new Set([...setArr].filter((i) => set.has(i)));

  return eqSet(intersect, setArr);
}
