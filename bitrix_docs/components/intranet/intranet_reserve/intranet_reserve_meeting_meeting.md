|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается тип информационного блока, используемого для резервирования переговорных. |
| Инфоблок |

| Для выбранного типа инфоблоков указывается идентификатор инфоблока, используемый для резервирования переговорных. |
| Код переговорной |

| Код, используемый для идентификации переговоной. |
| Группы пользователей, которые могут снимать резервирование переговорных |

| Указываются группы пользователей, которые смогут отменять события переговорных. |
| Выходные дни недели |

| Указываются выходные дни недели, которые не будут отображаться в графике переговорных. |
| **Шаблоны ссылок** |

| |
| Путь к графику переговорной |

| Указывается путь к странице с графиком переговорной от корня сайта. |
| Путь к главной странице резервирования переговорных |

| Указывается путь к главной странице резервирования переговорных от корня сайта. |
| Путь к странице просмотра брони |

| Указывается путь к странице просмотра брони от корня сайта. |
| Путь к странице резервирования переговорных |

| Указывается путь к странице резервирования переговорной от корня сайта. |
| **Дополнительные настройки** |

| |
| Устанавливать навигационную цепочку |

| [Y|N] При отмеченной опции будет добавлен пункт с заголовком страницы в цепочку навигации. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **График переговорной: <название\_переговорной>**. |
| **Псевдонимы переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, используемой для идентификации страницы. |
| Имя переменной для идентификатора переговорной |

| Указывается имя переменной, используемой для идентификации переговорной. |
| Имя переменной для идентификатора резервирования |

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.reserve_meeting.meeting","",Array(

		"IBLOCK_TYPE" => "events",

		"IBLOCK_ID" => "16",

		"PAGE_VAR" => "",

		"MEETING_VAR" => "",

		"ITEM_VAR" => "",

		"MEETING_ID" => "44",

		"PATH_TO_MEETING" => "",

		"PATH_TO_MEETING_LIST" => "",

		"PATH_TO_VIEW_ITEM" => "",

		"PATH_TO_RESERVE_MEETING" => "",

		"SET_NAVCHAIN" => "Y",

		"SET_TITLE" => "Y",

		"USERGROUPS_CLEAR" => Array(),

		"WEEK_HOLIDAYS" => Array("5","6")

	)

);?>


```