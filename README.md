# A small demo twisted server

#### Prerequisites
- Install the requirements with
  - pip install -r requirement.txt
- Run the server with
  - python -m main
- The server will start by default on port 8000 and listen on 0.0.0.0
- For the moment, we can change the port the server listens to by changing the value of PORT from the main.py file.

---
#### Endpoints
- Server static files
  - http://localhost:8000/static
- Returns no content with Content-type header as video/mp4
  - http://localhost:8000/video
- Returns content of page.html with Content-type text/html
  - http://localhost:8000/html
- Returns big amount of data in chunks with Content-type application/json
  - http://localhost:8000/stream

---

