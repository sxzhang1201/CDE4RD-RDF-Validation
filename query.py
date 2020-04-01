from SPARQLWrapper import SPARQLWrapper


def generate_query_string(query_type, iri=None):
    if query_type == "get_all":
        # The query that constructs all triples whose subjects are the given IRI
        query_string = """
        CONSTRUCT {{ {0} ?p ?o }}
        WHERE {{
            {0} ?p ?o.
        }}
        """.format(iri)

    if query_type == "get_type":
        query_string = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        CONSTRUCT {{ {0} rdf:type ?o}}
        WHERE {{
            {0} rdf:type ?o.
        }}
        """.format(iri)

    return query_string


def construct_sparql(sparql_service, query_string):

    # Initiate SPARQL Wrapper class and implement querying
    sparql = SPARQLWrapper(sparql_service)
    sparql.setQuery(query_string)

    # Get SPARQL results, and construct them in RDF format
    sparql_results = sparql.query().convert()

    return sparql_results






