from api42lib import IntraAPIClient

# point to your config file
ic = IntraAPIClient(config_path="./config.yml")

# Custom call – passing endpoint path *without* scheme/domain
me = ic.get("/me")  # NOT "/v2/me" or full URL
print(me.json())
