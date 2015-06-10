<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <b>Login</b>
    <p>${message}</p>
    <form action="${url}" method="post">
        <input type="hidden" name="came_from" value="${came_from}"/>
        <p>login name <input type="text" name="login" value="${login}"/></p>
        <p>Password <input type="password" name="password" value="${password}"/></p>
        <input type="submit" name="form.submitted" value="Log In"/>
    </form>

    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
</body>
</html>
