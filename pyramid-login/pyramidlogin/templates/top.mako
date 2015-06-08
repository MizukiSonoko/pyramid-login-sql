<html>
<head>
    <title>Top Page</title>
</head>
<body>
    <div>
    <h1> Top Page.</h1>    
    <hr>
    % for page in pages:
        ${content(page)}
    % endfor
    </div>
    
    <%def name="content(page)">
        <div>
            <h2><a href="/view/${page.name}">${page.name}</a></h2>
            <p>${page.data}</p>
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
