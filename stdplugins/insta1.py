# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import requests
import json

@borg.on(events.NewMessage(pattern=r".ig (.*)", incoming=True))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "https://rest.farzain.com/api/ig_profile.php?id={}&apikey={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(input_str, apikey)).json()
    if response_api["cod"] == 200:
        await event.edit(input_str + "\n `" +  "Username:" + json.dumps(response_api["username"]) + "`\n" + "Full Name:" +  json.dumps(response_api["full_name"]) + "`\n" + "Followers:" + json.dumps(response_api["followers"]) + "`\n"  + "Following:" + json.dumps(response_api["following"]) + "`\n" + "Post Count:" +  json.dumps(response_api["post"]) + "`\n" + "Profile Picture Url:" + json.dumps(response_api["profile_pict"]) + "`\n" + "Creator:" + "@hackedyouagain")
    else:
         await event.edit(input_str + "\n `" +  "Username:" + json.dumps(response_api["username"]) + "`\n" + "Full Name:" +  json.dumps(response_api["full_name"]) + "`\n" + "Followers:" + json.dumps(response_api["followers"]) + "`\n"  + "Following:" + json.dumps(response_api["following"]) + "`\n" + "Post Count:" +  json.dumps(response_api["post"]) + "`\n" + "Profile Picture Url:" + json.dumps(response_api["profile_pict"]) + "`\n" + "Creator:" + "@hackedyouagain")