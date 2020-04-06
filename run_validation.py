import configuration
from parse import parse_rdf_graph
from triple_coherence import run_triple_coherence_validation
from triple_resolvability import run_triple_resolvability_validation

# Initiate an empty list to store unresolvable IRIs
unresolvable_list = []

# Initiate an empty list to store incoherent triples
incoherent_property_list = []

print("Start parsing RDF graphs from {}.".format(configuration.file))
g = parse_rdf_graph(file_name=configuration.file, graph_format=configuration.graph_format)

print("Start validating resolvability of RDF IRIs, and coherence of RDF predicates")
for triple in g:
    unresolvable_list = unresolvable_list + run_triple_resolvability_validation(triple)
    incoherent_property_list = incoherent_property_list + run_triple_coherence_validation(triple)

print("In summary: \n  Unresolvable IRIs are: ", list(set(unresolvable_list)),
      "\n  Triples using incohenrent properties are: ", incoherent_property_list)