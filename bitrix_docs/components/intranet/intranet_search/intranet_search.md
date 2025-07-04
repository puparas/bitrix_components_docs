|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Страница структуры компании |

| Указывается путь к странице структуры компании. |
| Страница отправки личного сообщения |

| Указывается путь к странице отправки личного сообщения. |
| Шаблон пути к странице подразделения |

| Указывается шаблон пути к странице подразделения компании. |
| Имя фильтра страницы структуры компании |

| Указывается имя фильтра страницы структуры компании. |
| Выводить только синхронизируемых с 1С пользователей |

| [Y|N] При отмеченной опции будут выводиться только синхронизируемые с 1С пользователи. |
| Количество пользователей на страницу |

| Поле определяет количество пользователей, отображаемых на одной странице. Весь список будет отображен с помощью постраничной навигации. |
| Фильтр по подразделениям |

| Указывается тип фильтра по подразделениям:  * **прямой** (**Y**); * **рекурсивный** (**N**). |
| Отображение имени |

| Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя |

| [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Выводить уведомление при пустом списке |

| [Y|N] При отмеченной опции выводится уведомление при пустом списке. |
| Отображать фильтр по алфавиту на языках |

| Задаются языки для показа фильтра по алфавиту. |
| Подпись постраничной навигации |

| Поле содержит подпись для постраничной навигации. |
| Показывать постраничную навигацию над списком |

| [Y|N] При отмеченной опции постраничная навигация будет показываться над списком. |
| Показывать постраничную навигацию под списком |

| [Y|N] При отмеченной опции постраничная навигация будет показываться под списком. |
| Показывать список при пустом фильтре |

| [Y|N] При отмеченной опции будет выведен весь список сотрудников. Если опция не отмечена, то будет показана только форма поиска. |
| **Управление режимом AJAX** |

| |
| Включить режим AJAX |

| [Y|N] При отмеченной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента |

| [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей |

| [Y|N] Если параметр принимает значение **Y**, то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера |

| [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Формат показа даты |

| Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат показа даты без года |

| Указывается формат показа даты без года. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат показа даты и времени |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты и времени, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Показывать год рождения |

| Поле определяет кому показываеть год рождения:  * **всем** (**Y**); * **только мужчинам** (**M**); * **никому** (**N**). |
| Страница видеозвонка |

| Указывается шаблон пути к видеозвонку. |
| Показывать переключатель представления |

| [Y|N] При отмеченной опции на странице поиска будет показываться переключатель вывода результатов. |
| Представление по умолчанию |

| Указывается способ вывода результатов поиска по умолчанию:  * **список** (**list**); * **таблица** (**table**). |
| Шаблон для представления в виде списка |

| Указывается способ для представления в виде списка:  * **простой список** (**list**); * **с группировкой по отделам** (**group**).    Если параметр принимает значение **group**, то необходимо настроить следущий параметр: **USER\_PROPERTY\_GROUP**. |
| Шаблон для представления в виде таблицы |

| Указывается способ для представления в виде списка:  * **простой список** (**list**); * **с группировкой по отделам** (**group**). |
| Пользовательские поля для вывода в табличном представлении |

| Указываются поля, которые должны быть отображены при выводе списка пользователей в табличном представлении. |
| Пользовательские поля для вывода в формате Excel |

| Указываются поля пользователей, которые должны быть выгружены при выполнении экспорта пользователей в MS Excel. |
| Пользовательские поля для вывода в представлении в виде списка |

| Указываются поля, которые должны быть отображены при выводе пользователей в виде простого списка. |
| **Параметры фильтра** |

| |
| Имя фильтра (для внешних форм фильтрации) |

| Указывается имя фильтра (для внешних форм фильтрации). |
| Выбор подразделения для фильтрации |

| Указывается способ выбора подразделения(ий) в форме поиска:  * **одинарный** (**Y**) - в выпадающем списке можно выбрать только одно подразделение; * **множественный** (**N**) - поле позволяет выбирать несколько подразделений. |
| Запоминать фильтр в сессии |

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.search","",Array(

		"DEFAULT_VIEW" => "table",

		"LIST_VIEW" => "list",

		"USER_PROPERTY_TABLE" => Array("FULL_NAME", "EMAIL", "PERSONAL_PHONE", "WORK_POSITION", "UF_DEPARTMENT"),

		"USER_PROPERTY_EXCEL" => Array("FULL_NAME", "EMAIL", "PERSONAL_PHONE", "WORK_POSITION", "UF_DEPARTMENT"),

		"AJAX_MODE" => "Y",

		"STRUCTURE_PAGE" => "structure.php",

		"PM_URL" => "/messages/form/#USER_ID#/",

		"PATH_TO_CONPANY_DEPARTMENT" => "/company/structure.php?set_filter_structure=Y&structure_UF_DEPARTMENT=#ID#",

		"STRUCTURE_FILTER" => "structure",

		"FILTER_1C_USERS" => "Y",

		"FILTER_NAME" => "users",

		"USERS_PER_PAGE" => "20",

		"FILTER_DEPARTMENT_SINGLE" => "N",

		"FILTER_SESSION" => "Y",

		"FILTER_SECTION_CURONLY" => "N",

		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",

		"SHOW_LOGIN" => "Y",

		"SHOW_ERROR_ON_NULL" => "Y",

		"ALPHABET_LANG" => array("ru"),

		"NAV_TITLE" => "Сотрудники",

		"SHOW_NAV_TOP" => "Y",

		"SHOW_NAV_BOTTOM" => "Y",

		"SHOW_UNFILTERED_LIST" => "Y",

		"DATE_FORMAT" => "d.m.Y",

		"DATE_FORMAT_NO_YEAR" => "d.m",

		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",

		"SHOW_YEAR" => "Y",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"PATH_TO_VIDEO_CALL" => "/company/personal/video/#USER_ID#/",

		"AJAX_OPTION_JUMP" => "N",

		"AJAX_OPTION_STYLE" => "Y",

		"AJAX_OPTION_HISTORY" => "N"

	),

);?>


```