|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID местоположения |

| Идентификатор местоположения, которое должно быть отображено в форме. Можно не задавать, если задан **Символьный код местоположения**. |
| Символьный код местоположения |

| Символьный код местоположения, которое должно быть отображено в форме. Можно не задавать, если задан **ID местоположения**. |
| Имя поля ввода |

| Задается название переменной для имени поля ввода. |
| Сохранять связь через |

| Указывается, что необходимо записать в форму ввода при выборе местоположения: идентификатор (id) или символьный код (code). |
| **Источник данных** |

| |
| Отображать статичный ствол дерева |

| [Y|N] Если у дерева местоположений есть цепочка, ведущая от корня и не имеющая разветвлений, то при отмеченной опции она будет отображена в селекторе как выбранная изначально. |
| Предварительно загружать последний выбранный уровень |

| [Y|N] Если опция включена, то последний выбранный уровень будет пред-загружен при показе компонента. В противном случае, данные будут загружены при попытке открытия выпадающего списка. |
| Фильтровать по сайту |

| [Y|N] При отмеченной опции выбор местоположений осуществляется только среди тех, которые привязаны к сайту. |
| Отображать местоположения по умолчанию |

| [Y|N] При отмеченной опции вверху формы выбора местоположений будут отображены избранные местоположения. |
| Cайт |

| Указывается сайт, по местоположениям которого будет делаться выборка. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Идентификатор javascript-контрола |

| Системный параметр. Не описывается. |
| Javascript-функция обратного вызова |

| Системный параметр. Не описывается. |
| Не показывать ошибки, если они возникли при загрузке компонента |

| [Y|N] При отмеченной опции ошибки, возникающие при загрузке компонента, отображаться не будут. |
| Отключить поиск через ввод с клавиатуры и не показывать следующий уровень при выборе |

| [Y|N] При отмеченной опции будет отключен поиск местоположений через ввод с клавиатуры не будет показываться следующий уровень при выборе. |
| Инициализировать компонент только при наступлении указанного javascript-события на объекте window.document |

```
<?$APPLICATION->IncludeComponent(

	"bitrix:sale.location.selector.steps",

	"",

	Array(

		"COMPONENT_TEMPLATE" => ".default",

		"ID" => "980",

		"CODE" => "",

		"INPUT_NAME" => "LOCATION",

		"PROVIDE_LINK_BY" => "id",

		"JSCONTROL_GLOBAL_ID" => "",

		"JS_CALLBACK" => "",

		"FILTER_BY_SITE" => "Y",

		"SHOW_DEFAULT_LOCATIONS" => "Y",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "36000000",

		"FILTER_SITE_ID" => "s1",

		"PRECACHE_LAST_LEVEL" => "N",

		"PRESELECT_TREE_TRUNK" => "N",

		"DISABLE_KEYBOARD_INPUT" => "N",

		"INITIALIZE_BY_GLOBAL_EVENT" => "",

		"SUPPRESS_ERRORS" => "N"

	)

);?>


```