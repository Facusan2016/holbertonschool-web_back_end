export default function getStudentsByLocation(stdList, city) {
  return stdList.filter((std) => std.location === city);
}
