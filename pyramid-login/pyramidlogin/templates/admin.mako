<html>
<head>
    <title>Top Page</title>
</head>
<body>
    <div>
    <h1> Admin Page.</h1> 
    <p><a href="/">Top Page</a> <a href="/logout">logout</a></p>    
    <hr>
    % for user in users:
        % if user.name != logged_in:
            ${content(user)}
        % endif
    % endfor
    </div>
    
    <%def name="content(user)">
        <div>
            <p>${user.name}</p>
            <form  method="post">
                <button type="submit" name="deluser" value="">Delete</button>
            </form>
            <hr>
        </div>
    </%def>
    <div>
        <div class="footer"> &copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
</body>
</html>
