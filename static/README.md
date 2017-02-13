# Static files

This directory is meant to host files produced in order to search for documents in collections.

They are not mandatory since they can be built again when launching program but it may be useful to bypass the time required for their construction.

To create those files (not uploaded on Github since they may be heavy), simply run `performance_tests_<collection>.py` and follow the instructions.

Usually, CACM index is expected to be about 0.75Mo (plus 0.215Mo for vocabulary). CS276 index is about 61Mo (plus 5Mo for vocabulary).

## Format

### Index and vocabulary

Those files are dictionaries and are stored using pickle, which is very helpful to store efficiently this kind of data.
As a result, files are named `index_<collection>.p` and `voc_<collection>.p`

### Documents

This file simply lists all documents indexed (useful for instance when treating a NOT boolean request)
As a result, files are named `doc_<collection>.txt`, stored as simple text files