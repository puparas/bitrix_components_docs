|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок |

| Для выбранного типа инфоблоков указывается идентификатор необходимого информационного блока. |
| ID элемента |

| Указывается числовой код, в котором передается идентификатор элемента. Поле может быть оставлено пустым, если указан **Код элемента**. |
| Код элемента |

| Указывается символьный код элемента. Поле может быть оставлено пустым, если указан **ID элемента**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Максимальный балл |

| Указывается максимально возможный балл, т.е. число возможных оценок. |
| Подписи к баллам |

| Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:  ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. |
| В качестве рейтинга показывать  (кроме шаблонов default, ajax\_photo) |

| Выбирается что отображать в качестве рейтинга: сам рейтинг, либо среднее значение (сумма голосов поделённая на количество). |
| **Настройки 404 ошибки** |

| |
| Устанавливать статус 404, если не найдены элемент или раздел |

| [Y|N] Если система не находит в каталоге элемент или раздел, то при отмеченной опции вместо HTTP статуса 200 будет сообщаться HTTP статус 404. |
| Сообщение для показа (по умолчанию из компонента) |

| Задается сообщение, которое будет показано в случае возникновения ошибки 404. Если ничего не указывать, то будет использоваться стандартное сообщение из компонента. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.vote","",Array(

		"IBLOCK_TYPE" => "photos",

		"IBLOCK_ID" => "22",

		"ELEMENT_ID" => $_REQUEST["ELEMENT_ID"],

		"ELEMENT_CODE" => $_REQUEST["code"],

		"MAX_VOTE" => "5",

		"VOTE_NAMES" => array("0","1","2","3","4"),

		"SET_STATUS_404" => "N",

		"MESSAGE_404" => "",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600"

	)

);?>


```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **rustam550** 05.06.2017 15:02:44 |
| --- |
| В последних версиях рейтинг считается немного иначе. $rating = round((сумма оценок+31.25/5\*максимально допустимый рейтинг)/(количество проголосовавших+10),2);  Это можно увидеть в компоненте \bitrix\components\bitrix\iblock.vote\component.php строчка 190. |
|  |

| 24  **Роман Петров** 02.08.2012 16:48:48 |
| --- |
| не нашел этого в документации, а это важно. Дублирую ответ техподдержки про расчет рейтинга:  Для расчёта рейтинга применяется специальная формула. |
|  |

``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.vote","",Array(

		"IBLOCK_TYPE" => "photos",

		"IBLOCK_ID" => "22",

		"ELEMENT_ID" => $_REQUEST["ELEMENT_ID"],

		"ELEMENT_CODE" => $_REQUEST["code"],

		"MAX_VOTE" => "5",

		"VOTE_NAMES" => array("0","1","2","3","4"),

		"SET_STATUS_404" => "N",

		"MESSAGE_404" => "",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600"

	)

);?>


```