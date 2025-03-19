# practice 2/21/25
# chapter 9
# imported_admin_9_11.py
import priv_admin as pa

super_user = pa.Admin("foo", "bar", "foo@bar.net", "supafoo", "5/15/1990")
logins = super_user.login_attempts
print(logins)
super_user.permissions.show_privileges()