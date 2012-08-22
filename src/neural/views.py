from django.views.generic.detail import BaseDetailView
from django.views.generic.base import TemplateResponseMixin
#from django.http import Http404
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from tartarus.django.resources import BaseModelResource, ResourceView as View
from .models import Node


class NodeView(TemplateResponseMixin, BaseDetailView):
    template_name = 'main.html'

class Main(BaseModelResource):
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
            if self.object.is_root and not kwargs.has_key('root'):
                return redirect(self.object)
            parent_pk = kwargs.get('parent_pk', None)
            if parent_pk is not None:
                try:
                    self.object.parent = self.object.parents.get(pk=parent_pk)
                except ObjectDoesNotExist:
                    return redirect(self.object)
            return response

    class Create(View):
        pass

    class Search(View):
        pass