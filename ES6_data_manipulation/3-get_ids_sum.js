export default function getStudentIdsSum(stdList) {
  const sum = stdList.reduce((acc, current) => acc + current.id, 0);
  return sum;
}
