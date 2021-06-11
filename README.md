
# Machine Learning for Behavioural Data Project



## Abstract

In this paper, we analyze a music dataset collected on the Last.fm platform to find some similarities between users and artists. We propose different embeddings techniques to transform the users and artists into vectors. Then we apply several clustering algorithms to group the users and artists by similarity. Finally, we introduce different methods to find an optimal list of artists, i.e., a playlist, for a group of arbitrary users.

## Setup

Here are the different packages needed to reproduce our experiments:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
- `sklearn`
- `fbpca`
- `hdbscan`
- `gensim`

To obtain the results and reproduce our experiment:
Run all the cells of the following notebooks in order:

1) `./notebooks/data_exploration.ipynb`
2) `./notebooks/get_plays_matrix.ipynb`
3) `./notebooks/get_embeddings.ipynb`
4) `./notebooks/dim_reduction.ipynb`
5) `./notebooks/word2vect_embeddings.ipynb`
6) `./notebooks/embedding_evaluation.ipynb`
7) `./notebooks/clustering_analysis.ipynb`
8) `./notebooks/predict_list_of_artists.ipynb`

## Directory structure

The following directory contrains different text documents, code and data files. The structure is detailed below:

#### Documents:

report.pdf

#### Code:

##### Python files:

- `./notebook/helper_clustering.py`: contains the functions to performs K-Means clustering
- `./notebook/helpers.py`: contains utils function that are used through the project

##### Jupyter Notebooks:

- `./notebooks/data_exploration.ipynb`: notebook containing the explanatory data exploration of the Last.fm datasets
- `./notebooks/get_plays_matrix.ipynb`: notebook containing the steps to compute the matrix of plays for the users with the corresponding artists
- `./notebooks/get_embeddings.ipynb`: notebook containing the processing steps on the matrix of plays to get the artist-level and user-level embeddings
- `./notebooks/dim_reduction.ipynb`: notebook containing the steps to perform a dimensionality reduction on the artist and user embeddings
- `./notebooks/word2vect_embeddings.ipynb`: notebook containing the alternative approach of computing the embeddings at the user and artist level
- `./notebooks/embedding_evaluation.ipynb`: notebook containing the evaluation methods for all the embeddings
- `./notebooks/clustering_analysis.ipynb`: notebook containing the clusterings methods performed on the embeddings,
- `./notebooks/predict_list_of_artists.ipynb`: notebook containing the methods used for predicting the optimal list of artists given a list of users. 



## Authors


Lam Olivier [@olivierlam97](https://github.com/olivierlam97)\
Jouven Stanislas [@stanjouven](https://github.com/stanjouven)\
Zbinden Robin [@zbirobin](https://github.com/zbirobin)
