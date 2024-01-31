export default function cleanSet(set, startString) {
  const resStr = [];

  if (startString.length === 0) return '';

  Array.from(set).map((e) => {
    const position = e.search(startString);

    if (position !== -1) resStr.push(e.slice(position + startString.length));
    return null;
  });

  return resStr.join('-');
}
