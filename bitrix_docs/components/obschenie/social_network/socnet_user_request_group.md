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
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к странице группы |

| Задается путь к странице группы социальной сети. |
| Шаблон пути к странице запросов на вступление в группу |

| Задается путь к странице запросов на вступление в группу социальной сети. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт **Запрос на присоединение к группе**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **<имя\_группы> : Запрос на присоединение к группе**. |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для группы |

| Указывается имя переменной, которой передается идентификатор группы социальной сети. |
| Имя переменной для пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_request_group","",Array(

        "SET_NAVCHAIN" => "Y", 

        "PATH_TO_USER" => "/community/socnet/index.php?page=user&user_id=#user_id#", 

        "PATH_TO_GROUP" => "group_view.php?page=group&group_id=#group_id#", 

        "PAGE_VAR" => "page", 

        "GROUP_VAR" => "group_id", 

        "USER_VAR" => "user_id", 

        "GROUP_ID" => $group_id, 

        "SET_TITLE" => "Y"

    )

);?>


```