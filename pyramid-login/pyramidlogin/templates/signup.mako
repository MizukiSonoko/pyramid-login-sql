<!DOCTYPE HTML>
<html>
<head>
    <title>Sign up</title>
</head>
<body>
    <b>Signup</b>
    % if message:
        <p>${message}</p>
    % endif
    <form  method="post">
        <p> Name <input type="text" name="name" value="${name}" placeholder="name"/></p>
        <p> Password <input type="password" name="password" placeholder="password"/></p>
        <p> Re password <input type="password" name="repassword" placeholder="re password"/></p>
        <input type="submit" name="form.submitted" value="Sign up"/>
    </form>
    <div id="footer">
        <div class="footer">&copy; Copyright 2015, Sonoko Mizuki.</div>
    </div>
</body>
