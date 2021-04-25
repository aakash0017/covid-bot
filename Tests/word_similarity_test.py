import sys
import pytest
sys.path.append('../')
from utility.wordSimilarity import  check_city_similarity

@pytest.mark.parametrize("a,b", [
  ('jaipur', check_city_similarity('jaipur')),
])

def test_for_cities(a,b):
    assert a == b



