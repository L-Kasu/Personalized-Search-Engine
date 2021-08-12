# Personalized-Search-Engine

## Overview


### The UI
Start the engine by running the PersonalizedSearchEngine.exe in the program folder.

Located directly below the 'Settings' button is an entry field where you can enter a query. If you started the engine for the first time, you also need to select a directory (indicated also by the 'no directory selected!' message in the 'Search result' box). By pressing the 'Select Directory' button directly below the entry field a new window will open where you can select the directory in which you wish to search for documents (the engine is capable of searching in .txt and .pdf documents in the selectecd folder only, not it's subfolders!). 

If you selected a directory and did not close the window without doing so, the message 'preprocessing in progress...' will appear in the engine terminal (the space between the 'Select Directory', 'Search' and 'Clear' buttons and the 'Search result' box), after a short period of apparent inactivity followed by 'preprocessing successful' and something like 'reading in files took: 29.3087803444456879 for 456 pages'. 

You can now enter a query and press search to get a list of matching documents in the 'Search result' box with the best match on top of the list, the second best below that and so forth. The path above the list of documents in the 'Search result' box is the directory you selected. The 'Clear' button deletes all documents in the result list and everything in the entry field.

#### UI Terminal
The UI terminal displays informative messages about the search process.

#### Keyboard Shortcuts
- Ctrl-r: reset every setting to it's default state
- Ctrl-p: show/hide a preview of the selected document
- Ctrl-t: show/hide tooltips
- Enter: has the same effect as pressing the 'Search' button

#### Settings
- **Stemmer**: Changes the Stemmer that is used by the engine
- **Stop Word Removal**: Toggles Stop Word Removal
- **Search Mode**: Changes the search method that is used by the engine (descriptions of the different methods below)
- **Clustering**: Toggles Clustering (description below)
- **Language**: Changes the language of the engine.
- **Theme**: Changes the theme (colors and font) of the UI.
- **Font**: Changes the font used within the UI.
- **Language (Snowball Stemmer)**: Sets the language for the Snowball Stemmer. Use this if you want to match you query to documents that are not written in english.
- **Language (Stop Words)**: Sets the language for the Stop Word Removal. Use this if you want to match you query to documents that are not written in english.
- **Number of documents**: Changes the number of documents that are displayed in the 'Search result' box.


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


### Search Algorithms
When searching each page of a document is viewed as an own document. This enables the search to pinpoint a pache for a search. In the following description document referes to the pages.

#### Term-frequency-inverse-document-frequency-weighting (tf-idf)
(https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
When using this search method, first the count of each word in document is determined. For each word in each document this count is then divided by the logarithem of the count of the word in all documents. The implementation uses the scikit library (https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
In our implementation the cosine similarity between all documents and the query is computed, then the documents are sorted by most similar to least similar.

#### Word-embedding
A very simple algorithem using word embeddings (https://en.wikipedia.org/wiki/Word_embedding) is implemmented. It takes the mean vector over all word vectors for each document, therby generating one vector representing the document. By the same process a vector representing the query is generated. The cosine similarity between the query vector and the document voctors is then computed, then the documents are sorted by most similar to least similar.

One embedding we use is GloVe (https://nlp.stanford.edu/projects/glove/).

The other one is fastText (https://fasttext.cc/docs/en/english-vectors.html).

#### Clustering

Via the [k-means clustering algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
(Constructor: clustering.Clustering (doc_vector-matrix: 2d-Array/csr-matrix)).
The Clustering object gets created as follows:
Clustering the documents into Clusters by their cosine-similarity, to greatly speed up the searching process. The optimal number of Clusters for a given directory gets evaluated via the elbow-method and applied (method: find_optimal_k (max: int)). Gets applied in the Constructor automatically. Then the cluster gets predicted
(method: predict_the_cluster_of_vector(vec: 1D-Array). After given the index of a predicted cluster, the actual Cluster gets returned. Then the usual search-procedure is now used but only on the predicted Cluster, which should give a speedup by the factor k.
It is very important to normalize the vectors before Clustering them. Only that way useful results will apper.

#### Machine-Learning (Logistic-Regression)
Machine learning model to predict the similarity of two documents. Here the [Logistic-Regression Algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) is used. Firstgets train by a test dataset of documents, (which can be either realted or unrelated (given by a dictionary = {doc_id: list-of-related-document ids}.
TODO: finish


## Distribution
[Search Engine](https://karylreyne.itch.io/personalized-search-engine)  
[Source code](https://github.com/L-Kasu/Personalized-Search-Engine)


## License

This release of the Personalized Search Engine as a whole will be licensed under the GPL-3.0 license. A copy of this license can be found [here](https://github.com/L-Kasu/Personalized-Search-Engine/blob/main/LICENSE.md).



## Support

This release comes without any support, warranty or guarantee that your PC won't be set on fire. However, if you have any questions open an issue here on GitHub.



## Credits

#### Production
Niklas Munkes

#### UI Programming/Design
Niklas Munkes  
Haitham Samaan

#### Evaluation
Hannah Kessel  

#### Search-algorithms
Lars Kasüschke  
Julian Döhl

#### Icon
Julian Döhl

#### Special Thanks
Hassan Shahmohammadi
