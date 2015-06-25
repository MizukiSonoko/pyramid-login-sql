<!DOCTYPE html>
<html>
<head>
    <title>Login</title>

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
        <div class="page-header">
            <h1><b>Login</b></h1>
        </div>   

        % if message:
            <div class="alert alert-danger" role="alert">
                <strong>Message!</strong> ${message}
            </div>
        % endif

        <form action="${url}" method="post">
            <input type="hidden" name="came_from" value="${came_from}"/>
            <div class="form-group">            
                <label for="login">Login name</label>
                <input type="text" name="login" value="${login}" class="form-control" />
            </div>
            <div class="form-group">            
                <label for="name">Password</label>
                <input type="password" name="password" value="${password}" class="form-control" />
            </div>
            <input type="submit" name="form.submitted" value="Log In" class="btn btn-default"/>
        </form>
        <br/>
        <ul class="nav nav-pills" role="tablist">
            <li role="presentation" class="active"><a href="${request.application_url}">TopPage</a></li>
        </ul>
        <br/>
        <div id="footer">
            <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/js/bootstrap.min.js')}"></script>
    </div>
</body>
</html>

