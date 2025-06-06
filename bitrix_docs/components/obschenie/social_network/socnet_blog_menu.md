|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| Шаблон пути к главной странице сообщений |

| Указывается путь к главной странице блога. |
| Шаблон пути к недописанным сообщениям |

| Указывается путь к недописанным сообщениям социальной сети. |
| Шаблон пути к странице редактирования сообщения |

| Указывается путь к странице редактирования сообщения блога социальной сети. |
| Шаблон пути к странице пользователя |

| Указывается путь к странице пользователя блога социальной сети. |
| **Дополнительные настройки** |

| |
| Добавлять пункт в цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт с названием блога. |
| **Имена переменных** |

| |
| Имя переменной для идентификатора блога |

| Указывается имя переменной, которой передается идентификатор блога. |
| Имя переменной для идентификатора сообщения |

| Указывается имя переменной, которой передается идентификатор сообщения блога. |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница блога. |
| Имя переменной для идентификатора пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.blog.menu","",Array(

	"PATH_TO_BLOG" => "blog_blog.php?page=blog&blog=#blog#", 

	"PATH_TO_BLOG_INDEX" => "blog_s.php", 

	"PATH_TO_DRAFT" => "blog_b_draft.php?page=draft&blog=#blog#", 

	"PATH_TO_POST_EDIT" => "blog_p_edit.php?page=post_edit&blog=#blog#&post_id=#post_id#", 

	"PATH_TO_USER" => "blog_user.php?page=user&user_id=#user_id#", 

	"PATH_TO_USER_FRIENDS" => "blog_friends.php?page=user_friend&user_id=#user_id#", 

	"PATH_TO_USER_SETTINGS" => "blog_user_set.php?page=user_settings&blog=#blog#", 

	"PATH_TO_GROUP_EDIT" => "blog_user_gr.php?page=group_edit&blog=#blog#", 

	"PATH_TO_BLOG_EDIT" => "blog_b_edit.php?page=blog_edit&blog=#blog#", 

	"PATH_TO_CATEGORY_EDIT" => "blog_category.php?page=category_edit&blog=#blog#", 

	"BLOG_VAR" => "blog", 

	"POST_VAR" => "post_id", 

	"PAGE_VAR" => "page", 

	"USER_VAR" => "user_id", 

	"BLOG_URL" => $blog, 

	"SET_NAV_CHAIN" => "Y" 

	),

);?>


```