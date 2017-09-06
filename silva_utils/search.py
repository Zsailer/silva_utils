# Calculate root distances
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import dendropy as d

def search_for_root_distance(taxon, species_tree, species_tree_labels):
    """Search for taxon in species tree and calculate distance from root."""

    # Fuzzy search species tree for best match
    match = process.extractOne(taxon, species_tree_labels)
    label = match[0]

    # Find label in species tree and get node.
    node = species_tree.find_node_with_taxon_label(label)

    # Calculate node distance from root.
    distance = node.distance_from_root()

    return distance
