<html>
<head>
    <title>Top Page</title>

    <!-- Bootstrap core CSS -->
    <link href="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/css/bootstrap.min.css')}" rel="stylesheet">

    <!-- Bootstrap theme -->
    <link href="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/css/bootstrap-theme.min.css')}" rel="stylesheet">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>
<body role="document">
  <div class="container theme-showcase" role="main">
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
            <div class="page-header">
                <h1><a href="/view/${page.name}">${page.name}</a></h1>
            </div>   
            <p>${page.data}</p>
            <p> by ${page.author} </p>
            <hr>
        </div>
    </%def>
    <form  method="post">
        <button type="submit" name="newpage" value="newpage" class="btn btn-default">Add Page</button>
    </form>
    <div>
        <div class="footer"> &copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/js/bootstrap.min.js')}"></script>
  </div>
</body>
</html>

