<!DOCTYPE html>
<html>
<head>
  <title>Add page</title>
  <link href="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/css/bootstrap.min.css')}" rel="stylesheet">
  <link href="${request.static_url('pyramidlogin:static/bootstrap-3.3.5-dist/css/bootstrap-theme.min.css')}" rel="stylesheet">
</head>
<body role="document">
  <div class="container theme-showcase" role="main"> 
    <div class="page-header">
        <h1>New Page</h1>
    </div>   
    <div>
        <form action="${save_url}" method="post">
          <input type="text" name="pagename" placeholder="title" class="form-control" /> <br/>           
          <textarea name="body" rows="10" cols="50" placeholder="text"  class="form-control" >${page.data}</textarea>
          <button type="submit" name="form.submitted" value="Save" class="btn btn-default">Save</button>
        </form>
    </div>
    <br/>
    <ul class="nav nav-pills" role="tablist">
        <li role="presentation" class="active"><a href="${request.application_url}">TopPage</a></li>
        <li role="presentation"><a href="${request.application_url}/logout">Logout</a></li>
    </ul>
    <br/>
    <div id="footer">
      <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
  </div>
</body>
</html>
