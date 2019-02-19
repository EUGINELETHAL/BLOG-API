# BLOG-API

This is aN API that made with Django Rest Framework that exposes articles and categories for a blog. It has the following functionality:

1. Admin user - create using command line
* log in(Class-based API views)
* create, view, edit, delete article(Viewset Classes)
* create, view, edit, delete category(Viewset Classes)

2. Category - name

3. Article - writer (foreign key), title, content, category (foreign key), image

4. Permissions:
* only admin can create, edit, and delete articles and categories
* no login required for viewing articles
