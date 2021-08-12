# Personalized-Search-Engine
## Overview
### The UI
Start the engine by running the PersonalizedSearchEngine.exe in the program folder.

Located directly below the 'Settings' button is an entry field where you can enter a query. If you started the engine for the first time, you also need to select a directory (indicated also by the 'no directory selected!' message in the 'Search result' box). By pressing the 'Select Directory' button directly below the enry field a new window will open where you can select the directory in which you wish to search for documents (the engine is capable of searching in .txt and .pdf documents in the selectecd folder only, not it's subfolders!). If you selected a directory and did not close the window without doing so, the message 'preprocessing in progress...' will appear in the engine terminal (the space between the 'Select Directory', 'Search' and 'Clear' buttons and the 'Search result' box), after a short period of apparent inactivity followed by 'preprocessing successful' and something like 'reading in files took: 29.3087803444456879 for 456 pages'. You can now enter a query and press search to get a list of matching documents in the 'Search result' box with the best match on top of the list, the second best below that and so forth. The path above the list of documents in the 'Search result' box is the directory you selected. The 'Clear' button deletes all documents in the result list and everything in the entry field.

#### UI Terminal
The UI terminal displays informative messages about the search process.

#### Keyboard Shortcuts
- Ctrl-r: reset every setting to it's default state
- Ctrl-p: show/hide a preview of the selected document
- Ctrl-t: show/hide tooltips
- Enter: has the same effect as pressing the 'Search' button

#### Settings
- *Stemmer*: pending

##### Stop Word Removal
pending

##### Search Mode
pending

##### Clustering
pending

##### Language
Changes the language of the engine.

##### Theme
Changes the theme (colors and font) of the UI.

##### Font
Changes the font used within the UI.

##### Language (Snowball Stemmer)
Sets the language for the Snowball Stemmer. Use this if you want to match you query to documents that are not written in english (the supported languages are Arabic, Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish and Swedish)

##### Language (Stop Words)
Sets the language for the Stop Word Removal. Use this if you want to match you query to documents that are not written in english.

##### Number of documents
Changes the number of documents that are displayed in the 'Search result' box.

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

#### Production
Niklas Munkes

#### UI Programming/Design
Niklas Munkes  
Haitham Samaan

#### Evaluation
Hannah Kessel  

#### Search-algorithms
Lars Kasüschke
