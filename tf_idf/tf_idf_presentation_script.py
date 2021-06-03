# tf-idf script for scrum presentation
# author: Niklas Munkes

import tf_idf.tf_idf_main as main


doc_dicts = [
    {"I" : 0,
     "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
     'libraries', 'evaluations', 'make', 'show', 'book', 'case', 'university', 'ellsworth', 'present', 'representative',
     'attempt', 'important', 'architectural', 'unsuccessful', 'yale', 'college', 'architects', 'done', 'study',
     'except', 'mistakes', 'cases', 'attempts', 'existing', 'brown', 'examples', 'library', 'solutions', 'buildings',
     'enlarging', 'planning'}},
    {"I" : 1,
     "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
     'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
]

qry_dicts = [
    {"I" : 0,
     "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
     'libraries', 'evaluations', 'make', 'show', 'book', 'case', 'university', 'ellsworth', 'present', 'representative',
     'attempt', 'important', 'architectural', 'unsuccessful', 'yale', 'college', 'architects', 'done', 'study',
     'except', 'mistakes', 'cases', 'attempts', 'existing', 'brown', 'examples', 'library', 'solutions', 'buildings',
     'enlarging', 'planning'}},
    {"I" : 1,
     "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
     'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
    {"I" : 1,
         "W" : {'librarians', 'successful', 'avoid', 'new', 'identified', 'problems', 'structures', 'face', 'mason', 'remodeling',
         'libraries', 'evaluations', 'make', 'show'}}
]


main.main(doc_dicts, qry_dicts)