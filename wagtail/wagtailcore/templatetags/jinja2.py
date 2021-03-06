from __future__ import absolute_import

try:
    import jinja2
    from jinja2.ext import Extension
except:
    Extension = object

from .wagtailcore_tags import pageurl, richtext, slugurl, wagtail_version


class WagtailCoreExtension(Extension):
    def __init__(self, environment):
        super(WagtailCoreExtension, self).__init__(environment)

        self.environment.globals.update({
            'pageurl': jinja2.contextfunction(pageurl),
            'slugurl': jinja2.contextfunction(slugurl),
            'wagtail_version': wagtail_version,
        })
        self.environment.filters.update({
            'richtext': richtext,
        })


# Nicer import names
core = WagtailCoreExtension
