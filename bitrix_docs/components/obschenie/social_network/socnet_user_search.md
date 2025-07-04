|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Внешний вид** |

| |
| Число записей на страницу |

| Указывается количество найденных пользователей, отоброжаемых на одной странице. Все найденные пользователи будут выведены с помощью постраничной навигации. |
| Формат даты |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к странице поиска пользователей |

| Задается путь к странице поиска пользователей социальной сети. |
| Шаблон пути к внутренней странице поиска пользователей |

| Задается путь к внутренней странице поиска пользователей социальной сети. |
| Шаблон пути к странице добавления в друзья |

| Задается путь к странице добавления в друзья социальной сети. |
| Шаблон пути к странице отправки сообщений |

| Задается путь к странице отправки сообщений социальной сети. |
| Шаблон пути к странице чата |

| Задается путь к странице чата социальной сети. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт **Поиск пользователей**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **Поиск пользователей**. |
| Выбирать пользователей без заданного фильтра |

| [Y|N] При отмеченной опции на странице будут отображен список пользователей. |
| Поля пользователя для простой формы поиска |

| Указываются свойства пользователя, которые должны быть отображены на простой форме поиска сотрудника. |
| Пользовательские свойства пользователя для простой формы поиска |

| Указываются дополнительные свойства пользователя, которые также должны быть отображены на простой форме поиска сотрудника. |
| Поля пользователя для расширенной формы поиска |

| Указываются свойства пользователя, которые должны быть отображены на расширенной форме поиска сотрудника. |
| Пользовательские свойства пользователя для расширенной формы поиска |

| Указываются дополнительные свойства пользователя, которые также должны быть отображены на расширенной форме поиска сотрудника. |
| Поля пользователя для вывода в списке |

| Указываются поля пользователя, которые должны быть отображены при показе списка сотрудников. |
| Пользовательские свойства пользователя для вывода в списке |

| Указываются дополнительные свойства пользователя, которые также должны быть отображены при показе списка сотрудников. |
| Поля пользователя, по которым возможен поиск |

| Указываются поля пользователя, по которым будет осуществляться поиск сотрудников. |
| Пользовательские свойства пользователя, по которым возможен поиск |

| Указываются дополнительные свойства пользователя, по которым также будет осуществляться поиск сотрудников. |
| Показывать год рождения |

| Параметр определяет для каких сотрудников должен быть отображен год рождения:  * **Y** - всем; * **M** - только мужчинам; * **N** - никому. |
| Учитывать рейтинг в сортировке |

| [Y|N] При отмеченной опции при выводе поискового запроса по пользователям будет учитываться их рейтинг. |
| Включить рейтинг |

| Указывается включать ли вывод рейтинга:  * - по умолчанию; * **Y** - да; * **N** - нет. |
| Рейтинг |

| Указывается какой будет использоваться рейтинг. |
| Вид кнопок рейтинга |

| Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_search","",Array(

        "SET_NAVCHAIN" => "Y", 

        "PAGE_VAR" => "page", 

        "USER_VAR" => "user_id", 

        "PATH_TO_USER" => "index.php?page=user&user_id=#user_id#", 

        "PATH_TO_SEARCH" => "/company/index.php", 

        "PATH_TO_SEARCH_INNER" => "user_search.php", 

        "PATH_TO_USER_FRIENDS_ADD" => "user_friends_add.php?page=user_friends_add&user_id=#user_id#", 

        "PATH_TO_MESSAGE_FORM" => "message_form.php?page=message_form&user_id=#user_id#", 

        "PATH_TO_MESSAGES_CHAT" => "messages_chat.php?page=messages_chat&user_id=#user_id#", 

        "ITEMS_COUNT" => "10", 

        "DATE_TIME_FORMAT" => "d.m.Y H:i:s", 

        "SET_TITLE" => "Y", 

        "USER_FIELDS_SEARCH_SIMPLE" => Array(), 

        "SHOW_USERS_WITHOUT_FILTER_SET" => "N",

        "USER_PROPERTIES_SEARCH_SIMPLE" => Array("UF_DEPARTMENT"), 

        "USER_FIELDS_SEARCH_ADV" => Array("EMAIL"), 

        "USER_PROPERTIES_SEARCH_ADV" => Array("UF_DEPARTMENT"), 

        "USER_FIELDS_LIST" => Array("NAME","SECOND_NAME","LAST_NAME","EMAIL"), 

        "USER_PROPERTIES_LIST" => Array("UF_DEPARTMENT"), 

        "SONET_USER_FIELDS_SEARCHABLE" => Array("NAME","SECOND_NAME","LAST_NAME","EMAIL"), 

        "SONET_USER_PROPERTY_SEARCHABLE" => Array(), 

        "SHOW_YEAR" => "Y",

        "CACHE_TYPE" => "A",

        "CACHE_TIME" => "3600"

        "SHOW_RATING" => "Y",

        "RATING_ID" => array(),

    )

);?>


```