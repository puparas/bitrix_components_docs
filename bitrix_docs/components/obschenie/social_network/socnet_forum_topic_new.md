|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID форума |

| Указывается идентификатор форума социальной сети, в котором будут храниться темы и сообщения пользователей. |
| ID сообщения |

| Указывается идентификатор сообщения форума социальной сети. |
| Действие над сообщением |

| Указывается имя переменной, в которой будет содержаться код действия над сообщением. |
| ID группы |

| Указывается идентификатор рабочей группы социальной сети. |
| ID пользователя |

| Указывается идентификатор пользователя социальной сети. |
| **Шаблоны ссылок** |

| |
| Страница списка тем |

| Указывается путь к странице со списком тем форума социальной сети. |
| Страница чтения сообщения |

| Указывается путь к странице чтения сообщения социальной сети. |
| Страница профиля пользователя |

| Указывается путь к странице профиля пользователя социальной сети. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Путь относительно корня сайта к папке со смайлами |

| Указывается путь к папке со смайлами относительно корня сайта. По умолчанию поле содержит **/bitrix/images/forum/smile/**. |
| Путь относительно корня сайта к папке с иконками к темам |

| Указывается путь к папке с иконками к темам относительно корня сайта. По умолчанию поле содержит **/bitrix/images/forum/icon/**. |
| Формат показа даты и времени |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Использовать аякс |

| [Y|N] При отмеченной опции для компонента будет включен режим AJAX. |
| Устанавливать заголовок страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.forum.topic.new","",Array(

	"SHOW_TAGS" => "Y", 

	"FID" => "3", 

	"MID" => $_REQUEST["MID"], 

	"MESSAGE_TYPE" => $_REQUEST["MESSAGE_TYPE"], 

	"SOCNET_GROUP_ID" => $_REQUEST["SOCNET_GROUP_ID"], 

	"USER_ID" => $_REQUEST["USER_ID"], 

	"URL_TEMPLATES_TOPIC_LIST" => "topic_list.php", 

	"URL_TEMPLATES_MESSAGE" => "message.php?TID=#TID#&MID=#MID#", 

	"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#", 

	"PATH_TO_SMILE" => "/bitrix/images/forum/smile/", 

	"PATH_TO_ICON" => "/bitrix/images/forum/icons/", 

	"DATE_TIME_FORMAT" => "d.m.Y H:i:s", 

	"AJAX_TYPE" => "Y", 

	"CACHE_TYPE" => "A", 

	"CACHE_TIME" => "0", 

	"SET_TITLE" => "Y" 

	),

);?>


```