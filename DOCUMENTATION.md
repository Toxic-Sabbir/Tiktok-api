# TikToksAPI 
This is a Python wrapper for the TikTok API, allowing developers to interact with TikTok programmatically.

## Initialization
To use the TikTokAPI, you need to create an instance of the TikTokAPI class:
```py
from TikToksAPI import TikToksAPI

# Create an instance of TikToksAPI with session ID
user = TikToksAPI(session_id="your_session_id")
```


## Profile

### `edit(self, enum: str, text: str) -> requests.Response`
Edits the specified enumeration using the specified text.
- `Args:`
  - **enum (str)**: The enumeration to use for the edit. "signature" or "nickname" or "username"
  - **text (str)**: The text to edit.
- `Returns:`
  - **requests.Response**: The response object containing information after editing the enumeration.
```py
response = api.edit(enum="signature", text="example")
print(response.json())
```

### `verify(self) -> requests.Response`
Verifies sesssion ID.
- `Args:`
  - `None`
- `Returns:`
  - **requests.Response**: The response object containing information about the session ID.
```py
from TikToksAPI import TikToksAPI

# Create an instance of TikToksAPI with session ID
user = TikToksAPI(session_id="your_session_id")
print(user.verify())
```

## User

### `follow(self, username: str) -> requests.Response`
Follows a specified user.
- `Args:`
  - **username (str)**: The username of the user to follow.
- `Returns:`
  - **requests.Response**: The response object containing information about the follow action.
```py
api = TikToksAPI(session_id="your_session_id")
response = tiktoks_api.follow("soldier")
print(response.json())  
```

### `unfollow(self, username: str) -> requests.Response`
Follows a specified user.
- `Args:`
  - **username (str)**: The username of the user to unfollow.
- `Returns:`
  - **requests.Response**: The response object containing information about the unfollow action.
```py
api = TikToksAPI(session_id="your_session_id")
response = tiktoks_api.unfollow("soldier")
print(response.json())  
```

### `following_list(self, username: str, count: int) -> requests.Response`
Gets the list of a users following by their username.
- `Args:`
  - **username (str)**: The username of the user whose following list to retrieve.
  - **count (int)**: The maximum number of users to retrieve.
- `Returns:`
  - **requests.Response**: The response object containing information about the following list.
```py
following = api.following_list("soldier")
print(following.json())
```

### `followers_list(self, username: str, count: int) -> requests.Response`
Gets the list of a users followers by their username.
- `Args:`
  - **username (str)**: The username of the user whose followers list to retrieve.
  - **count (int)**: The maximum number of users to retrieve.
- `Returns:`
  - **requests.Response**: The response object containing information about the following list.
```py
followers = api.followers_list("soldier")
print(followers.json())
```


# Posts
### `like(self, video_id: int) -> requests.Response`
Likes a specified video.
- `Args:`
  - **video_id (int)**: The ID of the video to like.
- `Returns:`
  - **requests.Response:** The response object containing information about the like.
```py
api = TikToksAPI(session_id="your_session_id")
response = api.like(1232345)
print(response.json()) 
```

### `unlike(self, video_id: int) -> requests.Response`
Unlikes a specified video.
- `Args:`
  - **video_id (int)**: The ID of the video to unlike.
- `Returns:`
  - **requests.Response:** The response object containing information about the unlike.
```py
api = TikToksAPI(session_id="your_session_id")
response = api.unlike(1232345)
print(response.json()) 
```

## Misc
### `cookies_to_session(self, cookies: str) -> str`
Static method to extract the session ID from a string of cookies.
```py
cookies = "_ga=GA1.2.123456; sessionid=3e5f47507a3da4915c68c72e359e263c; csrftoken=abcde"
session_id = TikToksAPI.cookies_to_session(cookies)
print(session_id)
# Output: "3e5f47507a3da4915c68c72e359e263c"
```
