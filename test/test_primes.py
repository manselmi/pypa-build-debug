# third-party imports
import pytest

# first-party imports
from pypa_build_debug import primes


@pytest.mark.parametrize(
    ('input_expected', 'output_expected'),
    [
        (0, []),
        (1, [2]),
        (2, [2, 3]),
    ],
)
def test_valid_input(input_expected, output_expected):
    assert primes(input_expected) == output_expected
