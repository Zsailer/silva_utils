from ..base import *
from ..search import *


def test_search_for_root_distance():
    # This test is extremely slow...
    taxon = "Austwickia chelonae"

    # Load tree
    species_tree = load_silva_tree()
    species_tree_labels = species_tree.taxon_namespace.labels()

    # Calculate distance
    distance = search_for_root_distance(taxon, species_tree, species_tree_labels)
    assert type(distance) == float
    assert distance > 0
    assert distance < 1
