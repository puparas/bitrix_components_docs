|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается тип информационного блока. |
| Информационный блок |

| Для выбранного типа инфоблоков указывается идентификатор инфоблока, в котором хранится мастер техподдержки. |
| Свойство, в котором хранится тип вопроса |

| Указывается свойство, в котором хранится тип вопроса. |
| Множественное свойство, в котором хранятся значения выпадающего списка |

| Указывается множественное свойство, в котором хранятся значения выпадающего списка. |
| Страница, с которой пришли на мастер (для кнопки "Назад", может быть пустое) |

| Указывается адрес страницы, с которой пришли на мастер (для кнопки "Назад", поле может быть пустое). |
| Страница с формой редактирования сообщения |

| Указывается адрес страницы с формой редактирования сообщения. |
| **Управление режимом AJAX** |

| |
| Включить режим AJAX |

| [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента |

| [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей |

| [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера |

| [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Дополнительные настройки** |

| |
| Добавлять разделы мастера в навигационную цепочку |

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.wizard","",Array(

		"AJAX_MODE" => "N", 

		"IBLOCK_TYPE" => "services", 

		"IBLOCK_ID" => "11", 

		"PROPERTY_FIELD_TYPE" => "", 

		"PROPERTY_FIELD_VALUES" => "", 

		"BACK_URL" => "ticket_list.php", 

		"NEXT_URL" => "ticket_edit.php", 

		"INCLUDE_IBLOCK_INTO_CHAIN" => "Y", 

		"CACHE_TYPE" => "A", 

		"CACHE_TIME" => "3600", 

		"AJAX_OPTION_JUMP" => "N", 

		"AJAX_OPTION_STYLE" => "Y", 

		"AJAX_OPTION_HISTORY" => "N" 

	),

);?>


```