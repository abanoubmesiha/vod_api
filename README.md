# Welcome to 24/7 TV!

Users are able to use the admin panel to post movies and series with descriptions, and add the relative genres.

The project was built using **Django** as a backend framework and **Next.js** as a frontend framework. All generated information are saved in database (SQLite by default).

All webpages of the project are mobile-responsive.

# Installation

-  Install project dependencies by running  `pip install -r requirements.txt`. 
-   Make and apply migrations by running  `python manage.py makemigrations`  and  `python manage.py migrate`.
-   Create superuser with  `python manage.py createsuperuser`. This step is optional.
-   Navigate to the `frontend` folder and run `npm i` to install the required dependencies for the frontend react library

# How to Run Locally

-  To run the APIs, navigtate to the main directory then:
    - activate the virtual env using `./venv/Scripts/activate` command.
    - `py manage.py runserver`
-  To run on cloud `49....` server, run `source virtual_env/bin/activate`

# Files and directories

-   main application directory.
- `core` contains the models, apis and tests of the backend app.
-   `media`  - this directory contains two folders (`movies`  and  `series`), and here will be saved all photos.
- `vod` contains and settings and urls of the diango app.

# Distinctiveness and Complexity

- New project idea: Netflix clone.
- Models Relations Complexity:
    - `Series` model is linked to itself using the `seasons` property and linked to one-to-many relationship with `Episode` model.
    - `Section` model is related to `Movie` and `Series` models in many-to-many relationships.
    - `Actor` and `Director` models are instances of `Artist` model.
    - `Comments` model have relations with three other models, `Movie`, `Series` and `User`.

# What to be added in the future

- Video Streaming CDN: having an acount and upload movies and series to a streaming service provider and add the links of the videos to the movies and episode to be played in the front end application.
- Comments: replying to comments, liking and disliking, and sharing the comments.
- Search: user should be able to search for movies, series, and episodes in the app using the search bar.
- AI: the app should analyze the user preferance and show the genres he likes more frequently.
- Most viewed movies and series section.
- Pricing Plan: which limit the user from watching specific high rated movies and series.

# Producation (Cloud) Related Commands

- gunicorn_config.py: 
  ```
   command = '/home/247tvco/vod_api/virtual_env/bin/gunicorn'  
   pythonpath = '/home/247tvco/vod_api'  
   bind = '127.0.0.1:7001'  
   workers = 3
   ```
- Run gunicorn in the background:
  ```
  gunicorn -c /home/247tvco/vod_api/gunicorn_config/gunicorn_config.py vod.wsgi
  ```
    
  after that `ctl + z` then type `bg` and enter 

- vod_api.conf:
  ```
    server {
        listen 7000;
        server_name 127.0.0.1:7000;
        location /static/ {
                alias /home/247tvco/vod_api/static/;
        }
        location /media/ {
                alias /home/247tvco/vod_api/media/;
        }
        location / {
                proxy_pass http://127.0.01:7001;
        }
    }
  ```

- Run virutal env: `source virtual_env/bin/activate`
- Make Migrations: `python3 manage.py makemigrations`
- Kill Gunicorn: `pkill gunicorn`
- Find services by port: `sudo netstat -nlp | grep :7001`