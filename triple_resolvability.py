from query import construct_sparql, generate_query_string
import configuration as config
from rdflib.term import Literal


def iri_resolvability_validation(iri):
    # Get query string (that aims to find all triples for the given IRI)
    query_string = generate_query_string(query_type="get_all", iri=iri)
    # Run SPARQL query to obtain RDF resources in the IRI. If no information exists, the IRI is not resolvable.
    if len(construct_sparql(config.sparql_service, query_string)) == 0:

        return iri


def run_triple_resolvability_validation(triple):

    # Assign RDF subjects
    s = triple[0].n3()

    # Assign RDF predicates
    p = triple[1].n3()

    # Distinguish between literal objects and IRI objects, and assign them
    if isinstance(triple[2], Literal):
        o = triple[2].datatype.n3()
    else:
        o = triple[2].n3()

    # Return a list of unresolvable IRIs
    triple_unresolvable_list = list(filter(None, [iri_resolvability_validation(x) for x in [s, p, o]]))
    print("  These IRIs are not resolvable: ", triple_unresolvable_list)

    return triple_unresolvable_list
