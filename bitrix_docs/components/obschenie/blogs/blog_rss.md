|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Путь блога |

| Поле содержит код, в котором передается идентификатор блога. |
| Идентификатор сообщения блога |

| Поле содержит код, в котором передается идентификатор сообщения блога. |
| **Внешний вид** |

| |
| Количество сообщений |

| Указывается число сообщений блогов, данные из которых будут выгружены в соответствующем формате. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице блога |

| Указывается путь к главной странице блога. |
| Шаблон пути к странице с сообщением блога |

| Указывается шаблон пути к странице просмотра сообщения блога. |
| Шаблон пути к странице пользователя блога |

| Указывается шаблон пути к странице профиля пользователя блога. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Формат RSS |

| Указывается формат экспорта данных:  * **rss1** - формат RSS .92; * **rss2** - формат RSS 2.0; * **atom** - формат Atom .03;  либо тип экспорта указывается с помощью кода. |
| Отдавать в RSS |

| Укажите данные, из которых будет формироваться RSS: сообщения (**P**) или комментарии (**C**) блога. |
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
<?$APPLICATION->IncludeComponent("bitrix:blog.rss","",Array(

		"MESSAGE_COUNT" => "10",

		"PATH_TO_BLOG" => "blog_blog.php?page=blog&blog=#blog#",

		"PATH_TO_POST" => "blog_post.php?page=post&blog=#blog#&post_id=#post_id#",

		"PATH_TO_USER" => "blog_user.php?page=user&user_id=#iser_id#",

		"BLOG_VAR" => "blog",

		"POST_VAR" => "post_id",

		"USER_VAR" => "user_id",

		"PAGE_VAR" => "page",

		"BLOG_URL" =>$blog,

		"POST_ID" => $post_id,

		"TYPE" => "rss2",

		"MODE" => "P",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "86400"

	)

);?>


```