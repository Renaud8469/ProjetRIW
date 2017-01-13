# Projet RIW

This repository hosts a student project about information research.

## Language and packages used

This project uses Python 3.5.2 with the NLTK library.

## Boolean search

To run a boolean search (for example on CACM), run the file `test_index_bsearch_cacm.py`

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
