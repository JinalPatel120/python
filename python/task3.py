import csv
from typing import List, Dict, Any, Tuple, Optional

 

class StudentDataHandler:
    def __init__(self, file_path: str):
        self._file_path: str = file_path
        self._students: List[Dict[str, Any]] = []

    def read_data(self) -> bool:
        """
        Reads the CSV file and loads student data.
        :return: True if data is read successfully, False otherwise.
        """
        try:
            with open(self._file_path, mode='r', newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
          
             
                self._students = [
                    {
                        "name": row["name"],
                        "age": int(row["age"]),
                        "grade": float(row["grade"])
                    }
                    for row in reader if row["name"] and row["age"].isdigit() and row["grade"].replace('.', '', 1).isdigit()
                ]
            if not self._students:
                print("No valid data found in the CSV file.")
                return False
            return True
        except FileNotFoundError:
            print(f"Error: File '{self._file_path}' not found.")
            return False
        except (IOError, KeyError) as e:
            print("Error:", e)  # Print the specific error message
            print("Error: Unable to read the CSV file or missing required columns.")
            return False


    def calculate_average_grade(self) -> Optional[float]:
        """
        Calculates the average grade for all students.
        :return: The average grade, or None if no students are available.
        """
        if not self._students:
            print("No student data available.")
            return None
        total_grade = sum(student["grade"] for student in self._students)
        return total_grade / len(self._students)

    def find_highest_grade_student(self) -> Optional[Dict[str, Any]]:
        """
        Finds the student with the highest grade.
        :return: A dictionary with the student's information, or None if no students are available.
        """
        if not self._students:
            print("No student data available.")
            return None
        return max(self._students, key=lambda student: student["grade"])

    def filter_students(self, min_grade: Optional[float] = None, age_range: Optional[Tuple[int, int]] = None) -> List[Dict[str, Any]]:
        """
        Filters students by grade and/or age range.
        :param min_grade: Minimum grade to filter by.
        :param age_range: Tuple of (min_age, max_age) to filter by.
        :return: A list of filtered student dictionaries.
        """
        filtered_students = self._students

        if min_grade is not None:
            filtered_students = [student for student in filtered_students if student['grade'] >= min_grade]

        if age_range is not None:
            min_age, max_age = age_range
            filtered_students = [student for student in filtered_students if min_age <= student["age"] <= max_age]

        return filtered_students

    def sort_students(self, key: str = "name", reverse: bool = False) -> List[Dict[str, Any]]:
        """
        Sorts the students based on a specified column.
        :param key: The column to sort by, default is 'name'.
        :param reverse: Sort in descending order if True.
        :return: The sorted list of students.
        """
        if key not in ["name", "age", "grade"]:
            print("Invalid sort key provided. Defaulting to sort by 'name'.")
            key = "name"
        return sorted(self._students, key=lambda student: student[key], reverse=reverse)

    def write_data(self, file_path: str, data: List[Dict[str, Any]]) -> None:
        """
        Writes student data to a new CSV file.
        :param file_path: The output file path.
        :param data: The list of student data to write.
        """
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
            
                writer.writeheader()
                writer.writerows(data)
            print(f"Data successfully written to '{file_path}'.")
        except IOError:
            print(f"Error: Could not write to file '{file_path}'.")

    def display_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Displays student data in a readable format.
        """
        for student in data:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


def main() -> None:
    file_path = input("Enter the path to the student CSV file: ").strip()
    handler = StudentDataHandler(file_path)

    # Step 1: Read Data
    if not handler.read_data():
        return

    # Step 2: Calculate Average Grade
    average_grade = handler.calculate_average_grade()
    if average_grade is not None:
        print(f"\nAverage Grade of all students: {average_grade:.2f}")

    # Step 3: Find the Highest Grade Student
    top_student = handler.find_highest_grade_student()
    if top_student:
        print(f"\nTop Student: {top_student['name']} with Grade: {top_student['grade']}")

    try:
        min_grade = float(input("Enter minimum grade to filter students: "))
    except ValueError:
        print("Invalid input for minimum grade. Defaulting to no minimum grade filter.")
        min_grade = None

    try:
        min_age = int(input("Enter minimum age for filtering (or leave blank for no filter): ").strip() or -1)
        max_age = int(input("Enter maximum age for filtering (or leave blank for no filter): ").strip() or 100)
        age_range = (min_age, max_age) if min_age >= 0 and max_age >= 0 else None
    except ValueError:
        print("Invalid input for age range. Defaulting to no age filter.")
        age_range = None

    filtered_students = handler.filter_students(min_grade=min_grade, age_range=age_range)
    print("\nFiltered Students:")
    handler.display_data(filtered_students)

    # Step 5: Sort Students
    sort_key = input("Enter sort key (name, age, grade): ").strip()
    sort_order = input("Enter sort order (asc or desc): ").strip().lower() == "desc"
    sorted_students = handler.sort_students(key=sort_key, reverse=sort_order)
    print("\nSorted Students:")
    handler.display_data(sorted_students)

    # Step 6: Write Data
    output_file = input("Enter the output file path to save filtered data: ").strip()
    handler.write_data(output_file, sorted_students)






if __name__ == "__main__":
    main()
