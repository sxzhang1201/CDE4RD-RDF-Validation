from SPARQLWrapper import SPARQLWrapper


def generate_query_string(query_type, iri=None):
    """
    To generate IRI-dependent SPARQL query string.
    :param query_type: String, indicating which pre-defined query strings to be used. These types are supported:
    "get_all": to construct all triples with the given IRI as the subject;
    "get_type": to construct triples with the given IRI as the subject and the rdf:type as the predicate.
    :param iri: String describing an IRI in n3 format, i.e., "<IRI>".
    :return: A long string to be executed by SPARQL endpoint.
    """
    if iri is None:
        iri = "?s"

    if query_type == "get_all":
        # The query that constructs all triples whose subjects are the given IRI
        query_string = """
        CONSTRUCT {{ {0} ?p ?o }}
        WHERE {{
            {0} ?p ?o.
        }}
        """.format(iri)

    elif query_type == "get_type":
        query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        CONSTRUCT {{ {0} rdf:type ?o}}
        WHERE {{
            {0} rdf:type ?o.
        }}
        """.format(iri)

    else:
        query_string = None

    return query_string


def construct_sparql(sparql_service, query_string):
    """
    To obtain queried triples by running SPARQL
    :param sparql_service: String, indicating which SPARQL endpoint is used to implement SPARQL.
    :param query_string: A long string to be executed by SPARQL endpoint.
    :return: An rdflib "QueryResult" object that containing queried triples
    """

    # Initiate SPARQL Wrapper class and implement querying
    sparql = SPARQLWrapper(sparql_service)
    sparql.setQuery(query_string)

    # Get SPARQL results, and construct them in RDF format
    sparql_results = sparql.query().convert()

    return sparql_results






