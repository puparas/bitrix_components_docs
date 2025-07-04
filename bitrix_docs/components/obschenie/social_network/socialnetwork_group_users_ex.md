|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор группы |

| Параметр содержит код, в котором передается идентификатор группы социальной сети. |
| **Внешний вид** |

| |
| Количество записей в списке |

| Указывается количество найденных пользователей, отображаемых на одной странице. Все найденные пользователи будут выведены с помощью постраничной навигации. |
| Отображение имени |

| Указывается шаблон для отображения ФИО пользователя социальной сети. Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя |

| [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Размер картинки пользователя (px) |

| Указывается максимальный размер фотографии в списке пользователей в пикселях. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к странице группы |

| Задается путь к странице группы социальной сети. |
| Шаблон пути к странице изменения параметров группы |

| Задается путь к странице редактирования группы социальной сети. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции на странице будет установлена цепочка навигации вида **{Название группы} - Участники группы**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **{Название группы} - Участники группы**. |
| Использовать функционал черного списка в группах |

| [Y|N] При отмеченной опции будет использоваться функционал черного списка в рабочих группах. |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для группы |

| Указывается имя переменной, которой передается идентификатор группы социальной сети. |
| Имя переменной для пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.group_users.ex","",Array(

        "SET_NAV_CHAIN" => "Y", 

        "ITEMS_COUNT" => "20",

        "PATH_TO_USER" => "index.php?page=user&user_id=#user_id#", 

        "PATH_TO_GROUP" => "",		

        "PAGE_VAR" => "page", 

        "USER_VAR" => "user_id", 

        "ID" => "$id", 		

        "SET_TITLE" => "Y", 

        "NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",

        "SHOW_LOGIN" => "Y",

        "THUMBNAIL_LIST_SIZE" => "42"

	),

false        

);?>


```