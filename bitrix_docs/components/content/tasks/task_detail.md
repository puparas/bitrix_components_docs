|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Свойства задачи |

| Указываются поля, которые должны быть отображены при показе задач. |
| Тип задач |

| Указывается тип задач: **Для группы** (**group**) или **Для пользователя** (**user**). |
| **Шаблоны ссылок** |

| |
| Путь к списку задач |

| Указывается путь к списку задач. |
| Путь к задаче |

| Указывается путь к задаче. |
| Путь к представлению |

| Указывается путь к представлению задачи. |
| Путь к странице пользователя |

| Указывается путь к странице пользователя. |
| **Дополнительные настройки** |

| |
| Путь к папке со смайликами для форума относительно корня сайта |

| Указывается путь к папке со смайлами. По умолчанию указано **/bitrix/images/forum/smile/**. |
| Выводить рейтинг |

| [Y|N] При отмеченной опции будет включен функционал рейтинга. |
| Вид кнопок рейтинга |

| Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |
| Включить цепочку навигации |

| [Y|N] При отмеченной опции будет показана цепочка навигации. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции на каждой странице будет установлен заголовок **Задача №<номер\_задачи>**. |
| Количество записей на странице |

| [Y|N] Параметр определяет количество задач отображаемых на одной странице. Остальные задачи будут выведены с помощью постраничной навигации. |
| **Псевдонимы переменных** |

| |
| Имя переменной для кода задачи |

| Поле содержит имя переменной для кода задачи. |
| Имя переменной для кода пользователя |

| Поле содержит имя переменной для кода пользователя. |
| Имя переменной для кода группы |

| Поле содержит имя переменной для кода группы. |
| Имя переменной для кода действия |

| Поле содержит имя переменной для кода действия. |
| Имя переменной для кода страницы |

```


 <?$APPLICATION->IncludeComponent(

	"bitrix:tasks.task.detail",

	"",

	Array(

		"TASKS_FIELDS_SHOW" => array(),

		"TASK_TYPE" => "group",

		"TASK_VAR" => "task_var",

		"USER_VAR" => "user_var",

		"GROUP_VAR" => "grouop_var",

		"ACTION_VAR" => "action_var",

		"PAGE_VAR" => "page_var",

		"PATH_TO_GROUP_TASKS" => "/workgroups/group/#group_id#/tasks/",

		"PATH_TO_GROUP_TASKS_TASK" => "/workgroups/group/#group_id#/tasks/task/view/#task_id#/",

		"PATH_TO_GROUP_TASKS_VIEW" => "",

		"PATH_TO_FORUM_SMILE" => "/bitrix/images/forum/smile/",

		"URL_TEMPLATES_PROFILE_VIEW" => "",

		"SHOW_RATING" => "",

		"RATING_TYPE" => "",

		"SET_NAVCHAIN" => "Y",

		"SET_TITLE" => "Y",

		"ITEMS_COUNT" => "20"

	)

);?>


```