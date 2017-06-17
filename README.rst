=====
Members
=====

Members is a simple Django app to make crud operation using apis

Detailed documentation is in the "docs" directory.
*https://www.codersbyte.xyz/docs/*

Quick start for adding app to existing django project
-----------
1. curl -O https://github.com/amankumarjain/team_member_management/blob/development/members-0.1.tar.gz

2. pip install members-0.1.tar.gz

3. INSTALLED_APPS = [
        ...
        'members',
    ]

4. Include the members URLconf in your project urls.py like this::

    from members.urls import routers as member_routers
    url("^api/v1/", include(member_routers.urls)),

Installing and setup project from scratc in isolated evv(virtualenv)
----------
1. Install and create virtual env like this::

    ```
    sudo apt-get install python3-pip
    pip3 install virtualenv
    virtualenv {project_name}
    ```

2, Activate virtual env like this::

    ```
    source {path/to/virtualenv}/bin/activate
    ```

3. Clone repository::

    ```
    git clone https://github.com/amankumarjain/team_member_management.git
    ```

3. Inside virtualenv run *pip install -r requirements.txt* to download all related packages.

4. 
