from typing import BinaryIO
from requests import Session

class Lolzteam:
    def __init__(self, token: str) -> None:
        self.api = "https://api.lolz.guru"
        self.session = Session()
        self.session.headers = {
            "Authorization": f"Bearer {token}"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def _post(self, endpoint: str, data: dict = None) -> dict:
        return self.session.post(
            f"{self.api}{endpoint}", data=data).json()

    def _put(self, endpoint: str, data: dict = None) -> dict:
        return self.session.put(
            f"{self.api}{endpoint}", data=data).json()

    def _delete(self, endpoint: str, params: dict = None) -> dict:
        return self.session.delete(
            f"{self.api}{endpoint}", params=params).json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def get_categories(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list") -> dict:
        params = self._filter({
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id
        })
        return self._get(f"/categories?order={order}", params)

    def get_category_info(self, category_id: int) -> dict:
        return self._get(f"/categories/{category_id}")

    def get_forums(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list") -> dict:
        params = self._filter({
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id
        })
        return self._get(f"/forums?order={order}", params)

    def get_forum_info(self, forum_id: int) -> dict:
        return self._get(f"/forums/{forum_id}")

    def get_forum_followers(self, forum_id: int) -> dict:
        return self._get(f"/forums/{forum_id}/followers")

    def follow_forum(
            self,
            forum_id: int,
            post: int = 0,
            alert: int = 1,
            email: int = 0) -> dict:
        data = {
            "post": post,
            "alert": alert,
            "email": email
        }
        return self._post(f"/forums/{forum_id}/followers", data)

    def unfollow_forum(self, forum_id: int) -> dict:
        return self._delete(f"/forums/{forum_id}/followers")

    def get_pages(
            self, parent_page_id: int = None, order: str = "list") -> dict:
        params = self._filter({"parent_page_id": parent_page_id})
        return self._get(f"/pages?order={order}", params)

    def get_page_info(self, page_id: int) -> dict:
        return self._get(f"/pages/{page_id}")

    def get_navigation(self, parent_element_id: int = None) -> dict:
        params = self._filter({"parent": parent_element_id})
        return self._get("/navigation", params)

    def get_threads_list(
            self,
            forum_id: int = None,
            thread_ids: str = None,
            creator_user_id: int = None,
            sticky: int = 0,
            thread_prefix_id: int = None,
            thread_tag_id: int = None,
            page: int = None,
            limit: int = None,
            order: str = None,
            thread_create_date: str = None,
            thread_update_date: str = None) -> dict:
        params = self._filter({
            "sticky": sticky,
            "forum_id": forum_id,
            "thread_ids": thread_ids,
            "creator_user_id": creator_user_id,
            "thread_prefix_id": thread_prefix_id,
            "thread_tag_id": thread_tag_id,
            "page": page,
            "limit": limit,
            "order": order,
            "thread_create_date": thread_create_date,
            "thread_update_date": thread_update_date
        })
        return self._get("/threads", params)

    def create_thread(
            self,
            forum_id: int,
            thread_title: str,
            content: str,
            thread_prefix_id: int = None,
            thread_tags: str = None) -> dict:
        data = self._filter({
            "forum_id": forum_id,
            "thread_title": thread_title,
            "post_body": content,
            "thread_prefix_id": thread_prefix_id,
            "thread_tags": thread_tags
        })
        return self._post("/threads", data)

    def upload_thread_attachment(
            self,
            forum_id: int,
            file: BinaryIO,
            attachment_hash: str = None) -> dict:
        data = self._filter({
            "file": file.read(),
            "forum_id": forum_id,
            "attachment_hash": attachment_hash
        })
        return self._post("/threads/attachments", data)

    def delete_thread_attachment(
            self,
            forum_id: int,
            attachment_id: int,
            attachment_hash: str = None) -> dict:
        params = self._filter({"attachment_hash": attachment_hash})
        return self._delete(
            f"/threads/attachments?forum_id={forum_id}&attachment_id={attachment_id}",
            params)

    def get_thread_info(self, thread_id: int) -> dict:
        return self._get(f"/threads/{thread_id}")

    def delete_thread(self, thread_id: int) -> dict:
        return self._delete(f"/threads/{thread_id}")

    def get_thread_followers(self, thread_id: int) -> dict:
        return self._get(f"/threads/{thread_id}/followers")

    def follow_thread(self, thread_id: int, email: int = 0) -> dict:
        return self._post(f"/threads/{thread_id}/followers", {"email": email})

    def unfollow_thread(self, thread_id: int) -> dict:
        return self._delete(f"/threads/{thread_id}/followers")

    def get_thread_navigation(self, thread_id: int) -> dict:
        return self._get(f"/threads/{thread_id}/navigation")

    def get_thread_poll_info(self, thread_id: int) -> dict:
        return self._get(f"/threads/{thread_id}/poll")

    def vote_poll(
            self,
            thread_id: int,
            response_id: int,
            response_ids: str = None) -> dict:
        data = self._filter({
            "response_id": response_id,
            "response_ids": response_ids
        })
        return self._post(f"/threads/{thread_id}/poll/votes", data)

    def get_poll_results(self, thread_id: int) -> dict:
        return self._get(f"/threads/{thread_id}/poll/results")

    def get_new_threads(
            self,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None) -> dict:
        params = self._filter({
            "forum_id": forum_id,
            "data_limit": data_limit
        })
        return self._get(f"/threads/new?limit={limit}", params)

    def get_recent_threads(
            self,
            days: int = None,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None) -> dict:
        params = self._filter({
            "days": days,
            "forum_id": forum_id,
            "data_limit": data_limit
        })
        return self._get(f"/threads/recent?limit={limit}", params)

    def get_thread_posts(
            self,
            thread_id: int = None,
            page_of_post_id: int = None,
            post_ids: str = None,
            page: int = None,
            limit: int = None,
            order: str = "natural") -> dict:
        params = self._filter({
            "thread_id": thread_id,
            "page_of_post_id": page_of_post_id,
            "post_ids": post_ids,
            "page": page,
            "limit": limit
        })
        return self._get(f"/posts?order={order}", params)

    def create_post(
            self,
            thread_id: int,
            quote_post_id: int = None,
            content: str = None) -> dict:
        data = self._filter({
            "thread_id": thread_id,
            "post_body": content,
            "quote_post_id": quote_post_id
        })
        return self._post("/posts", data)

    def upload_post_attachment(
            self,
            file: BinaryIO,
            thread_id: int = None,
            post_id: int = None,
            attachment_hash: str = None) -> dict:
        data = {"file": file.read()}
        if thread_id:
            data["thread_id"] = thread_id
        elif post_id:
            data["post_id"] = post_id
        elif attachment_hash:
            data["attachment_hash"] = attachment_hash
        return self._post("/posts/attachments", data)

    def get_post_info(self, post_id: int) -> dict:
        return self._get(f"/posts/{post_id}")

    def edit_post(
            self,
            post_id: int,
            content: str,
            thread_title: str = None,
            thread_prefix_id: int = None,
            thread_tags: str = None,
            thread_node_id: int = None) -> dict:
        data = self._filter({
            "post_body": content,
            "thread_title": thread_title,
            "thread_prefix_id": thread_prefix_id,
            "thread_tags": thread_tags,
            "thread_node_id": thread_node_id
        })
        return self._put(f"/posts/{post_id}", data)

    def delete_post(self, post_id: int) -> dict:
        return self._delete(f"/posts/{post_id}")

    def get_post_attachments(self, post_id: int) -> dict:
        return self._get(f"/posts/{post_id}/attachments")

    def delete_post_attachment(
            self, post_id: int, attachment_id: int) -> dict:
        return self._delete(
            f"/posts/{post_id}/attachments/{attachment_id}")

    def get_post_likes(
            self, post_id: int, page: int = None, limit: int = 10) -> dict:
        params = self._filter({"page": page})
        return self._get(f"/posts/{post_id}/likes?limit={limit}", params)

    def like_post(self, post_id: int) -> dict:
        return self._post(f"/posts/{post_id}/likes")

    def unlike_post(self, post_id: int) -> dict:
        return self._delete(f"/posts/{post_id}/likes")

    def report_post(self, post_id: int, message: str) -> dict:
        return self._post(f"/posts/{post_id}/report", {"message": message})

    def get_popular_tags(self) -> dict:
        return self._get("/tags")

    def get_tags_list(self) -> dict:
        return self._get("/tags/list")

    def get_tagged_content(
            self, tag_id: int, page: int = None, limit: int = 10) -> dict:
        params = self._filter({"page": page})
        return self._get(f"/tags/{tag_id}?limit={limit}", params)

    def get_filtered_tags_list(self, tag: str) -> dict:
        return self._get(f"/tags/find?tag={tag}")

    def get_users_list(self, page: int = None, limit: int = 10) -> dict:
        params = self._filter({"page": page})
        return self._get(f"/users?limit={limit}", params)

    def register(
            self,
            email: str,
            username: str,
            password: str,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: str = None,
            client_id: str = None,
            extra_data: str = None,
            extra_timestamp: int = None) -> dict:
        data = self._filter({
            "user-email": email,
            "username": username,
            "password": password,
            "user_dob_day": user_dob_day,
            "user_dob_month": user_dob_month,
            "user_dob_year": user_dob_year,
            "fields": fields,
            "client_id": client_id,
            "extra_data": extra_data,
            "extra_timestamp": extra_timestamp
        })
        return self._post("/users", data)

    def get_user_fields(self) -> dict:
        return self._get("/users/fields")

    def find_user(
            self,
            username: str = None,
            user_email: str = None) -> dict:
        params = self._filter({
            "username": username,
            "user_email": user_email
        })
        return self._get("/users/find", params)

    def get_user_info(self, user_id: int) -> dict:
        return self._get(f"/users/{user_id}")

    def edit_user(
            self,
            user_id: int,
            password: str = None,
            old_password: str = None,
            email: str = None,
            username: str = None,
            user_title: str = None,
            primary_group_id: int = None,
            secondary_group_ids: str = None,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: str = None) -> dict:
        data = self._filter({
            "password": password,
            "password_old": old_password,
            "user_email": email,
            "username": username,
            "user_title": user_title,
            "primary_group_id": primary_group_id,
            "secondary_group_ids": secondary_group_ids,
            "user_dob_day": user_dob_day,
            "user_dob_month": user_dob_month,
            "user_dob_year": user_dob_year,
            "fields": fields
        })
        return self._put(f"/users/{user_id}", data)

    def upload_avatar(self, user_id: int, file: BinaryIO) -> dict:
        return self._post(
            f"/users/{user_id}/avatar", {"avatar": file.read()})

    def delete_avatar(self, user_id: int) -> dict:
        return self._delete(f"/users/{user_id}/avatar")

    def get_user_followers(self, user_id: int) -> dict:
        return self._get(f"/users/{user_id}/followers")

    def follow_user(self, user_id: int) -> dict:
        return self._post(f"/users/{user_id}/followers")

    def unfollow_user(self, user_id: int) -> dict:
        return self._delete(f"/users/{user_id}/followers")

    def get_user_followings(
            self,
            user_id: int,
            order: str = "natural",
            page: int = None,
            limit: int = None) -> dict:
        params = self._filter({"page": page, "limit": limit})
        return self._get(
            f"/users/{user_id}/followings?order={order}", params)

    def get_ignored_users(self) -> dict:
        return self._get("/users/ignored")

    def ignore_user(self, user_id: int) -> dict:
        return self._post(f"/users/{user_id}/ignore")

    def unignore_user(self, user_id: int) -> dict:
        return self._delete(f"/users/{user_id}/ignore")

    def get_all_user_groups(self) -> dict:
        return self._get("/users/groups")

    def get_user_groups(self, user_id: int) -> dict:
        return self._get(f"/users/{user_id}/groups")

    def get_current_user(self) -> dict:
        return self._get("/users/me")

    def get_user_contents(
            self, user_id: int, page: int = None, limit: int = 10) -> dict:
        params = self._filter({"page": page})
        return self._get(
            f"/users/{user_id}/timeline?limit={limit}", params)

    def create_profile_post(self, user_id: int, post_body: str) -> dict:
        return self._post(
            f"/users/{user_id}/timeline", {"post_body": post_body})

    def get_profile_post_info(self, profile_post_id: int) -> dict:
        return self._get(f"/profile-posts/{profile_post_id}")

    def edit_profile_post(
            self, profile_post_id: int, post_body: str) -> dict:
        return self._put(
            f"/profile-posts/{profile_post_id}", {"post_body": post_body})

    def delete_profile_post(
            self, profile_post_id: int, reason: str = None) -> dict:
        params = self._filter({"reason": reason})
        return self._delete(f"/profile-posts/{profile_post_id}", params)

    def get_profile_post_likes(self, profile_post_id: int) -> dict:
        return self._get(f"/profile-posts/{profile_post_id}/likes")

    def like_profile_post(self, profile_post_id: int) -> dict:
        return self._post(f"/profile-posts/{profile_post_id}/likes")

    def unlike_profile_post(self, profile_post_id: int) -> dict:
        return self._delete(f"/profile-posts/{profile_post_id}/likes")

    def get_profile_post_comments(
            self,
            profile_post_id: int,
            before: str = None,
            limit: int = 10) -> dict:
        params = self._filter({"before": before})
        return self._get(
            f"/profile-posts/{profile_post_id}/comments?limit={limit}", params)

    def comment_profile_post(
            self, profile_post_id: int, comment_body: str) -> dict:
        return self._post(
            f"/profile-posts/{profile_post_id}/comments",
            {"comment_body": comment_body})

    def get_profile_post_comment(
            self, profile_post_id: int, comment_id: int) -> dict:
        return self._get(
            f"/profile-posts/{profile_post_id}/comments/{comment_id}")

    def delete_profile_post_comment(
            self, profile_post_id: int, comment_id: int) -> dict:
        return self._delete(
            f"/profile-posts/{profile_post_id}/comments/{comment_id}")

    def report_profile_post(
            self, profile_post_id: int, message: str) -> dict:
        return self._post(
            f"/profile-posts/{profile_post_id}/report", {"message": message})

    def get_conversations(
            self, page: int = None, limit: int = 10) -> dict:
        params = self._filter({"page": page})
        return self._get(f"/conversations?limit={limit}", params)

    def create_conversation(
            self,
            conversation_title: str,
            recipients: str,
            content: str) -> dict:
        data = {
            "conversation_title": conversation_title,
            "recipients": recipients,
            "message_body": content
        }
        return self._post("/conversations", data)

    def get_conversation_info(self, conversation_id: int) -> dict:
        return self._get(f"/conversations/{conversation_id}")

    def delete_conversation(self, conversation_id: int) -> dict:
        return self._delete(f"/conversations/{conversation_id}")

    def upload_conversation_attachment(
            self, file: BinaryIO, attachment_hash: str = None) -> dict:
        data = self._filter({
            "file": file.read(),
            "attachment_hash": attachment_hash
        })
        return self._post("/conversations/attachments", data)

    def delete_conversation_attachment(
            self, attachment_id: int, attachment_hash: str = None) -> dict:
        params = self._filter({"attachment_hash": attachment_hash})
        return self._delete(
            f"/conversations/attachments?attachment_id={attachment_id}", params)

    def get_conversation_messages(
            self,
            conversation_id: int,
            page: int = None,
            limit: int = None,
            order: str = None,
            before: str = None,
            after: str = None) -> dict:
        params = self._filter({
            "page": page,
            "limit": limit,
            "order": order,
            "before": before,
            "after": after
        })
        return self._get(
            f"/conversation-messages?conversation_id={conversation_id}", params)

    def send_message(self, conversation_id: int, message: str) -> dict:
        data = {
            "conversation_id": conversation_id,
            "message_body": message
        }
        return self._post("/conversation-messages", data)

    def upload_message_attachment(
            self,
            file: BinaryIO,
            conversation_id: int = None,
            message_id: int = None,
            attachment_hash: str = None) -> dict:
        data = {"file": file.read()}
        if conversation_id:
            data["conversation_id"] = conversation_id
        elif message_id:
            data["message_id"] = message_id
        elif attachment_hash:
            data["attachment_hash"] = attachment_hash
        return self._post("/conversation-messages/attachments", data)

    def get_message_info(self, message_id: int) -> dict:
        return self._get(f"/conversation-messages/{message_id}")

    def edit_message(self, message_id: int, message_body: str) -> dict:
        return self._put(
            f"/conversation-messages/{message_id}",
            {"message_body": message_body})

    def delete_message(self, message_id: int) -> dict:
        return self._delete(f"/conversation-messages/{message_id}")

    def get_message_attachments(self, message_id: int) -> dict:
        return self._get(
            f"/conversation-messages/{message_id}/attachments")

    def delete_message_attachment(
            self,
            message_id: int,
            attachment_id: int,
            conversation_id: int = None,
            attachment_hash: str = None) -> dict:
        params = self._filter({
            "conversation_id": conversation_id,
            "attachment_hash": attachment_hash
        })
        return self._delete(
            f"/conversation-messages/{message_id}/attachments/{attachment_id}",
            params)

    def report_message(self, message_id: int, message: str) -> dict:
        return self._post(
            f"/conversation-messages/{message_id}/report",
            {"message": message})

    def get_notifications(self) -> dict:
        return self._get("/notifications")

    def get_notification_content(self, notification_id: int) -> dict:
        return self._get(f"/notifications/{notification_id}/content")

    def send_custom_alert(
            self,
            user_id: int,
            message: str,
            notification_type: int = None,
            extra_data: str = None) -> dict:
        data = self._filter({
            "user_id": user_id,
            "message": message,
            "notification_type": notification_type,
            "extra_data": extra_data
        })
        return self._post("/notifications/custom", data)

    def mark_notification_read(self, notification_id: int = None) -> dict:
        data = self._filter({"notification_id": notification_id})
        return self._post("/notifications/read", data)

    # Search

    def search_threads(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None) -> dict:
        data = self._filter({
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        })
        return self._post("/search/threads", data)

    def search_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None) -> dict:
        data = self._filter({
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        })
        return self._post("/search/posts", data)

    def search_profile_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None) -> dict:
        data = self._filter({
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit
        })
        return self._post("/search/profile-posts", data)

    def search(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None) -> dict:
        data = self._filter({
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit
        })
        return self._post("/search", data)

    def search_tagged(
            self,
            tag: str,
            tags: str = None,
            page: int = None,
            limit: int = None) -> dict:
        data = self._filter({
            "tag": tag,
            "tags": tags,
            "page": page,
            "limit": limit
        })
        return self._post("/search/tagged", data)
