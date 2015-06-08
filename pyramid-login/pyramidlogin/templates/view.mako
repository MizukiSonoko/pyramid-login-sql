<!DOCTYPE html>
<html>
<head>
    <title>${page.name}</title>
</head>
<body>
    <h1><b>${page.name}</b></h1>
    <a href="${request.application_url}">TopPage</a>
    <hr>
    <p>${page.data}</p>
    <hr>
    <p><a href="${edit_url}">Edit</a>  by ${page.author}.</p>
    <hr>
    % if logged_in:
        <p>you are ${logged_in}. 
        <a href="${request.application_url}/logout">Logout</a>
    % endif
    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>   
    </div>
</body>
</html>
