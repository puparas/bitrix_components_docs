|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Идентификатор пользователя |

| Параметр содержит код, в котором передается идентификатор пользователя социальной сети. |
| **Внешний вид** |

| |
| Количество записей в списке |

| Указывается количество визиток групп, отображаемых на одной странице. Все визитки будут выведены с помощью постраничной навигации. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к странице пользователя |

| Задается путь к странице профиля пользователя социальной сети. |
| Шаблон пути к странице создания группы |

| Задается путь к странице создания новой группы социальной сети. |
| Шаблон пути к странице группы |

| Задается путь к странице группы социальной сети. |
| Шаблон пути к обновлениям |

| Задается путь к странице обновлений социальной сети. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт **Группы**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на странице в качестве заголовка будет установлено **Группы**. |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для пользователя |

| Указывается имя переменной, которой передается идентификатор пользователя социальной сети. |
| Имя переменной для группы |

```
<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.user_groups","",Array(

		"SET_NAVCHAIN" => "Y", 

		"ITEMS_COUNT" => "30", 

		"PATH_TO_USER" => "index.php?page=user&user_id=#user_id#", 

		"PATH_TO_GROUP_CREATE" => "group_add.php?page=create&user_id=#user_id#", 

		"PATH_TO_GROUP" => "/community/workgroups/group_view.php?page=group&group_id=#group_id#", 

		"PAGE_VAR" => "page", 

		"USER_VAR" => "user_id", 

		"PATH_TO_LOG" => "user_log.php?page=log&user_id=#user_id#", 

		"GROUP_VAR" => "group_id", 

		"USER_ID" => $user_id, 

		"SET_TITLE" => "Y" 

	)

);?>


```