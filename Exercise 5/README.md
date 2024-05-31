# Exercise 5: Setting Up a Simple HTTP Server
This exercise demonstrates setting up a basic HTTP server in Python using the **http.server** 
and **socketserver** modules. The code extends the SimpleHTTPRequestHandler class to handle GET requests dynamically.
When a request is made for the path **"/testseite.html"**,
the server responds with a custom HTML page containing details of the requested path.
Otherwise, it delegates the request handling to the parent class.
The server is configured to run on port 8000 and continuously serves incoming requests.
Additionally, it includes the configuration to allow the reuse of the server's address.

#### NOTE: This exercise is designed to provide hands-on experience with server-side programming and HTTP request handling in Python. While it may not pose challenges for myself since i am already familiar with networking and backend APIs like FastAPI, it serves as a foundational exercise for understanding basic server setup and request handling processes.   