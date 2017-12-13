from itsdangerous import URLSafeTimedSerializer
s = URLSafeTimedSerializer('testing12345')

data = s.loads("<Request 'http://localhost:2000/' [GET]>", max_age=1024)
