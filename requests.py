from requests import get

# websites = (
# 	"google.com",
# 	"airbnb.com",
# 	"https://twitter.com",
# 	"facebook.com",
# 	"https://tiktok.com",
# )

websites = (
	"httpstat.us/200",
	"httpstat.us/206",
	"https://httpstat.us/305",
	"httpstat.us/404",
	"https://httpstat.us/502",
)

results = {}

for website in websites:
	if not website.startswith("https://"):
		website = f"https://{website}"
  
	response = get(website)
	status = str(response.status_code)
	
	if status.startswith("2"):
		results[website] = "OK"
	elif status.startswith("3"):
		results[website] = "REDIRECTED"
	else:
		results[website] = "FAILED"

print(results)