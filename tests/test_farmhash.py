from __future__ import absolute_import
import pytest

import farmhash


@pytest.mark.parametrize('input, expected', [
    ('hello world', 2346102811),
])
def test_hash32(input, expected):
    assert farmhash.hash32(input) == expected
