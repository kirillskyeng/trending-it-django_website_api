# TrendingIT website on Django with REST API
![trendingit](https://user-images.githubusercontent.com/38908085/170826378-b1b74578-026a-4652-8047-63a5c9473faa.png)

### Django used features:
- class-based views
- mixins
- custom template tags
- admin page

### Django REST Framework used features:
- CRUD with permissions
- session-based authenticaiton
- pagination

### API usage
- [api/v1/itlist/](https://trendingit.pythonanywhere.com/api/v1/itlist/): get posts or post a new one if authenticated
- [api/v1/itlist/2/](https://trendingit.pythonanywhere.com/api/v1/itlist/2/): get specified post and update/delete if it is user's post

### Visit in [here](http://trendingit.pythonanywhere.com/)

### Run with Docker
- assuming you have docker installed
- use `docker push kirill0720/trendingit:volumes` to load image
- use `run -d -p 80:8000 -v vol:/app/db.sqlite3 --rm --name trendingit kirill0720/trendingit:volumes` to run container
- go to *localhost* in your browser and enjoy :slightly_smiling_face:
