|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор сообщения |

| Параметр содержит код, в котором передается идентификатор сообщения. |
| **Внешний вид** |

| |
| Формат показа даты и времени |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт *(другое)->*, можно сформировать свой вариант на основании php-функции **date**. |
| Максимальная ширина изображения |

| Указывается максимальная ширина изображения, вставляемого в сообщение (в пикселах). |
| Максимальная высота изображения |

| Указывается максимальная высота изображения, вставляемого в сообщение (в пикселах). |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице сообщений |

| Задается путь к главной странице конкретного сообщения социальной сети. |
| Шаблон пути к странице сообщения c фильтром по тегу |

| Задается путь к главной странице сообщения социальной сети c фильтром по тегу. |
| Шаблон пути к странице редактирования сообщения |

| Задается путь к странице редактирования сообщения блога социальной сети. |
| Шаблон пути к странице пользователя |

| Задается путь к странице пользователя социальной сети. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Путь к папке со смайликам относительно корня сайта |

| Указывается путь к папке со смайлами относительно корня сайта. По умолчанию поле содержит */bitrix/images/socialnetwork/smile/*. |
| Добавлять пункт в цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт с названием блога. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено название сообщения в социальной сети. |
| Показывать доп. свойства сообщения |

| Указываются пользовательские свойства сообщения, которые необходимо дополнительно отобразить в социальной сети. |
| Включить рейтинг |

| Указывается включать ли вывод рейтинга:  * - по умолчанию; * **Y** - да; * **N** - нет. |
| Вид кнопок рейтинга |

| Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |
| **Имена переменных** |

| |
| Имя переменной для идентификатора сообщения |

| Указывается имя переменной, которой передается идентификатор сообщения блога социальной сети. |
| Имя переменной для идентификатора пользователя |

| Указывается имя переменной, которой передается идентификатор пользователя блога социальной сети. |
| Имя переменной для страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.blog.post","",Array(

	"ID" => $id, 

	"DATE_TIME_FORMAT" => "d.m.Y H:i:s", 

	"PATH_TO_BLOG" => "blog_blog.php?page=blog&blog=#blog#", 

	"PATH_TO_BLOG_CATEGORY" => "blog_filter.php?page=blog&blog=#blog#&category=#category#", 

	"PATH_TO_POST_EDIT" => "blog_p_edit.php?page=post_edit&blog=#blog#&post_id=#post_id#", 

	"PATH_TO_USER" => "blog_user.php?page=user&user_id=#user_id#", 

	"PATH_TO_SMILE" => "/bitrix/images/blog/smile/", 

	"POST_VAR" => "post_id", 

	"USER_VAR" => "user_id", 

	"PAGE_VAR" => "page", 

	"CACHE_TYPE" => "A", 

	"CACHE_TIME" => "7200", 

	"SET_NAV_CHAIN" => "Y", 

	"SET_TITLE" => "Y", 

	"NAV_TEMPLATE" => "",

	"SHOW_RATING" => "Y", 

	"POST_PROPERTY" => Array() 

	"RATING_TYPE" => "",

	"IMAGE_MAX_WIDTH" => "600",

	"IMAGE_MAX_HEIGHT" => "600"

	)

);?>


```