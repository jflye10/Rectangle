# Joshua Flye, CIS 261, Rectangle

class Rectangle:
    """
    A class to represent a rectangle with properties height and width,
    and methods to calculate its perimeter, area, and print its details.
    """

    def __init__(self, height, width):
        """
        Initializes a new Rectangle object.

        Args:
            height (float or int): The height of the rectangle.
            width (float or int): THe width of the rectangle.
        """
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a non-negative number.")
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a non-negative number.")

        self.height = height
        self.width = width

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)
    def calculate_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.height * self.width

    def print_rectangle(self):
        """
        Prints the details of the rectangle, including its height, width,
        perimeter, and area.
        """
        print(f"Height: {self.height}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {int(self.calculate_perimeter())}")
        print(f"Area: {int(self.calculate_area())}")

    def draw_rectangle(self):
        """
        Draws a textual representation of the rectangle using asterisks.
        """
        if self.height <= 0 or self.width <= 0:
            print("Cannot draw rectangle with non-positive dimensions.")
            return

        print("*" * int(self.width))
        for _ in range(int(self.height) - 2):
            print("*" + " " * (int(self.width) - 2) + "*")
        if self.height > 1:
            print("*" * int(self.width))

def run_rectangle_calculator():
    """
    Runs the interactive rectangle calculator.
    """
    print("Rectangle Calculator")
    while True:
        try:
            height = float(input("Enter Height: "))
            width = float(input("Enter Width: "))

            rect = Rectangle(height, width)
            rect.print_rectangle()
            rect.draw_rectangle()

        except ValueError as e:
            print(f"Errpr: {e}. Please enter valid numbers for dimensions.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

        cont = input("\nContinue? (y/n): ").strip().lower()
        if cont != 'y':
            break
if __name__ == "__main__":
    run_rectangle_calculator()


