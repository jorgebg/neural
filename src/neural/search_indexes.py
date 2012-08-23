
from haystack import indexes
from .models import Node

class NodeIndex(indexes.SearchIndex, indexes.Indexable): 
    text = indexes.CharField(document=True, use_template=True)
    parents = indexes.CharField()

    def get_model(self): 
        return Node

    def prepare_parents(self, object): 
        return [parent.title for parent in object.parents.all()] 
