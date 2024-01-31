export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsByCity = studentList.filter((student) => student.location === city);
  const updatedStudents = studentsByCity.map((student) => {
    const grade = newGrades.find((grade) => grade.studentId === student.id);
    const updatedStudent = { ...student }; // Create a copy of the student object
    if (grade) {
      updatedStudent.grade = grade.grade;
    } else {
      updatedStudent.grade = 'N/A';
    }
    return updatedStudent;
  });

  return updatedStudents;
}
