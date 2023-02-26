# www.aithe.dev
# github.com/aithedev/TikToksAPI

import Terminalia
import requests
import secrets
import hashlib
import urllib
import time

from .utils.signature import signature

class TikToksAPI:
    def __init__(
        self,
        session_id: str,
        custom_device_id: dict = None
    ) -> None:

        self.base_url = "https://api-h2.tiktokv.com/"
        self.session = requests.Session()

        self.headers = {
            "accept-encoding": "gzip",
            "connection": "Keep-Alive",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "host": "api-h2.tiktokv.com",
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "user-agent": "okhttp/3.10.0.1",
            "x-ss-req-ticket": str(int(time.time() * 1000))
        }
        self.params = {
            'manifest_version_code': 190103, 
            '_rticket': int(round(time.time() * 1000)), 
            'current_region': 'BE', 
            'app_language': 'en', 
            'app_type': 'normal', 
            'iid': 7183409061831001857 if self.custom_device_id == None else custom_device_id['iid'], 
            'channel': 'googleplay', 
            'device_type': 'ASUS_Z01QD', 
            'language': 'en', 
            'cpu_support64': 'true', 
            'host_abi': 'armeabi-v7a', 
            'locale': 'en', 
            'resolution': 1600*900, 
            'openudid': '7f8e923db4b22341', 
            'update_version_code': 190103, 
            'ac2': 'wifi', 
            'cdid': 'c7357243-a13f-4d42-94d9-cb318ae73c52', 
            'sys_region': 'US', 
            'os_api': 28, 
            'uoo': 0, 
            'timezone_name': 'Asia/Shanghai', 
            'dpi': 300, 
            'residence': 'BE', 
            'carrier_region': 'BE', 
            'ac': 'wifi', 
            'device_id': 7147445232161539590 if self.custom_device_id == None else custom_device_id['did'], 
            'mcc_mnc': 20610, 
            'os_version': 9, 
            'timezone_offset': 28800, 
            'version_code': 190103, 
            'app_name': 'trill', 
            'ab_version': '19.1.3', 
            'version_name': '19.1.3', 
            'device_brand': 'Asus', 
            'op_region': 'BE', 
            'ssmix': 'a', 
            'device_platform': 'android', 
            'build_number': '19.1.3', 
            'region': 'US', 
            'aid': 1180, 
            'ts': int(time.time())
        }
        self.session.headers.update(self.headers)
        self.session.params.update(self.params)
        self.session.cookies.update({"sessionid": session_id})

    @staticmethod
    def query(data: str) -> str:
        return urllib.parse.urlencode(data)

    @staticmethod
    def cookies_to_session(cookies: str) -> str:
        """
        Convert cookies string to session ID.
    
        Args:
            cookies (str): A string of cookies received from a client.
    
        Returns:
            str: The session ID parsed from the cookies string.
        """
        return cookies.split(";")[13].replace(" ", "")

    @staticmethod
    def user_info(self) -> requests.Response:
        requests.Response = requests.get(
            url = "https://www.tiktok.com/passport/web/account/info/",
            headers = {
                "cookie"     : f"sessionid={self.session_id}",
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
        )
        
        return requests.Response

    def get_user_ids(self, username) -> dict:
        requests.Response = requests.post(
            url = f"https://search16-normal-c-useast1a.tiktokv.com/aweme/v1/search/user/sug/?iid=7202411203019441925&device_id=7147445232161539590&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=270804&version_name=27.8.4&device_platform=android&ab_version=27.8.4&ssmix=a&device_type=ASUS_Z01QD&device_brand=Asus&language=en&os_api=25&os_version=7.1.2&openudid=704713c0da01388a&manifest_version_code=2022708040&resolution=1024*576&dpi=191&update_version_code=2022708040&_rticket=1674508422512&app_type=normal&sys_region=CN&mcc_mnc=20408&timezone_name=Asia%2FShanghai&ts=1674508425&timezone_offset=28800&build_number=27.8.4&region=CN&uoo=0&app_language=en&carrier_region=NL&locale=en&op_region=NL&ac2=wifi&host_abi=armeabi-v7a&cdid=5b45c87e-eaea-47d9-9d73-f9cef7ecabb5",
            headers = {
                'accept-encoding': 'gzip',
                'connection': 'Keep-Alive',
                'content-length': '65',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'sessionid=6db9138c78bb3f915cf7e73e0ff75caf;',
                'host': 'search16-normal-c-useast1a.tiktokv.com',
                'multi_login': '1',
                'passport-sdk-version':'19', 
                'sdk-version': '2',
                'user-agent': 'com.zhiliaoapp.musically/2022708040 (Linux; U; Android 7.1.2; zh_CN; ASUS_Z01QD; Build/N2G48H;tt-ok/3.12.13.1)',
                'x-bd-kmsv': '0',
                'x-gorgon': '04044092400006417ee1e5af3aac9c8eebf59032b22f70486f65',
                'x-khronos': "1676942260",
                'x-tt-store-region': 'nl',
                'x-tt-store-region-src': 'uid',
                'x-vc-bdturing-sdk-version': '2.2.1.i18n'
            },
            data = {
                'mention_type': '3',
                'keyword': username,
                'source': 'comment_user',
                'count': '10',
                'uid_filter_list':''
            }
        ).json()

        return {
            "sec_user_id": requests.Response["sug_list"][0]["extra_info"]['sug_sec_user_id'],
            "user_id": requests.Response["sug_list"][0]["extra_info"]['sug_user_id']
        }

    def verify(self) -> requests.Response:
        """
        Verifies sesssion ID.

        Args:
            None

        Returns:
            requests.Response: The response object containing information about the session ID.
        """
        return self.user_info()
    
    def edit(self, enum: str, text: str) -> requests.Response: 
        """
        Edits the specified enumeration using the specified text.
    
        Args:
            enum (str): The enumeration to use for the edit. "signature" or "nickname" or "username"
            text (str): The text to set.
    
        Returns:
            requests.Response: The response object containing information after editing the enumeration.
        """

        data = {
            "uid": self.user_info().json()["data"]["user_id"],
            "page_from": 0,
            enum: text,
            "confirmed": 0 
        } 
        data if choice != "username" else data.pop("confirmed")
        
        self.session.headers.update({
            **signature(
                params = self.query(self.session.params),
                data = self.query(data),
                cookies = self.session.cookies
            ).get_value(),
            "x-ss-stub": str(hashlib.md5(self.query(data).encode()).hexdigest()).upper()
        })

        return self.session.post(
            url = self.base_url + "aweme/v1/commit/user/?" if choice != "username" else "passport/login_name/update/?",
            data = data
        )


    def check(self, username: str) -> requests.Response:
        """
        Checks whether the specified username is available.

        Args:
            username (str): The username to check.

        Returns:
            requests.Response: The response object containing the availability status.
        """
    
        self.session.params.update({"unique_id": username})
        self.session.headers.update({
            **signature(
                params = self.query(self.params),
                data = None,
                cookies = self.session.cookies
            ).get_value()
        })
    
        return self.session.post(url = self.base_url + "aweme/v1/unique/id/check/?")

    def following_followers(self, choice: str, username: str, count: int) -> requests.Response:
        self.session.params.update(
            {
                'user_id': self.get_user_ids(username)["user_id"], 
                'sec_user_id': self.get_user_ids(username)["sec_user_id"], 
                'max_time': 0,
                'count': count,
                'offset': 0,
                'source_type': 1,
                'address_book_access': 1
            }
        )
        self.session.headers.update({
            **signature(
                params = self.query(self.session.params),
                data = None,
                cookies = self.session.cookies
            ).get_value()
        })

        return self.session.get(url = self.base_url + f"aweme/v1/user/{choice}/list/?")

    def following_list(self, username: str, count: int) -> requests.Response:
        """
        Gets the list of a users following by their username.

        Args:
            username (str): The username of the user whose following list to retrieve.
            count (int): The number of users to retrieve.

        Returns:
            requests.Response: The response object containing information about the following list.
        """

        return self.following_followers("following", username, count)

    def followers_list(self, username: str, count: int) -> requests.Response:
        """
        Gets the list of a users followers by their username.

        Args:
            username (str): The username of the user whose followers list to retrieve.
            count (int): The number of users to retrieve.

        Returns:
            requests.Response: The response object containing information about the followers list.
        """

        return self.following_followers("followers", username, count)


    def toggle_like(self, like_type: int, video_id: int) -> requests.Response:
        self.session.params.update(
            {
                'aweme_id': video_id, 
                'enter_from': 'homepage_hot', 
                'type': like_type,
                'channel_id': 0,
            }
        )
        self.session.headers.update({
            **signature(
                params = self.query(self.session.params),
                data = None,
                cookies = self.session.cookies
            ).get_value()
        })

        return self.session.post(url = self.base_url + "aweme/v1/commit/item/digg/?")

        def like(self, video_id: int) -> requests.Response:
            """
            Likes a specified video.

            Args:
                video_id (int): The ID of the video to like.

            Returns:
                requests.Response: The response object containing information about the like.
            """

            return self.toggle_like(1, video_id)

        def unlike(self, video_id: int) -> requests.Response:
            """
            Unlikes a specified video.

            Args:
                video_id (int): The ID of the video to unlike.

            Returns:
                requests.Response: The response object containing information about the unlike.
            """

            return self.toggle_like(0, video_id)

    def toggle_follow(self, like_type: int, username: int) -> requests.Response:
        self.session.params.update(
            {
                'city': '',
                'sec_user_id': self.get_user_ids(username)["sec_user_id"],
                'from': 0,
                'from_pre': -1,
                'enter_from': 'homepage_hot', 
                'type': like_type,
                'channel_id': 3,
            }
        )
        self.session.headers.update({
            **signature(
                params = self.query(self.session.params),
                data = None,
                cookies = self.session.cookies
            ).get_value()
        })

        return self.session.post(url = self.base_url + "aweme/v1/commit/follow/user/?")

    def follow(self, username: str) -> requests.Response:
        """
        Follows a specified user.

        Args:
            username (str): The username of the user to follow.

        Returns:
            requests.Response: The response object containing information about the follow action.
        """

        return self.toggle_follow(1, username)


    def unfollow(self, username: str) -> requests.Response:
        """
        Unfollows a specified user.

        Args:
            username (str): The username of the user to unfollow.

        Returns:
            requests.Response: The response object containing information about the unfollow action.
        """

        return self.toggle_follow(0, username)
