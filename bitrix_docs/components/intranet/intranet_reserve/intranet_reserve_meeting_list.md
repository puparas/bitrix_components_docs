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
| Группы пользователей, которые могут изменять переговорные |

| Указываются группы пользователей, которым будет разрешено создавать и изменять переговорные. |
| Группы пользователей, которые могут резервировать переговорные |

| Указываются группы пользователей, которые будут осуществлять резервирование переговорных комнат. |
| **Шаблоны ссылок** |

| |
| Путь к графику переговорной |

| Указывается путь к странице с графиком переговорной от корня сайта. |
| Путь к главной странице резервирования переговорных |

| Указывается путь к странице со списком переговорных от корня сайта. |
| Путь к странице резервирования переговорных |

| Указывается путь к странице резервирования переговорной от корня сайта. |
| Путь к странице изменения переговорной |

| Указывается путь к странице изменения переговорной от корня сайта. |
| **Дополнительные настройки** |

| |
| Устанавливать навигационную цепочку |

| [Y|N] При отмеченной опции будет добавлен пункт с заголовком страницы в цепочку навигации. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Список переговорных**. |
| **Псевдонимы переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, используемой для идентификации страницы. |
| Имя переменной для идентификатора переговорной |

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.reserve_meeting.list","",Array(

		"IBLOCK_TYPE" => "services",

		"IBLOCK_ID" => "25",

		"PAGE_VAR" => "",

		"MEETING_VAR" => "",

		"PATH_TO_MEETING" => "",

		"PATH_TO_MEETING_LIST" => "",

		"PATH_TO_RESERVE_MEETING" => "",

		"PATH_TO_MODIFY_MEETING" => "",

		"SET_NAVCHAIN" => "Y",

		"SET_TITLE" => "Y",

		"USERGROUPS_MODIFY" => Array("1"),

		"USERGROUPS_RESERVE" => Array("1")

	),

);?>


```