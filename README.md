# <img src="https://user-images.githubusercontent.com/77536370/217814702-adbdc1d5-dd6f-42e2-a8e3-cda9f428eb51.svg" width="28" style="vertical-align:middle;" /> lolzteam.py

> Web-API for [Lolz.guru](https://lolz.guru) a large Russian-speaking forum and social platform with threads, posts, conversations, profiles, and more.

## Quick Start
```python
from lolzteam import Lolzteam

lolz = Lolzteam(token="your_token_here")

# Get current user
lolz.get_current_user()

# Search threads
lolz.search_threads(query="python")
```

---

## Categories & Forums

| Method | Description |
|--------|-------------|
| `get_categories(parent_category_id, parent_forum_id, order)` | List categories |
| `get_category_info(category_id)` | Get a category by ID |
| `get_forums(parent_category_id, parent_forum_id, order)` | List forums |
| `get_forum_info(forum_id)` | Get a forum by ID |
| `get_forum_followers(forum_id)` | Get forum followers |
| `follow_forum(forum_id, post, alert, email)` | Follow a forum |
| `unfollow_forum(forum_id)` | Unfollow a forum |

---

## Pages & Navigation

| Method | Description |
|--------|-------------|
| `get_pages(parent_page_id, order)` | List pages |
| `get_page_info(page_id)` | Get a page by ID |
| `get_navigation(parent_element_id)` | Get navigation tree |

---

## Threads

| Method | Description |
|--------|-------------|
| `get_threads_list(forum_id, thread_ids, ...)` | List threads with filters |
| `create_thread(forum_id, thread_title, content, ...)` | Create a new thread |
| `get_thread_info(thread_id)` | Get thread details |
| `delete_thread(thread_id)` | Delete a thread |
| `get_thread_followers(thread_id)` | Get thread followers |
| `follow_thread(thread_id, email)` | Follow a thread |
| `unfollow_thread(thread_id)` | Unfollow a thread |
| `get_thread_navigation(thread_id)` | Get thread navigation |
| `get_new_threads(limit, forum_id, data_limit)` | Get new threads |
| `get_recent_threads(days, limit, forum_id, data_limit)` | Get recently active threads |
| `upload_thread_attachment(forum_id, file, attachment_hash)` | Upload a thread attachment |
| `delete_thread_attachment(forum_id, attachment_id, attachment_hash)` | Delete a thread attachment |

---

## Polls

| Method | Description |
|--------|-------------|
| `get_thread_poll_info(thread_id)` | Get poll for a thread |
| `vote_poll(thread_id, response_id, response_ids)` | Vote on a poll |
| `get_poll_results(thread_id)` | Get poll results |

---

## Posts

| Method | Description |
|--------|-------------|
| `get_thread_posts(thread_id, ...)` | Get posts in a thread |
| `create_post(thread_id, quote_post_id, content)` | Create a post |
| `get_post_info(post_id)` | Get a post by ID |
| `edit_post(post_id, content, ...)` | Edit a post |
| `delete_post(post_id)` | Delete a post |
| `get_post_attachments(post_id)` | Get post attachments |
| `delete_post_attachment(post_id, attachment_id)` | Delete a post attachment |
| `upload_post_attachment(file, thread_id, post_id, attachment_hash)` | Upload a post attachment |
| `get_post_likes(post_id, page, limit)` | Get post likes |
| `like_post(post_id)` | Like a post |
| `unlike_post(post_id)` | Unlike a post |
| `report_post(post_id, message)` | Report a post |

---

## Tags

| Method | Description |
|--------|-------------|
| `get_popular_tags()` | Get popular tags |
| `get_tags_list()` | Get full tag list |
| `get_tagged_content(tag_id, page, limit)` | Get content by tag |
| `get_filtered_tags_list(tag)` | Search tags by name |

---

## Users

| Method | Description |
|--------|-------------|
| `get_current_user()` | Get authenticated user info |
| `get_user_info(user_id)` | Get a user's profile |
| `get_users_list(page, limit)` | List all users |
| `find_user(username, user_email)` | Find a user by name or email |
| `register(email, username, password, ...)` | Register a new account |
| `edit_user(user_id, ...)` | Edit a user profile |
| `get_user_fields()` | Get available profile fields |
| `upload_avatar(user_id, file)` | Upload a user avatar |
| `delete_avatar(user_id)` | Delete a user avatar |
| `get_user_followers(user_id)` | Get user followers |
| `follow_user(user_id)` | Follow a user |
| `unfollow_user(user_id)` | Unfollow a user |
| `get_user_followings(user_id, order, page, limit)` | Get who a user follows |
| `get_ignored_users()` | Get ignored users list |
| `ignore_user(user_id)` | Ignore a user |
| `unignore_user(user_id)` | Unignore a user |
| `get_all_user_groups()` | Get all user groups |
| `get_user_groups(user_id)` | Get groups for a user |
| `get_user_contents(user_id, page, limit)` | Get user timeline |

---

## Profile Posts

| Method | Description |
|--------|-------------|
| `create_profile_post(user_id, post_body)` | Post on a user's profile |
| `get_profile_post_info(profile_post_id)` | Get a profile post |
| `edit_profile_post(profile_post_id, post_body)` | Edit a profile post |
| `delete_profile_post(profile_post_id, reason)` | Delete a profile post |
| `get_profile_post_likes(profile_post_id)` | Get profile post likes |
| `like_profile_post(profile_post_id)` | Like a profile post |
| `unlike_profile_post(profile_post_id)` | Unlike a profile post |
| `get_profile_post_comments(profile_post_id, before, limit)` | Get profile post comments |
| `comment_profile_post(profile_post_id, comment_body)` | Comment on a profile post |
| `get_profile_post_comment(profile_post_id, comment_id)` | Get a specific comment |
| `delete_profile_post_comment(profile_post_id, comment_id)` | Delete a comment |
| `report_profile_post(profile_post_id, message)` | Report a profile post |

---

## Conversations

| Method | Description |
|--------|-------------|
| `get_conversations(page, limit)` | List conversations |
| `create_conversation(conversation_title, recipients, content)` | Start a new conversation |
| `get_conversation_info(conversation_id)` | Get conversation details |
| `delete_conversation(conversation_id)` | Delete a conversation |
| `upload_conversation_attachment(file, attachment_hash)` | Upload conversation attachment |
| `delete_conversation_attachment(attachment_id, attachment_hash)` | Delete conversation attachment |

---

## Messages

| Method | Description |
|--------|-------------|
| `get_conversation_messages(conversation_id, ...)` | Get messages in a conversation |
| `send_message(conversation_id, message)` | Send a message |
| `get_message_info(message_id)` | Get a message by ID |
| `edit_message(message_id, message_body)` | Edit a message |
| `delete_message(message_id)` | Delete a message |
| `get_message_attachments(message_id)` | Get message attachments |
| `delete_message_attachment(message_id, attachment_id, ...)` | Delete a message attachment |
| `upload_message_attachment(file, ...)` | Upload a message attachment |
| `report_message(message_id, message)` | Report a message |

---

## Notifications

| Method | Description |
|--------|-------------|
| `get_notifications()` | Get all notifications |
| `get_notification_content(notification_id)` | Get notification content |
| `send_custom_alert(user_id, message, ...)` | Send a custom alert |
| `mark_notification_read(notification_id)` | Mark notification as read |

---

## Search

| Method | Description |
|--------|-------------|
| `search(query, ...)` | Global search |
| `search_threads(query, ...)` | Search threads |
| `search_posts(query, ...)` | Search posts |
| `search_profile_posts(query, ...)` | Search profile posts |
| `search_tagged(tag, tags, page, limit)` | Search by tag |
