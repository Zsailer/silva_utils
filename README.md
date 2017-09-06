# Python functions for searching SILVA living tree

A suite of useful functions for searching the [SILVA](https://www.arb-silva.de/) rRNA database project.

## Usage

Load the SILVA bacterial species tree

```python
import silva_utils as su

# Returns a Dendropy tree
species_tree = su.load_silva_tree()
```

Calculate distance of a taxon from root of species tree:

```python
taxon = 'Austwickia chelonae'

# Get a list of all species in SILVA tree.
species_list = tree.taxon_namespace.labels()

# Search
distance = su.search_for_root_distance(taxon, species_tree, species_list)

print(distance) # prints 0.560
```


## Installation

Clone this repo and install development version using pip:
```
pip install -e .
```
