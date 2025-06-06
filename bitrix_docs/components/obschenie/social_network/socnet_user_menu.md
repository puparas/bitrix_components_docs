|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор пользователя |

| Параметр содержит код, в котором передается идентификатор пользователя социальной сети. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к странице добавления в друзья |

| Задается путь к странице добавления в друзья социальной сети. |
| Шаблон пути к странице входящих сообщений |

| Задается путь к странице входящих сообщений социальной сети. |
| Шаблон пути к странице отправки сообщений |

| Задается путь к странице отправки сообщений социальной сети. |
| Шаблон пути к странице удаления из друзей |

| Задается путь к странице удаления из друзей социальной сети. |
| Шаблон пути к странице друзей пользователя |

| Задается путь к странице друзей пользователя социальной сети. |
| Шаблон пути к странице поиска пользователей |

| Задается путь к странице поиска пользователей социальной сети. |
| Шаблон пути к странице добавления групп |

| Задается путь к странице добавления групп социальной сети. |
| Шаблон пути к странице групп пользователя |

| Задается путь к странице групп пользователя социальной сети. |
| Шаблон пути к странице редактирования пользователя |

| Задается путь к странице редактирования пользователя социальной сети. |
| Шаблон пути к странице блога пользователя |

| Задается путь к странице блога пользователя социальной сети. |
| Шаблон пути к странице фото пользователя |

| Задается путь к странице фото пользователя социальной сети. |
| Шаблон пути к странице форума пользователя |

| Задается путь к странице форума пользователя социальной сети. |
| Шаблон пути к странице календаря пользователя |

| Задается путь к странице календаря пользователя социальной сети. |
| Шаблон пути к странице задач пользователя |

| Задается путь к странице задач пользователя социальной сети. |
| Шаблон пути к странице файлов пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_menu",".default",Array(

        "PATH_TO_USER" => "index.php?page=user&user_id=#user_id#", 

        "PATH_TO_USER_FRIENDS_ADD" => "user_friends_add.php?page=user_friends_add&user_id=#user_id#", 

        "PATH_TO_MESSAGES_INPUT" => "messages_input.php?page=messages_input&user_id=#user_id#", 

        "PATH_TO_MESSAGE_FORM" => "message_form.php?page=message_form&user_id=#user_id#", 

        "PATH_TO_USER_FRIENDS_DELETE" => "user_friends_delete.php?page=user_friends_delete&user_id=#user_id#", 

        "PATH_TO_USER_FRIENDS" => "user_friends.php?page=user_friends&user_id=#user_id#", 

        "PATH_TO_SEARCH" => "user_search.php", 

        "PATH_TO_USER_GROUPS_ADD" => "group_add.php?page=create&user=#user_id#", 

        "PATH_TO_USER_GROUPS" => "user_groups.php?page=user_groups&user=#user_id#", 

        "PATH_TO_USER_EDIT" => "user_edit.php?page=user_edit&user_id=#user_id#", 

        "PATH_TO_USER_BLOG" => "user_blog.php?page=user_blog&user_id=#user_id#", 

        "PATH_TO_USER_PHOTO" => "user_photo.php?page=user_photo&user_id=#user_id#", 

        "PATH_TO_USER_FORUM" => "user_forum.php?page=user_forum&user_id=#user_id#", 

        "PATH_TO_USER_CALENDAR" => "user_calendar.php?page=user_calendar&user_id=#user_id#",

        "PATH_TO_USER_TASKS" => "", 

        "PATH_TO_USER_FILES" => "user_files.php?page=user_files&user_id=#user_id#", 

        "PAGE_VAR" => "page", 

        "USER_VAR" => "user_id", 

        "ID" => $user_id 

    )

);?>


```