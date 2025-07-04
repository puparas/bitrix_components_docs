|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Показывать события текущего пользователя |

| [Y|N] При отмеченной опции будут показаны события календаря текущего пользователя.   Если опция не отмечена (параметр принимает значение **N**), то необходимо настроить следущие параметры: **IBLOCK\_TYPE**, **IBLOCK\_ID** и **IBLOCK\_SECTION\_ID**. |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационного блока. |
| Инфоблок |

| Для выбранного типа инфоблока указывается идентификатор информационного блока, события календарей которого будут выводиться. |
| ID секции инфоблока |

| В поле указывается код, в котором передается идентификатор календаря (раздела инфоблока), события которого будут отображены. |
| Дата инициализации |

| Если в параметре указана дата, то список ближайших событий будет выведен для заданной даты. В противном случае список ближайших событий календаря будет отображен для текущей даты. |
| Показывать ближайшие события за количество месяцев |

| Указывается количество месяцев, за которые будут отображены ближайшие события. |
| Адрес страницы для детального просмотра |

| Указывается адрес страницы для детального просмотра события календаря. |
| Количество событий в списке |

| Указывается количество событий, которые будут отображены в списке ближайших событий. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

```
<$APPLICATION->IncludeComponent("bitrix:intranet.event_list","",Array(

		"B_CUR_USER_LIST" => "N",

		"IBLOCK_TYPE" => "events",

		"IBLOCK_ID" => "13",

		"IBLOCK_SECTION_ID" => "",

		"INIT_DATE" => "--текущая дата--",

		"FUTURE_MONTH_COUNT" => "2",

		"DETAIL_URL" => "",

		"EVENTS_COUNT" => "5",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600"

	)

);?>
```