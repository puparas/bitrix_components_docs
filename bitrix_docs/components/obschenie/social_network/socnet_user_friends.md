|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор пользователя |

| Параметр содержит код, в котором передается идентификатор пользователя социальной сети. |
| **Внешний вид** |

| |
| Количество записей в списках |

| Указывается количество визиток друзей пользователя, отображаемых на одной странице. Все визитки будут выведены с помощью постраничной навигации. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к обновлениям |

| Задается путь к странице обновлений социальной сети. |
| Шаблон пути к странице добавления в друзья |

| Задается путь к странице добавления в друзья социальной сети. |
| Шаблон пути к странице удаления из друзей |

| Задается путь к странице удаления из друзей социальной сети. |
| Шаблон пути к странице поиска пользователей |

| Задается путь к странице поиска пользователей социальной сети. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт **Друзья**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **Друзья**. |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_friends","",Array(

        "SET_NAVCHAIN" => "Y", 

        "ITEMS_COUNT" => "30", 

        "PATH_TO_USER" => "index.php?page=user&user_id=#user_id#", 

        "PATH_TO_LOG" => "user_subscribe.php?page=subscribe&user_id=#user_id#", 

        "PATH_TO_USER_FRIENDS_ADD" => "user_friends_add.php?page=user_friends_add&user_id=#user_id#", 

        "PATH_TO_USER_FRIENDS_DELETE" => "user_friends_delete.php?page=user_friends_delete&user_id=#user_id#", 

        "PATH_TO_SEARCH" => "user_search.php", 

        "PAGE_VAR" => "page", 

        "USER_VAR" => "user_id", 

        "ID" => $user_id, 

        "SET_TITLE" => "Y" 

    )

);?>


```