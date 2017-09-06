import dendropy as d

SILVA_TREE_URL = "https://www.arb-silva.de/fileadmin/silva_databases/living_tree/LTP_release_128/LTPs128_SSU/LTPs128_SSU_tree.newick"

def load_silva_tree():
    """Load the SILVA living tree."""
    return d.Tree.get(url=SILVA_TREE_URL, schema="newick")
