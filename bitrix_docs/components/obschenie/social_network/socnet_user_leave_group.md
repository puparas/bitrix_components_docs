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
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт **Группы**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **<имя\_группы> : Выход из группы**. |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для пользователя |

| Указывается имя переменной, которой передается идентификатор пользователя социальной сети. |
| Имя переменной для группы |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_leave_group","",Array(

        "SET_NAVCHAIN" => "Y", 

        "PATH_TO_USER" => "/community/socnet/index.php?page=user&user_id=#user_id#", 

        "PATH_TO_GROUP" => "group_view.php?page=group&group_id=#group_id#", 

        "PAGE_VAR" => "page", 

        "USER_VAR" => "user_id", 

        "GROUP_VAR" => "group_id", 

        "GROUP_ID" => $group_id, 

        "SET_TITLE" => "Y" 

    )

);?>


```