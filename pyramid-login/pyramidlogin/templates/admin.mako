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
        ${content(user)}
    % endfor
    </div>
    
    <%def name="content(user)">
        <div>
            % if user.group != "admin":
                <p>${user.name}</p>
                    <form  method="post">
                    <button type="submit" name="deluser" value="${user.name}">Delete</button>
                </form>
                <hr>
            % endif
        </div>
    </%def>
    <div>
        <div class="footer"> &copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
</body>
</html>
