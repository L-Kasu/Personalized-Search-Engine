# Personalized-Search-Engine
## Overview
### The UI
To start the search engine run the [executable file](https://github.com/L-Kasu/Personalized-Search-Engine/blob/main/executable.py).  
In the UI you can choose a file you want to search in. 
You can choose between several color schemes and languages.  
The System searches in txt- and PDF-documents.  

### The search engine  
You have the choice between different searching alorithms:
- tf-idf
- word embedding  

For every searching algortihm you can used it with or without clustering.  

### The evaluation
For the Evaluation the [CISI dataset from kaggle](https://www.kaggle.com/dmaso01dsta/cisi-a-dataset-for-information-retrieval) is used. 

The evaluation is executed in the [main file](https://github.com/L-Kasu/Personalized-Search-Engine/blob/main/main.py). You will be gudided through the Evaluation in the Terminal. You can evaluate the algorithms and compare all algorithms. 
#### Evaluate the algorithms
You can evaluate the algorithms using tf-idf, word-embedding or logistic regression. The algorithms using tf-idf and word-embedding can be evaluated with or without clustering. The algorithm using logistic regression only works without clustering.  
There is also the option to evaluate the algorithms using all the queries or just the first 30 ones, because the logistic regression is also trained in the dataset. So the first 30 queries are used to evaluate the algorithm and the rest is used for train and validation.  
The results of the evaluation can be found in the directiory [eval_output](https://github.com/L-Kasu/Personalized-Search-Engine/tree/main/eval_output).  
The metrics used are mean-average-precission and F1-score. The metrics are computed for every query and the average over all queries.  
#### Compare the algorithms
To compare the algorithms a evaluation for all of them has to be in the pickle-database.  
The average over all queries of all algorithms will be printed in one document, to show a overview of how good the results in comparson are.  


### Credits

#### UI Programming/Design
Niklas Munkes


## License
pending
(GNU LGPL under consideration, but not applied yet)
