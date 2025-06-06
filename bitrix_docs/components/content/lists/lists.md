|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Тип инфоблока |

| Указывается тип информационных блоков, в котором будут храниться универсальные списки. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **lists** - главная страница; * **list** - страница элементов и разделов; * **list\_sections** - страница управления разделами; * **list\_edit** - страница настроек списка; * **list\_fields** - страница с полями списка; * **list\_field\_edit** - страница настроек полей списка. * **element\_id** - страница редактирования элемента; * **document\_state\_id** - страница просмотра журнала бизнес-процесса; * **element\_id** - страница запуска бизнес-процесса; * **task\_id** - страница задачи бизнес-процесса. |  : **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

```


<?$APPLICATION->IncludeComponent("bitrix:lists","",Array(

		"SEF_MODE" => "Y",

		"IBLOCK_TYPE_ID" => "lists",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"SEF_FOLDER" => "/",

		"SEF_URL_TEMPLATES" => Array(

			"lists" => "",

			"list" => "#list_id#/view/#section_id#/",

			"list_sections" => "#list_id#/edit/#section_id#/",

			"list_edit" => "#list_id#/edit/",

			"list_fields" => "#list_id#/fields/",

			"list_field_edit" => "#list_id#/field/#field_id#/",

			"list_element_edit" => "#list_id#/element/#section_id#/#element_id#/",

			"bizproc_log" => "#list_id#/bp_log/#document_state_id#/",

			"bizproc_workflow_start" => "#list_id#/bp_start/#element_id#/",

			"bizproc_task" => "#list_id#/bp_task/#section_id#/#element_id#/#task_id#/"

		),

		"VARIABLE_ALIASES" => Array(

			"lists" => Array(),

			"list" => Array(),

			"list_sections" => Array(),

			"list_edit" => Array(),

			"list_fields" => Array(),

			"list_field_edit" => Array(),

			"list_element_edit" => Array(),

			"bizproc_log" => Array(),

			"bizproc_workflow_start" => Array(),

			"bizproc_task" => Array(),

			

		)

	)

);?>


```