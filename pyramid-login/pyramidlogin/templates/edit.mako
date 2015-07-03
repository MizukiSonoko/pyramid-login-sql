<!DOCTYPE html>
<html>
<head>
  <title>${page.name}</title>
</head>
<body>
    <h1>${page.name}</h1>
    <a href="/">TopPage</a>
    <div>
      <form action="${save_url}" method="post">
        <textarea name="body" rows="10" cols="50">${page.data}</textarea>
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
