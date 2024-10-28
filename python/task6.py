
import re
from typing import List, Optional, Dict, Tuple

class RegexOperations:
    def __init__(self) -> None:
        pass

    def match_pattern(self, pattern: str, text: str) -> List[str]:
        """Matches the regex pattern against the text and returns the matched results."""
        try:
            matches = re.findall(pattern, text)
            return matches
        except re.error as e:
            print(f"Regex error: {e}")
            return []

    def extract_capture_groups(self, pattern: str, text: str) -> Optional[Dict[str, str]]:
        """Extracts named capture groups from matched results."""
        try:
            match = re.search(pattern, text)
            if match:
                return match.groupdict()
            else:
                print("No match found.")
                return None
        except re.error as e:
            print(f"Regex error: {e}")
            return None

    def manipulate_text(self, pattern: str, replacement: str, text: str) -> str:
        """Replaces specific patterns in the text with desired replacements using regex."""
        try:
            modified_text = re.sub(pattern, replacement, text)
            return modified_text
        except re.error as e:
            print(f"Regex error: {e}")
            return text

    def validate_input(self, input_text: str, pattern: str) -> bool:
        """Validates input based on the provided regex pattern."""
        try:
            return bool(re.match(pattern, input_text))
        except re.error as e:
            print(f"Invalid regex pattern: {e}")
            return False

    def split_text(self, pattern: str, text: str) -> List[str]:
        """Splits the text into specific components using a regex pattern."""
        try:
            return re.split(pattern, text)
        except re.error as e:
            print(f"Regex error: {e}")
            return []

    def join_text(self, components: List[str], delimiter: str) -> str:
        """Joins separate components into a single text with the specified delimiter."""
        return delimiter.join(components)


class Operations:
    regex_ops = RegexOperations()
    def choice_match_pattern(self):
        pattern = input("Enter regex pattern: ")
        text = input("Enter text string: ")
        matches = self.regex_ops.match_pattern(pattern, text)
        print("Matched Results:", matches)

    def choice_extract_capture_groups(self):
        pattern = input("Enter regex pattern with named capture groups (e.g., (?P<name>\w+)) : ")
        text = input("Enter text string: ")
        extracted_info = self.regex_ops.extract_capture_groups(pattern, text)
        print("Extracted Information:", extracted_info)

    def choice_manipulate_text(self):
        pattern = input("Enter regex pattern to replace: ")
        replacement = input("Enter replacement text: ")
        text = input("Enter original text: ")
        modified_text = self.regex_ops.manipulate_text(pattern, replacement, text)
        print("Modified Text:", modified_text)

    def choice_validate_input(self):
        input_text = input("Enter text to validate: ")
        pattern = input("Enter regex pattern for validation: ")
        is_valid = self.regex_ops.validate_input(input_text, pattern)
        print(f"Validation Result: {'Valid' if is_valid else 'Invalid'}")

    def choice_split_and_join_text(self):
    
        action = input("Enter 'split' to split or 'join' to join text: ").lower()
        text = input("Enter text string: ")
        if action == 'split':
            pattern = input("Enter regex pattern to split by: ")
            split_result =self.regex_ops.split_text(pattern, text)
            print("Split Result:", split_result)
        elif action == 'join':
            components = input("Enter components separated by a comma: ").split(',')
            delimiter = input("Enter delimiter to join with: ")
            joined_text = self.regex_ops.join_text([component.strip() for component in components], delimiter)
            print("Joined Text:", joined_text)
        else:
            print("Invalid action.")

def main() -> None:
    operation=Operations()

    while True:
        print("\nRegex Operations Menu:")
        print("1. Pattern Matching")
        print("2. Capture Group Extraction")
        print("3. Text Manipulation")
        print("4. Validation")
        print("5. Splitting and Joining")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            operation.choice_match_pattern()

        elif choice == '2':
            operation.choice_extract_capture_groups()

        elif choice == '3':
            operation.choice_manipulate_text()

        elif choice == '4':
            operation.choice_validate_input()
           
        elif choice == '5':
           operation.choice_split_and_join_text()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()


