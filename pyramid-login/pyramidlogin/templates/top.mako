<html>
<head>
    <title>Top Page</title>
</head>
<body>
    <div>
    <h1> Top Page.</h1> 
    % if user:  
        <p> You are ${user.name} <a href="/logout">logout</a></p>    
        % if user.group == 'admin':
            <p><a href="/admin">Admin</a></p>    
        % endif
    % else:
        <p><a href="/signup">sign up</a> <a href="/login">login</a></p>
    % endif 
    <hr>
    % for page in pages:
        ${content(page)}
    % endfor
    </div>
    
    <%def name="content(page)">
        <div>
            <h2><a href="/view/${page.name}">${page.name}</a></h2>
            <p>${page.data}</p>
            <p> by ${page.author} </p>
            <hr>
        </div>
    </%def>
    <form  method="post">
        <button type="submit" name="newpage" value="newpage">Add Page</button>
    </form>
    <div>
        <div class="footer"> &copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
</body>
</html>
