|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Искать без учета морфологии (при отсутствии результата поиска) |

| [Y|N] Если опция отмечена, то будет отключен морфологический поиск (морфологический поиск предполагает поиск по полному совпадению слова с запросом). |
| Отключить обработку слов как логических операторов |

| [Y|N] При отмеченной опции слова (и, или, не) не будут использоваться как логические операторы. |
| **Шаблоны ссылок** |

| |
| Страница списка форумов |

| Указывается адрес страницы со списком форумов. По умолчанию поле содержит *index.php*. |
| Страница чтения темы |

| Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#.** |
| Страница чтения сообщения |

| Указывается адрес страницы чтения сообщения форума. По умолчанию поле содержит **message.php?FID=#FID#&TID=#TID#&MID=#MID#.** |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Указывается тип кеширования:  * **A** - Авто: действует при включенном кешировании в течение заданного времени; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| ID форума |

| Указывается форумы, по которым будет осуществляться поиск. |
| Формат показа даты |

| Формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->, вы можете сформировать свой вариант на основании php-функции **date**.** |
| Количество тем на одной странице |

| Количество тем, отображаемых на одной странице. Для отображения всех тем используется постраничная навигация. |
| Название шаблона для вывода постраничной навигации |

| Название шаблона для вывода постраничной навигации. Если поле пусто, то используется шаблон по умолчанию, также в системе имеется шаблон orange. |
| Количество страниц в постраничной навигации |

| Задается количество отображаемых в навигации ссылок на страницы. Если количество страниц превышает заданное число, то в навигацию будет добавлено многоточие. |
| Показывать навигацию |

| [Y|N] При отмеченной опции в навигационной цепочке будет отражен переход на страницу поиска. |
| Устанавливать заголовок страницы |

```
<?APPLICATION->IncludeComponent("bitrix:forum.search","",Array(

		"URL_TEMPLATES_INDEX" => "index.php", 

		"URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#", 

		"URL_TEMPLATES_MESSAGE" => "message.php?FID=#FID#&TID=#TID#&MID=#MID#", 

		"FID_RANGE" => Array("3"), 

		"DATE_FORMAT" => "d.m.Y H:i:s", 

		"TOPICS_PER_PAGE" => "10", 

		"PAGE_NAVIGATION_TEMPLATE" => "",

		"PAGE_NAVIGATION_WINDOW" => "11", 

		"SET_NAVIGATION" => "Y", 

		"DISPLAY_PANEL" => "N", 

		"CACHE_TYPE" => "A", 

		"CACHE_TIME" => "3600", 

		"SET_TITLE" => "Y" 

	)

);?>


```