import os
import os.path
import json
import requests


def scrape_linkedin_profile(name="eden-marco"):
    fname = f"{name}.json"
    if os.path.isfile(fname):
        with open(fname, "r") as fh:
            str = fh.read()
            return json.loads(str)

    proxyCurlUrl = "https://nubela.co/proxycurl/api/v2/linkedin"
    linkedInUrl = f"https://www.linkedin.com/in/{name}"
    hHeaders = {"Authorization": f"Bearer {os.environ['PROXYCURL_API_KEY']}"}
    hParams = {
        "url": linkedInUrl,  # will work with just this
        "fallback_to_cache": "on-error",
        "use_cache": "if-present",
        "skills": "include",
        "inferred_salary": "include",
        "personal_email": "include",
        "personal_contact_number": "include",
        "twitter_profile_id": "include",
        "facebook_profile_id": "include",
        "github_profile_id": "include",
        "extra": "include",
    }

    # --- resp has these fields:
    #        status_code - should be 200, otherwise an error occurred
    #        headers - a hash of header name/header value
    #        encoding - should be 'utf-8'
    #        text - the text of the response, should be a JSON string
    #        json() - interprets text as JSON, returns a data structure

    resp = requests.get(proxyCurlUrl, params=hParams, headers=hHeaders)
    assert resp.status_code == 200, "Bad status"
    with open(fname, "w") as fh:
        fh.write(resp.text)
    return resp.json()


# def scrape_linkedin_profile(linkedin_profile_url: str):
#     """scrape information from LinkedIn profiles,
#     Manually scrape the information from the LinkedIn profile"""
#     api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
#     header_dic = {
#         "Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

#     response = requests.get(
#         api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
#     )

#     data = response.json()
#     data = {
#         k: v
#         for k, v in data.items()
#         if v not in ([], "", "", None)
#         and k not in ["people_also_viewed", "certifications"]
#     }
#     if data.get("groups"):
#         for group_dict in data.get("groups"):
#             group_dict.pop("profile_pic_url")

#     return data
