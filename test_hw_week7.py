import io, sys
import textwrap

try:
    from hw_week7 import hw_week7
except ImportError:
    from hw_week7_solution import hw_week7

class Test:
    def test_function(self, capsys):

        user_input = """\
        1
        20
        15
        """
        expected_output = """\
        Take a guess.
        Your guess is too low.
        Take a guess.
        Your guess is too high.
        Take a guess.
        Good job! You guessed my number in 3 guesses!
        """

        sys.stdin = io.StringIO(textwrap.dedent(user_input))
        hw_week7(15)
        captured = capsys.readouterr()
        assert captured.out == textwrap.dedent(expected_output)

    def setup_method(self):
        self.orig_stdin = sys.stdin

    def teardown_method(self):
        sys.stdin = self.orig_stdin
