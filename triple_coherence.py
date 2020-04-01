from query import construct_sparql, generate_query_string
import configuration as config
from rdflib.term import Literal, URIRef


def run_triple_coherence_validation(triple):

    # Assign RDF terms
    target_subject = triple[0]
    target_property = triple[1]
    target_object = triple[2]

    incoherent_triple_list = []

    if target_property.n3() != "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>":
        p_sparql_results = construct_sparql(config.sparql_service,
                                            generate_query_string(query_type="get_type", iri=target_property.n3()))

        for _, _, property_type in p_sparql_results:
            if property_type.n3() == "<http://www.w3.org/2002/07/owl#ObjectProperty>":
                if isinstance(target_object, URIRef):
                    pass
                else:
                    incoherent_triple_list.append((target_subject.n3(), target_property.n3(), target_object.n3()))
                    print("  The object property {0} is NOT coherent as the range {1} is not IRI".
                          format(target_property.n3(), target_object.n3()))
            elif property_type.n3() == "<http://www.w3.org/2002/07/owl#DatatypeProperty>":
                if isinstance(target_object, Literal):
                    pass
                else:
                    incoherent_triple_list.append((target_subject.n3(), target_property.n3(), target_object.n3()))
                    print("  The data property {0} is NOT coherent as the range {1} is not literal".
                          format(target_property.n3(), target_object.n3()))
            else:
                pass

    return incoherent_triple_list


