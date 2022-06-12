run:
	docker run -d -p 80:8000 -v vol:/app/db.sqlite3 --rm --name trendingit kirill0720/trendingit:volumes
stop:
	docker stop trendingit