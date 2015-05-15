=====
Tagger
=====

Tagger is a simple Django app to tag content. 

Detailed documentation will be available in the "docs" directory.

Quick start
-----------

1. Add "tagger" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'tagger',
    )

2. Include the tagger URLconf in your project urls.py like this::

    url(r'^tagger/', include('tagger.urls', namespace='tagger')),

3. Run `python manage.py migrate` to create the tagger models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create some tags (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/tagger/tag-cloud to view the results. 
