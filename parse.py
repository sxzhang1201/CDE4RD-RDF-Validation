import os.path
from rdflib.graph import Graph


def parse_rdf_raph(file_name, graph_format):


    # Initiate an empty graph
    g = Graph()

    # Check 1) if the file exists and 2) if RDF graphs in that file is parsable
    if os.path.exists(file_name):
        try:
            g.parse(file_name, format=graph_format)
        except:
            raise Exception("The file {} cannot be parsed into RDF triples, please check syntaxes".format(file_name))
    else:
        raise OSError("The file {} is not found".format(file_name))

    print("  Finish Syntactical Validation: RDF graphs are successfully parsed and returned.")

    return g












