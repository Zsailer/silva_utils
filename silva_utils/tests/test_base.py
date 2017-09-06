from ..base import *
import dendropy as d

def test_load_silva_tree():
    # Test loading function
    tree = load_silva_tree()
    assert type(tree) == d.Tree
