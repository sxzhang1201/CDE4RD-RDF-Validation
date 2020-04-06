"""
In this file, key parameters are specified, including:
"file": string, the path of to-be-validated RDF graphs;
"graph_format": string, the format the file;
"sparql_service": string, the Ontobee SPARQL endpoint
"""


# The RDF graphs to be validated
# file = "personInformation.ttl"
file = "patientStatusInstance.ttl"

# The representation format of the file
graph_format = 'turtle'

# The Ontobee SPARQL endpoint
sparql_service = "http://sparql.hegroup.org/sparql/"


