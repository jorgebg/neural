from django.views.generic.detail import BaseDetailView
from django.views.generic.base import TemplateResponseMixin
#from django.http import Http404
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from tartarus.django.resources import BaseModelResource, ResourceView as View
from .models import Node


class NodeView(TemplateResponseMixin, BaseDetailView):
    template_name = 'main.html'

class Node(BaseModelResource):
    name = 'node'
    model = Node
    pattern = '^'

    class Default(NodeView):
        patterns = (
            ('^$', { 'pk': Node.ROOT_ID, 'root': True }),
            '^(?P<pk>\d+)$',
            '^(?P<parent_pk>\d+)/(?P<pk>\d+)$',
        )
        def get(self, request, *args, **kwargs):
            response = super(NodeView, self).get(request, *args, **kwargs)
            object = self.object
            if object.is_root and not kwargs.has_key('root'):
                return redirect(object)
            parent_pk = kwargs.get('parent_pk', None)
            if parent_pk is not None:
                try:
                    object.parent = object.parents.get(pk=parent_pk)
                except ObjectDoesNotExist:
                    return redirect(object)
            if not hasattr(object, 'parent') and object.parents.count() is 1:
                object.parent = object.parents.all()[0]
            return response

    class Search(View):
        pass

    class Create(View):
        pass

    class Update(NodeView):
        pass

    class Delete(NodeView):
        pass


class Relation(BaseModelResource):
    name = 'relation'
    model = Node
    default = 'add'

    class Add(NodeView):
        pattern = '^(?P<pk>\d+)$'

    class Create(View):
        pattern =  '^(?P<type>parent|child|related)/(?P<related_pk>\d+)/(?P<pk>\d+)$'

    class Delete(View):
        pattern =  '^delete/(?P<type>parent|child|related)/(?P<related_pk>\d+)/(?P<pk>\d+)$'