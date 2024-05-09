# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://inmanage.atlassian.net/rest/api/3/issue/{issueIdOrKey}"

auth = HTTPBasicAuth("omerb@inmanage.co.il", "ATATT3xFfGF0ABkQGOYXhTHpyeiKDVyC1YnJI2K3YYa5juGACr0zfw21W1bI1crXilFXw0wEzfOxBBahoCBRxx9TdshnpHoVHvGTy8qdpuGrTL-YyR2NIf4mLqD9s2ASmgDumeJnhSPd33SH9GPNX4cXihmaSWb_3YNUYM0Nv3IdtpMTHGlGix4=211D6EE3")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))