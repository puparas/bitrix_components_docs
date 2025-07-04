|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор группы |

| Указывается код, в котором передается идентификатор группы блога. |
| **Внешний вид** |

| |
| Количество блогов, выводимых на страницу |

| Указывается количество блогов, отображаемых на странице. |
| Формат показа даты и времени |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Показывать блоги без сообщений |

| [Y|N] При отмеченной опции будут показаны блоги, которые не имеют сообщений. |
| Имя шаблона для постраничной навигации |

| Указывается имя шаблона для постраничной навигации. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице блога |

| Указывается путь к главной странице блога. |
| Шаблон пути к странице с сообщением блога |

| Указывается путь к странице детального просмотра сообщения блога. |
| Шаблон пути к странице пользователя блога |

| Указывается путь к странице профиля пользователя блога. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **<имя\_группы>** блогов. |
| Запретить индексацию ссылки на профиль пользователя поисковыми ботами |

| [Y|N] При отмеченной опции поисковые боты не смогут индексировать ссылки на профиль пользователя. |
| **Имена переменных** |

| |
| Имя переменной для идентификатора блога |

| Указывается имя переменной, которой передается идентификатор блога. |
| Имя переменной для идентификатора сообщения блога |

| Указывается имя переменной, которой передается идентификатор сообщения блога. |
| Имя переменной для идентификатора пользователя блога |

| Указывается имя переменной, которой передается идентификатор пользователя блога. |
| Имя переменной для страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:blog.group.blog","",Array(

		"SEO_USER" => "Y",

		"BLOG_COUNT" => "20",

		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",

		"PATH_TO_BLOG" => "blog_blog.php?page=blog&blog=#blog#",

		"PATH_TO_POST" => "blog_post.php?page=post&blog=#blog#&post_id=#post_id#",

		"PATH_TO_USER" => "blog_user.php?page=user&user_id=#user_id#",

		"BLOG_VAR" => "blog",

		"POST_VAR" => "post_id",

		"USER_VAR" => "user_id",

		"PAGE_VAR" => "page",

		"ID" => $id,

		"SHOW_BLOG_WITHOUT_POSTS" => "Y",

		"NAV_TEMPLATE" => "",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "86400",

		"SET_TITLE" => "Y"

	),

);?>


```