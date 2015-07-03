<!DOCTYPE html>
<html>
<head>
  <title>Add page</title>
</head>
<body>
    <a href="/">TopPage</a>
    <div>
      <form action="${save_url}" method="post">
        <textarea name="pagename" rows="1" cols="50" placeholder="title" >${page.name}</textarea><br/>
        <textarea name="body" rows="10" cols="50" placeholder="text" >${page.data}</textarea>
        <button type="submit" name="form.submitted" value="Save">Save</button>
      </form>
      <a href="/logout">Logout</a>
    </div>
  </div>
  <div id="footer">
    <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
  </div>
</body>
</html>
