# Projet RIW

This repository hosts a student project about information retrieval.

## Language and packages used

This project uses Python 3.5.2 with the NLTK library.

## How to use

You need to have Python 3 with NLTK installed. To use the project on CS276, please fill `CS276/` directory by unzipping CS276 archive in it.
CS276 files have not been included on the Github repository because of their size.

First, it is strongly recommended to build indexes and vocabulary files in the `static/` directory by running `performance_tests_<collection>.py` and following instructions.
This will allow quicker start when using search models (especially when working on CS276).
If not found, the program will rebuild the required index and store it in memory.

You may now start using boolean and vector search models (see below).

## Boolean search

### How to run

To run a boolean search, run the file `boolean_search_cacm.py` or `boolean_search_cs276.py` depending on the collection you want to search.

Your query must then comply with a few rules:
- You may use any boolean operator among AND, OR, NOT
    - AND must be preceded *and* followed by a keyword (eg harvard AND computer), it will return the intersection
    - OR must be preceded *and* followed by a keyword (eg harvard OR computer), it will return the union
    - NOT may either be used at the beginning of a query (eg NOT computer) or later on by using parenthesis (eg harvard AND (NOT computer))
- You may use parenthesis in your query. Use it to avoid flawed queries that make no logical sense (see the table below)
- Be careful to avoid mistakes while typing keywords since there is no correction on them. Uppercase or lowercase is equivalent
- Avoid redundant paranthesis, they may cause abnormal results

Here are a few request that won't work and how you should correct them:

Don't | Why | Do
--- | --- | ---
harvard AND NOT computer | Parenthesis are required | harvard AND (NOT computer)
harvard AND computer OR program | Ambiguous / makes no logical sense | harvard AND (computer OR program) (depending on what you mean)
physics OR (harvard AND (computer) OR program) | Parenthesis are no placed properly | physics OR (harvard AND (computer OR program))
physics OR (harvard AND (computer OR program) | Missing parenthesis | physics OR (harvard AND (computer OR program))
(physics OR (harvard AND computer)) | Redundant parenthesis | physics OR (harvard AND computer)

### Principles

Boolean search program means either a document is relevant or it isn't. 
Only documents matching the boolean query will be returned.
Documents are not ordered by relevance since they are all deemed equally relevant.

## Vector search

### How to run

To run a vector search, run the `vector_search_cacm.py` or `vector_search_cs276` depending on the collection you want to search.

You query must then comply with a few rules:
- You should separate your keywords using spaces ` ` or commas `,` 
- Be careful not to use other kind of punctuation or you may have flawed results

### Principles

Vector search means each document's similarity with the query is calculated.
Documents are then returned ordered by decreasing similarity (documents closer to the query will be higher in the list).
