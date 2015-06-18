<!DOCTYPE html>
<html>
<head>
    <title>${page.name}</title>
</head>
<body>
    <h1><b>${page.name}</b></h1>
    <a href="${domain}">TopPage</a>
    <hr>
    <p>${page.data}</p>
    <hr>
    <p> by ${page.author}.</p>
    % if logged_in and logged_in == page.author:
        <p><a href="${edit_url}">Edit</a>
    % endif
    <hr>
    % if logged_in:
        <p>you are ${logged_in}. 
        <a href="${domain}/logout">Logout</a>
    % endif
    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>   
    </div>
</body>
</html>
