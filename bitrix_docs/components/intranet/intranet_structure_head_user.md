|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Идентификатор пользователя |

| Параметр содержит код, в котором передается идентификатор пользователя. |
| Шаблон ссылки на подразделение |

| Указывается шаблон ссылки на подразделение компании. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

```


<?$APPLICATION->IncludeComponent("bitrix:intranet.structure.head.user","",Array(

		"ID" => $USER->GetID(),

		"DETAIL_URL" => "/company/structure.php?set_filter_structure=Y&structure_UF_DEPARTMENT=#ID#",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600"

	),

);?>


```