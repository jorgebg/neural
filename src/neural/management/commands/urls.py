from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Shows the url patterns'

    def handle(self, *args, **options):
        urls = __import__(settings.ROOT_URLCONF, {}, {}, [''])
        self.show_urls(urls.urlpatterns)
        
    def show_urls(self, urllist, depth=0):
        for entry in urllist:
            print "  " * depth, entry.regex.pattern, hasattr(entry, 'name') and ' ->  "%s" %s' % ( entry.name or '', entry._callback )
            if hasattr(entry, 'url_patterns'):
                self.show_urls(entry.url_patterns, depth + 1)
