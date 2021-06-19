import os

# GOOGLE OAUTH
CERT_STR = b"""-----BEGIN CERTIFICATE-----\nMIIDJjCCAg6gAwIBAgIIVGBFY93ZYokwDQYJKoZIhvcNAQEFBQAwNjE0MDIGA1UE\nAxMrZmVkZXJhdGVkLXNpZ25vbi5zeXN0ZW0uZ3NlcnZpY2VhY2NvdW50LmNvbTAe\nFw0yMTA2MTIwNDI5NTVaFw0yMTA2MjgxNjQ0NTVaMDYxNDAyBgNVBAMTK2ZlZGVy\nYXRlZC1zaWdub24uc3lzdGVtLmdzZXJ2aWNlYWNjb3VudC5jb20wggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRi52e+K7A11wKhcQzAyUlaHFZimYB5FdD\nwN/lsJV/nEVUSYvlqb/ZNNZHBF/fi+om6ganJ/dLvMl4m/wjYvK+anDfctF5ESQ5\nsK3W6nXskbDn930rYx/n0Sec+R3thQaSVTGN7yvEguJOGI90RoXw/mlF575YPaaZ\nBK6DSuo2Uylp1hVoy/dj8cuv3sd6HUAJGh9h+/aGYZKYLqijRI3h3mA/7+CADOD0\nqjssNVwGDpNYB8kuHfcaky0AjYw+N3pcUmO75H13rwgMIhSj4ITwrSkBmdcZLxpa\nWf92mNmGUyNeuBjjbdBrhg2yWg9zCRDbSuTxcZgWvQf/0a5YhpZZAgMBAAGjODA2\nMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/BAQDAgeAMBYGA1UdJQEB/wQMMAoGCCsG\nAQUFBwMCMA0GCSqGSIb3DQEBBQUAA4IBAQCrfG7K0x6L/Y9Sj/Au3GraEX3lPScu\n5AuW7tP26iYMf69n4m8Vi/UtkiHbZJeOWQ0HNgevq50ke8MHXOMBoHMfcjEsPyxu\nfWRtIsqNWnNCWgbfSTIhk/NLHbZKnSbW+qysLcDNMrFc1XEaMR7i0XTQE8tNPfV9\nNJSI+scn6Oq/z6Tjdw+iSbqkw8n8+PfSRl0J8hx6gEQoKFagw1Zt/jAApSW6SWKb\ny4VwFHgTVDbPwdMV4VbseKKx66Lb8qGPqTu8TM70nQlIHUnbXccalXGOaQsycaaN\nWPGpychl1JxUftwbdaW/dY5NVpGEwXJ2DRAJiNK6jDcSsrjOJI4d7ukb\n-----END CERTIFICATE-----\n"""
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

# SPOTIFY
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_USER_URL = "https://api.spotify.com/v1/me"
GRANT_TYPE = "authorization_code"
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
