# Multiple-level Validation on RDF Graphs

The script aims to validate RDF graphs in three levels:
* Syntax: if an RDF graph can be parsed into RDF triples
* Resolvability: if IRIs used in the graphs can lead to resolved resources
* Coherence: if object property has IRI value, and if data property has literal value

## Getting Started
Two steps need to be performed to validate RDF graphs:
1. Edit `configuration.py`. 
2. Run `run_validation.py`.

### Dependencies
Run the following command to install dependencies with `pip` installed:
 
```
pip install -r requirements.txt
```

### Future Work
In Functionality:  
* Enable validation online RDF graphs
* Enable using different SPARQL endpoints
* Extend corpus of SPARQL query strings
* ... 

In Programming:
* Use more rigorous file path 
* Store identified invalid RDF components 
* ...