# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('rpy',SPAN(2)),
                  _class="brand",_href="https://github.com/ebratt/rpy2_demo")
response.title = request.application.replace('_',' ').title()
response.subtitle = 'demonstrating the power and simplicity of rpy2 with web2py'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Eric Bratt <eric_bratt@yahoo.com>'
response.meta.keywords = 'web2py, python, rpy2, demonstration, demo'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('About'), False, URL('default', 'about'), []),
    (T('Basic'), False, URL('default', 'basic'), [])
]
