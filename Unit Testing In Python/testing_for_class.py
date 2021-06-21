from unittest import TestCase

class PrinterError(RuntimeError):
    pass

# class Code
class Printer:
    def __init__(self, pages_per_second: float, capacity: int):
        self.pages_per_second = pages_per_second
        self.capacity = capacity

    def print(self, pages):
        if pages > self.capacity:
            raise PrinterError("You Can Not Print More Than Printer Capacity.")

        self.capacity -= pages

        return f'Printed {pages} pages in {pages/self.pages_per_second:.2f} seconds.'


# Testing Code

class PrinterTest(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_second=2, capacity=300)

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer.capacity)


    def test_printer_speed(self):
        pages = 10
        expected = 'Printed 10 pages in 5.00 seconds.'
        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_second=3.0, capacity=300)
        pages = 11
        expected = 'Printed 11 pages in 3.67 seconds.'

        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_runs_end_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)