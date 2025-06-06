|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор группы |

| Параметр содержит код, в котором передается идентификатор группы социальной сети. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице группы |

| Задается путь к странице группы социальной сети. |
| Шаблон пути к странице руководства группы |

| Задается путь к странице модераторов группы социальной сети. |
| Шаблон пути к странице членов группы |

| Задается путь к странице членов группы социальной сети. |
| Шаблон пути к странице редактирования группы |

| Задается путь к странице редактирования группы социальной сети. |
| Шаблон пути к странице приглашения пользователей в группу |

| Задается путь к странице приглашения пользователей в группу социальной сети. |
| Шаблон пути к странице черного списка пользователей |

| Задается путь к странице черного списка пользователей группы социальной сети. |
| Шаблон пути к странице запросов пользователей на вступление |

| Задается путь к странице запросов пользователей на вступление в группу социальной сети. |
| Шаблон пути к странице блога группы |

| Задается путь к странице блога группы социальной сети. |
| Шаблон пути к странице фото группы |

| Задается путь к странице фото группы социальной сети. |
| Шаблон пути к странице форума группы |

| Задается путь к странице форума группы социальной сети. |
| Шаблон пути к странице календаря группы |

| Задается путь к странице календаря группы социальной сети. |
| Шаблон пути к странице задач группы |

| Задается путь к странице задач группы социальной сети. |
| Шаблон пути к странице файлов группы |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.group_menu",".default",Array(

        "PATH_TO_GROUP" => "group_view.php?page=group&group_id=#group_id#", 

        "PATH_TO_GROUP_MODS" => "group_mods.php?page=group_mods&group_id=#group_id#", 

        "PATH_TO_GROUP_USERS" => "group_users.php?page=group_users&group_id=#group_id#", 

        "PATH_TO_GROUP_EDIT" => "group_edit.php?page=group_edit&group_id=#group_id#", 

        "PATH_TO_GROUP_REQUEST_SEARCH" => "group_invite.php?page=group_request_search&group_id=#group_id#", 

        "PATH_TO_GROUP_BAN" => "group_ban.php?page=group_ban&group_id=#group_id#", 

        "PATH_TO_GROUP_REQUESTS" => "group_requests.php?page=group_requests&group_id=#group_id#", 

        "PATH_TO_GROUP_BLOG" => "group_blog.php?page=group_blog&group_id=#group_id#", 

        "PATH_TO_GROUP_PHOTO" => "group_photo.php?page=group_photo&group_id=#group_id#", 

        "PATH_TO_GROUP_FORUM" => "group_forum.php?page=group_forum&group_id=#group_id#", 

        "PATH_TO_GROUP_CALENDAR" => "group_calendar.php?page=group_calendar&group_id=#group_id#",

        "PATH_TO_GROUP_TASK" => "group_task.php?page=group_task&group_id=#group_id#",

        "PATH_TO_GROUP_FILES" => "group_files.php?page=group_files&group_id=#group_id#", 

        "PAGE_VAR" => "page", 

        "GROUP_VAR" => "group_id", 

        "GROUP_ID" => $group_id 

    )

);?>


```