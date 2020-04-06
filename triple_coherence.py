from query import construct_sparql, generate_query_string
import configuration as config
from rdflib.term import Literal, URIRef


def run_triple_coherence_validation(triple):
    """
    To obtain a list of RDF triples whose property usages are not coherent with property types.
    :param triple: An iterable item in an rdflib "QueryResult" object.
    :return: A list of tuples with each tuple representing an RDF triple whose property usage is not coherent
    with property type.
    """

    # Assign RDF terms
    target_subject = triple[0]
    target_property = triple[1]
    target_object = triple[2]

    # Initiate an empty list to store incoherent triples
    incoherent_triple_list = []

    if target_property.n3() != "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>":
        # Obtain query results of "rdf:type" triples with the target property as the subject
        p_sparql_results = construct_sparql(config.sparql_service,
                                            generate_query_string(query_type="get_type", iri=target_property.n3()))

        # To inspect the owl type of the target property
        for _, _, property_type in p_sparql_results:
            # If the target property is object property:
            if property_type.n3() == "<http://www.w3.org/2002/07/owl#ObjectProperty>":
                # If the target object of the target property is IRI:
                if isinstance(target_object, URIRef):
                    # The target triple is coherent.
                    pass
                # Else the target triple is not coherent, and store the triple
                else:
                    incoherent_triple_list.append((target_subject.n3(), target_property.n3(), target_object.n3()))
                    print("  The object property {0} is NOT coherent as the range {1} is not IRI".
                          format(target_property.n3(), target_object.n3()))
            # If the target property is data property:
            elif property_type.n3() == "<http://www.w3.org/2002/07/owl#DatatypeProperty>":
                # If the target object of the target property is literal
                if isinstance(target_object, Literal):
                    # The target triple is coherent.
                    pass
                else:
                    # Else the target triple is not coherent, and store the triple
                    incoherent_triple_list.append((target_subject.n3(), target_property.n3(), target_object.n3()))
                    print("  The data property {0} is NOT coherent as the range {1} is not literal".
                          format(target_property.n3(), target_object.n3()))
            else:
                pass

    return incoherent_triple_list
