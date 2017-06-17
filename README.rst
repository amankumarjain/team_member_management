=====
Members
=====

Members is a simple Django app to make crud operation using apis

Quick start for adding app to existing django project
-----------
1. curl -O https://github.com/amankumarjain/team_member_management/blob/development/members-0.1.tar.gz

2. pip install members-0.1.tar.gz

3. Change your INSTALLED_APPS settings file

    INSTALLED_APPS = [
        ...
        'members',
    ]

4. Include the members URLconf in your project urls.py like this::

    from members.urls import routers as member_routers
    url("^api/v1/", include(member_routers.urls)),

Installing and setup project from scratch in isolated evv(virtualenv)
----------
1. Install and create virtual env like this::

    ```
    sudo apt-get install python3-pip
    pip3 install virtualenv
    virtualenv {project_name}
    ```

2. Activate virtual env like this::

    ```
    source {path/to/virtualenv}/bin/activate
    ```

3. Clone repository::

    ```
    git clone https://github.com/amankumarjain/team_member_management.git
    ```

3. Inside virtualenv run *pip install -r requirements.txt* to download all related packages.

4. Run ./manage.py runserver 0.0.0.0:8080 in development server

Detailed documentation is in the "docs" directory.
----------
*https://www.codersbyte.xyz/docs/*

Running or Testing on Live Running Projects
-----------
**This will create a new member instance**
```
curl -X POST \
"https://www.codersbyte.xyz/api/v1/members/" \
-H 'content-type: application/json' \
-d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
```

**Return a list of all the existing members**
```
curl -X GET \
https://www.codersbyte.xyz/api/v1/members/ \
-H 'content-type: application/json' \
```

**Return the given member**
```
curl -X GET \
"https://www.codersbyte.xyz/api/v1/members/31376e06-69a5-47fd-b357-b603cbfb9fba/" \
-H 'content-type: application/json' \
```

**Update the given member**
```
curl -X PUT \
"https://www.codersbyte.xyz/api/v1/members/" \
-H 'content-type: application/json' \
-d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
```

**Update partial field for given member**
>```
curl -X PATCH \
"https://www.codersbyte.xyz/api/v1/members/" \
-H 'content-type: application/json' \
-d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
```
