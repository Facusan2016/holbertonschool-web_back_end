export default class HolbertonCourse {
  constructor(name, length, students) {
    
    if (typeof (name) === 'string') {
      this.__name = name;
    } else {
      throw new TypeError('Name must be a string');
    }

    if (typeof (l) === 'number') {
      this.__length = l;
    } else {
      throw new TypeError('Length must be a number');
    }

    if (std.every((i) => typeof i === 'string')) {
      this.__students = std;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }

  get name() {
    return this.__name;
  }

  set name(name) {
    if (typeof (name) === 'string') {
      this.__name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    return this.__length;
  }

  set length(l) {
    if (typeof (l) === 'number') {
      this.__length = l;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get students() {
    return this.__students;
  }

  set students(std) {
    if (std.every((i) => typeof i === 'string')) {
      this.__students = std;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
