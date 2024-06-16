def test_function(arg1: int, arg2: str, arg3: float) -> str:
    """
    This is a test function.

    Args:
        arg1 (int): The first argument.
        arg2 (float): The second argument.

    Returns:
        str: The concatenated string.
    """
    # Your code here
    return str(arg1) + arg2 + str(arg3)

class TestClass:
    def __init__(self, arg1: int, arg2: float):
        """
        Initializes the TestClass instance.

        Args:
            arg1 (int): The first argument.
            arg2 (float): The second argument.
        """
        self.arg1 = arg1
        self.arg2 = arg2

    def add(self, arg3: float) -> str:
        """
        This is the first test method.

        Args:
            arg3 (float): The third argument.

        Returns:
            float: added

        example:
            >>>TestClass(1,2).add(5) == 7

        """
        return self.arg1 + self.arg2 + arg3

    def multiply(self) -> str:
        """
        This is the second test method.

        Args:
            arg4 (bool): The fourth argument.

        Returns:
            float: mutipled attrs
        """
        return self.arg1 * self.arg2