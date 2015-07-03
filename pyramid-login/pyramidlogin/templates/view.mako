<!DOCTYPE html>
<html>
<head>
    <title>${page.name}</title>
    <link href="/static/bootstrap-3.3.5-dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/statica/bootstrap-3.3.5-dist/css/bootstrap-theme.min.css" rel="stylesheet">
</head>
<body role="document">
  <div class="container theme-showcase" role="main"> 
    <div class="page-header">
        <h1>${page.name}</h1>
    </div>   
    <p>${page.data}</p>
    <hr>
    <p> by ${page.author}.</p>
    % if logged_in and logged_in == page.author:
        <p><a href="${edit_url}">Edit</a>
    % endif
    <hr>
    <br/>
    <ul class="nav nav-pills" role="tablist">
        <li role="presentation" class="active"><a href="/">TopPage</a></li>
        % if logged_in:
            <li role="presentation"><a href="/logout">Logout</a></li>
        % endif
    </ul>
    <br/>
    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
  </div>
</body>
</html>

