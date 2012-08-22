from django.db import models
from django.db.models import Q


class Node(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    content = models.TextField(blank=True)
    parents = models.ManyToManyField('self', symmetrical=False, related_name='children')
    related = models.ManyToManyField('self')

    ROOT_ID = 0
    @classmethod
    def get_root(cls):
        return Node.objects.get(id=Node.ROOT_ID)

    def __unicode__(self):
        return "#%s %s" % ( self.id, self.title )

    @property
    def is_root(self):
        return self.id is self.ROOT_ID

    @models.permalink
    def get_absolute_url(self):
        args = []
        kwargs = {}
        if not self.is_root:
            kwargs['pk'] = self.id
        return ('node', args, kwargs)


    def save(self):
        if self.is_root:
            self.parents.remove()
        elif self.parents.count() is 0:
            self.parents.add(Node.ROOT_ID)
        super(Node, self).save()
