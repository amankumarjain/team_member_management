=====
Members
=====

Members is a simple Django app to make crud operation using apis

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "members" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'members',
    ]

2. Include the members URLconf in your project urls.py like this::

    from members.urls import routers as member_routers
    url("^api/v1/", include(member_routers.urls)),

3. Run `python manage.py migrate` to create the members models.

4. Start the development server and visit http://127.0.0.1:8000/api/v1/members/
   to create a member (you'll need the Admin app enabled).
