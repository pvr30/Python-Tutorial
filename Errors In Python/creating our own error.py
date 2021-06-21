#  Creating our own errors
# Here All Error are class So we just inherit form typeerror for our own error.

"""
Sometimes it can be useful to create and raise errors with names we define,
as opposed to only using the built-in errors.

If we want to create a custom error, we can do so very easily by
subclassing the `Exception` class:

"""
"""class My_error(TypeError):
      pass

raise My_error("Hello i Am Error") """

"""This `MyCustomError` class just inherits everything
from `Exception`, which means it behaves just like any other error. """

"""class MyCustomError(Exception):
      def __init__(self, message, code):
          super().__init__(message)
          self.code = code




raise MyCustomError("Message Describe The Error.", 200)

"""

# Docstrings
"""
Docstrings in Python are just strings that are commonly used to describe what a class or function does or when it should be used.

A docstring has this format:
"""

"""
Your docstring goes here.
"""

"""
It so happens that in Python the triple-quotation mark is a *multi-line string*. You can use it instead of a normal string anywhere, if you want multiple lines.

But back to docstrings! We can add a docstring to our exception to explain when it should be used:
"""

class MyErrorWithCode(Exception):
    """Exception raised when a specific error code is needed."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


error = MyErrorWithCode("Message Describe The Error", 404)
print(error.__doc__)

"""
Notice how here the multi-line string is in one line; and that’s OK. We could put it into multiple lines if we want to.
"""