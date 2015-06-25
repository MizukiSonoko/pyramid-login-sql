<!DOCTYPE html>
<html>
<head>
    <title>${page.name}</title>

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
        <h1>${page.name}</h1>
    </div>   
    <div>
        <form action="${save_url}" method="post">
          <textarea name="body" rows="10" cols="50" class="form-control" >${page.data}</textarea>
          <button type="submit" name="form.submitted" value="Save" class="btn btn-default">Save</button>
        </form>
        <div class="page-header">
          <h1>Menu</h1>
        </div> 
        <ul class="nav nav-pills" role="tablist">
            <li role="presentation" class="active"><a href="${request.application_url}">TopPage</a></li>
            <li role="presentation"><a href="${request.application_url}/logout">Logout</a></li>
        </ul>
    </div>
    <br/>
    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
        </div>
    </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/js/bootstrap.min.js')}"></script>
</body>
</html>

