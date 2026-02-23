from typing import BinaryIO
from requests import Session

class Lolzteam:
    def __init__(self, token: str) -> None:
        self.api = "https://api.lolz.guru"
        self.session = Session()
        self.session.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_categories(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list") -> dict:
        params = {
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/categories?order={order}", params=filtered_params).json()

    def get_category_info(self, category_id: int) -> dict:
        return self.session.get(
            f"{self.api}/categories/{category_id}").json()

    def get_forums(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list") -> dict:
        params = {
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/forums?order={order}", params=filtered_params).json()

    def get_forum_info(self, forum_id: int) -> dict:
        return self.session.get(
            f"{self.api}/forums/{forum_id}").json()

    def get_forum_followers(self, forum_id: int) -> dict:
        return self.session.get(
            f"{self.api}/forums/{forum_id}/followers").json()

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
        return self.session.post(
            f"{self.api}/forums/{forum_id}/followers", data=data).json()

    def unfollow_forum(self, forum_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/forums/{forum_id}/followers").json()

    def get_pages(
            self, parent_page_id: int, order: str = "list") -> dict:
        params = {"parent_page_id": parent_page_id} if parent_page_id else {}
        return self.session.get(
            f"{self.api}/pages?order={order}", params=params).json()

    def get_page_info(self, page_id: int) -> dict:
        return self.session.get(f"{self.api}/pages/{page_id}").json()

    def get_navigation(self, parent_element_id: int = None) -> dict:
        params = {"parent": parent_element_id} if parent_element_id else {}
        return self.session.get(
            f"{self.api}/navigation", params=params).json()

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
        params = {
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
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/threads", params=filtered_params).json()

    def create_thread(
            self,
            forum_id: int,
            thread_title: str,
            content: str,
            thread_prefix_id: int = None,
            thread_tags: str = None) -> dict:
        data = {
            "forum_id": forum_id,
            "thread_title": thread_title,
            "post_body": content
        }
        if thread_prefix_id:
            data["thread_prefix_id"] = thread_prefix_id
        if thread_tags:
            data["thread_tags"] = thread_tags
        return self.session.post(
            f"{self.api}/threads", data=data).json()

    def upload_thread_attachment(
            self,
            forum_id: int,
            file: BinaryIO,
            attachment_hash: str = None) -> dict:
        data = {
            "file": file.read(),
            "forum_id": forum_id
        }
        if attachment_hash:
            data["attachment_hash"] = attachment_hash
        return self.session.post(
            f"{self.api}/threads/attachments", data=data).json()

    def delete_thread_attachment(
            self,
            forum_id: int,
            attachment_id: int,
            attachment_hash: str = None) -> dict:
        params = {"attachment_hash": attachment_hash} if attachment_hash else {}
        return self.session.delete(
            f"{self.api}/threads/attachments?forum_id={forum_id}&attachment_id={attachment_id}",
            params=params).json()

    def get_thread_info(self, thread_id: int) -> dict:
        return self.session.get(
            f"{self.api}/threads/{thread_id}").json()

    def delete_thread(self, thread_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/threads/{thread_id}").json()

    def get_thread_followers(self, thread_id: int) -> dict:
        return self.session.get(
            f"{self.api}/threads/{thread_id}/followers").json()

    def follow_thread(self, thread_id: int, email: int = 0) -> dict:
        data = {"email": email}
        return self.session.post(
            f"{self.api}/threads/{thread_id}/followers", data=data).json()

    def unfollow_thread(self, thread_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/threads/{thread_id}/followers").json()

    def get_thread_navigation(self, thread_id: int) -> dict:
        return self.session.get(
            f"{self.api}/threads/{thread_id}/navigation").json()

    def get_thread_poll_info(self, thread_id: int) -> dict:
        return self.session.get(
            f"{self.api}/threads/{thread_id}/poll").json()

    def vote_poll(
            self,
            thread_id: int,
            response_id: int,
            response_ids: str = None) -> dict:
        data = {
            "response_id": response_id
        }
        if response_ids:
            data["response_ids"] = response_ids
        return self.session.post(
            f"{self.api}/threads/{thread_id}/poll/votes", data=data).json()

    def get_poll_results(self, thread_id: int) -> dict:
        return self.session.get(
            f"{self.api}/threads/{thread_id}/poll/results").json()

    def get_new_threads(
            self,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None) -> dict:
        params = {
            "forum_id": forum_id,
            "data_limit": data_limit
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/threads/recent?limit={limit}",
            params=filtered_params).json()

    def get_recent_threads(
            self,
            days: int = None,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None) -> dict:
        params = {
            "days": days,
            "forum_id": forum_id,
            "data_limit": data_limit
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/threads/recent?limit={limit}",
            params=filtered_params).json()

    def get_thread_posts(
            self,
            thread_id: int = None,
            page_of_post_id: int = None,
            post_ids: str = None,
            page: int = None,
            limit: int = None,
            order: str = "natural") -> dict:
        params = {
            "thread_id": thread_id,
            "page_of_post_id": page_of_post_id,
            "post_ids": post_ids,
            "page": page,
            "limit": limit
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/posts?order={order}",
            params=filtered_params).json()

    def create_post(
            self,
            thread_id: int,
            quote_post_id: int = None,
            content: str = None) -> dict:
        data = {
            "thread_id": thread_id,
            "post_body": content
        }
        if quote_post_id:
            data["quote_post_id"] = quote_post_id
        return self.session.post(
            f"{self.api}/posts", data=data).json()

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
        return self.session.post(
            f"{self.api}/posts/attachments", data=data).json()

    def get_post_info(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}").json()

    def edit_post(
            self,
            post_id: int,
            content: str,
            thread_title: str = None,
            thread_prefix_id: int = None,
            thread_tags: str = None,
            thread_node_id: int = None) -> dict:
        data = {
            "post_body": content,
            "thread_title": thread_title,
            "thread_prefix_id": thread_prefix_id,
            "thread_tags": thread_tags,
            "thread_node_id": thread_node_id
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.put(
            f"{self.api}/posts/{post_id}", data=filtered_data).json()

    def delete_post(self, post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}").json()

    def get_post_attachments(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/attachments").json()

    def delete_post_attachment(self, post_id: int, attachment_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}/attachments/{attachment_id}").json()

    def get_post_likes(
            self,
            post_id: int,
            page: int = None,
            limit: int = 10) -> dict:
        params = {"page": page} if page else {}
        return self.session.get(
            f"{self.api}/posts/{post_id}/likes?limit={limit}",
            params=params).json()

    def like_post(self, post_id: int) -> dict:
        return self.session.post(
            f"{self.api}/posts/{post_id}/likes").json()

    def unlike_post(self, post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}/likes").json()

    def report_post(self, post_id: int, message: str) -> dict:
        data = {
            "message": message
        }
        return self.session.post(
            f"{self.api}/posts/{post_id}/report", data=data).json()

    def get_popular_tags(self) -> dict:
        return self.session.get(f"{self.api}/tags").json()

    def get_tags_list(self) -> dict:
        return self.session.get(f"{self.api}/tags/list").json()

    def get_tagged_content(
            self,
            tag_id: int,
            page: int = None,
            limit: int = 10) -> dict:
        params = {"page": page} if page else {}
        return self.session.get(
            f"{self.api}/tags/{tag_id}?limit={limit}",
            params=params).json()

    def get_filtered_tags_list(self, tag: str) -> dict:
        return self.session.get(
            f"{self.api}/tags/find?tag={tag}").json()

    def get_users_list(self, page: int = None, limit: int = 10) -> dict:
        params = {"page": page} if page else {}
        return self.session.get(
            f"{self.api}/users?limit={limit}", params=params).json()

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
        data = {
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
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/users", data=filtered_data).json()

    def get_user_fields(self) -> dict:
        return self.session.get(f"{self.api}/users/fields").json()

    def find_user(
            self, 
            username: str = None,
            user_email: str = None) -> dict:
        params = {
            "username": username,
            "user_email": user_email
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/users/find", params=filtered_params).json()

    def get_user_info(self, user_id: int) -> dict:
        return self.session.get(f"{self.api}/users/{user_id}").json()

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
        data = {
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
            "fields": fields,
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.put(
            f"{self.api}/users/{user_id}", data=filtered_data).json()

    def upload_avatar(self, user_id: int, file: BinaryIO) -> dict:
        data = {
            "avatar": file.read()
        }
        return self.session.post(
            f"{self.api}/users/{user_id}/avatar", data=data).json()

    def delete_avatar(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/{user_id}/avatar").json()

    def get_user_followers(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/users/{user_id}/followers").json()

    def follow_user(self, user_id: int) -> dict:
        return self.session.post(
            f"{self.api}/users/{user_id}/followers").json()

    def unfollow_user(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/{user_id}/followers").json()

    def get_user_followings(
            self,
            user_id: int,
            order: str = "natural",
            page: int = None,
            limit: int = None) -> dict:
        params = {
            "page": page,
            "limit": limit
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/users/{user_id}/followings?order={order}",
            params=filtered_params).json()

    def get_ignored_users(self) -> dict:
        return self.session.get(
            f"{self.api}/users/ignored").json()

    def ignore_user(self, user_id: int) -> dict:
        return self.session.post(
            f"{self.api}/users/{user_id}/ignore").json()

    def unignore_user(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/{user_id}/ignore").json()

    def get_all_user_groups(self) -> dict:
        return self.session.get(
            f"{self.api}/users/groups").json()

    def get_user_groups(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/users/{user_id}/groups").json()

    def get_current_user(self) -> dict:
        return self.session.get(f"{self.api}/users/me").json()

    def get_user_contents(
            self,
            user_id: int,
            page: int = None,
            limit: int = 10) -> dict:
        params = {"page": page} if page else {}
        return self.session.get(
            f"{self.api}/users/{user_id}/timeline?limit={limit}", params=params).json()

    def create_profile_post(self, user_id: int, post_body: str) -> dict:
        data = {
            "post_body": post_body
        }
        return self.session.post(
            f"{self.api}/users/{user_id}/timeline", data=data).json()

    def get_profile_post_info(
            self, profile_post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/profile-posts/{profile_post_id}").json()

    def edit_profile_post(
            self, profile_post_id: int, post_body: str) -> dict:
        data = {
            "post_body": post_body
        }
        return self.session.put(
            f"{self.api}/profile-posts/{profile_post_id}", data=data).json()

    def delete_profile_post(
            self, profile_post_id: int, reason: str = None) -> dict:
        params = {"reason": reason} if reason else {}
        return self.session.delete(
            f"{self.api}/profile-posts/{profile_post_id}",
            params=params).json()

    def get_profile_post_likes(
            self, profile_post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/profile-posts/{profile_post_id}/likes").json()

    def like_profile_post(self, profile_post_id: int) -> dict:
        return self.session.post(
            f"{self.api}/profile-posts/{profile_post_id}/likes").json()

    def unlike_profile_post(self, profile_post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/profile-posts/{profile_post_id}/likes").json()

    def get_profile_post_comments(
            self,
            profile_post_id: int,
            before: str = None,
            limit: int = 10) -> dict:
        params = {"before": before} if before else {}
        return self.session.get(
            f"{self.api}/profile-posts/{profile_post_id}/comments?limit={limit}",
            params=params).json()

    def comment_profile_post(
            self,
            profile_post_id: int,
            comment_body: str) -> dict:
        data = {
            "comment_body": comment_body
        }
        return self.session.post(
            f"{self.api}/profile-posts/{profile_post_id}/comments",
            data=data).json()

    def get_profile_post_comment(
            self,
            profile_post_id: int,
            comment_id: int) -> dict:
        return self.session.get(
            f"{self.api}/profile-posts/{profile_post_id}/comments/{comment_id}").json()

    def delete_profile_post_comment(
            self,
            profile_post_id: int,
            comment_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/profile-posts/{profile_post_id}/comments/{comment_id}").json()

    def report_profile_post(
            self,
            profile_post_id: int,
            message: str) -> dict:
        data = {
            "message": message
        }
        return self.session.post(
            f"{self.api}/profile-posts/{profile_post_id}/report",
            data=data).json()

    def get_conversations(
            self, page: int = None, limit: int = 10) -> dict:
        params  = {"page": page} if page else {}
        return self.session.get(
            f"{self.api}/conversations?limit={limit}",
            params=params).json()

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
        return self.session.post(
            f"{self.api}/conversations", data=data).json()

    def get_conversation_info(self, conversation_id: int) -> dict:
        return self.session.get(
            f"{self.api}/conversations/{conversation_id}").json()

    def delete_conversation(self, conversation_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/conversations/{conversation_id}").json()

    def upload_conversation_attachment(
            self,
            file: BinaryIO,
            attachment_hash: str = None) -> dict:
        data = {
            "file": file.read()
        }
        if attachment_hash:
            data["attachment_hash"] = attachment_hash
        return self.session.post(
            f"{self.api}/conversations/attachments", data=data).json()

    def delete_conversation_attachment(
            self,
            attachment_id: int,
            attachment_hash: str = None) -> dict:
        params = {"attachment_hash": attachment_hash} if attachment_hash else {}
        return self.session.delete(
            f"{self.api}/conversations/attachments?attachment_id={attachment_id}",
            params=params).json()

    def get_conversation_messages(
            self,
            conversation_id: int,
            page: int = None,
            limit: int = None,
            order: str = None,
            before: str = None,
            after: str = None) -> dict:
        params = {
            "page": page,
            "limit": limit,
            "order": order,
            "before": before,
            "after": after
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/conversation-messages?conversation_id={conversation_id}",
            params=filtered_params).json()

    def send_message(self, conversation_id: int, message: str) -> dict:
        data = {
            "conversation_id": conversation_id,
            "message_body": message
        }
        return self.session.post(
            f"{self.api}/conversation-message", data=data).json()

    def upload_message_attachment(
            self,
            file: BinaryIO,
            conversation_id: int = None,
            message_id: int = None,
            attachment_hash: str = None) -> dict:
        data = {
            "file": file.read()
        }
        if conversation_id:
            data["conversation_id"] = conversation_id
        elif message_id:
            data["message_id"] = message_id
        elif attachment_hash:
            data["attachment_hash"] = attachment_hash
        return self.session.post(
            f"{self.api}/conversation-messages/attachments", data=data).json()

    def get_message_info(self, message_id: int) -> dict:
        return self.session.get(
            f"{self.api}/conversation-messages/{message_id}").json()

    def edit_message(self, message_id: int, message_body: str) -> dict:
        data = {
            "message_body": message_body
        }
        return self.session.put(
            f"{self.api}/conversation-messages/{message_id}", data=data).json()

    def delete_message(self, message_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/conversation-messages/{message_id}").json()

    def get_message_attachments(self, message_id: int) -> dict:
        return self.session.get(
            f"{self.api}/conversation-messages/{message_id}/attachments").json()

    def delete_message_attachment(
            self,
            message_id: int,
            attachment_id: int,
            conversation_id: int = None,
            attachment_hash: str = None) -> dict:
        params = {
            "conversation_id": conversation_id,
            "attachment_hash": attachment_hash
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.delete(
            f"{self.api}/conversation-messages/{message_id}/attachments/{attachment_id}",
            params=filtered_params).json()

    def report_message(self, message_id: int, message: str) -> dict:
        data = {
            "message": message
        }
        return self.session.post(
            f"{self.api}/conversation-messages/{message_id}/report",
            data=data).json()

    def get_notifications(self) -> dict:
        return self.session.get(f"{self.api}/notifications").json()

    def get_notification_content(self, notification_id: int) -> dict:
        return self.session.get(
            f"{self.api}/notifications/{notification_id}/content").json()

    def send_custom_alert(
            self,
            user_id: int,
            message: str,
            notification_type: int = None,
            extra_data: str = None) -> dict:
        data = {
            "user_id": user_id,
            "message": message
        }
        if notification_type:
            data["notification_type"] = notification_type
        elif extra_data:
            data["extra_data"] = extra_data
        return self.session.post(
            f"{self.api}/notifications/custom",
            data=data).json()

    def mark_notification_read(self, notification_id: int = None) -> dict:
        data = {
            "notification_id": notification_id} if notification_id else {}
        return self.session.post(
            f"{self.api}/notifications/read", data=data).json()

    def search_threads(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None) -> dict:
        data = {
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/search/threads", data=filtered_data).json()

    def search_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None) -> dict:
        data = {
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/search/posts", data=filtered_data).json()

    def search_profile_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None) -> dict:
        data = {
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/search/profile-posts", data=filtered_data).json()

    def search(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None) -> dict:
        data = {
            "q": query,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": data_limit
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/search", data=filtered_data).json()

    def search_tagged(
            self,
            tag: str,
            tags: str = None,
            page: int = None,
            limit: int = None) -> dict:
        data = {
            "tag": tag,
            "tags": tags,
            "page": page,
            "limit": limit
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/search/tagged", data=filtered_data).json()
