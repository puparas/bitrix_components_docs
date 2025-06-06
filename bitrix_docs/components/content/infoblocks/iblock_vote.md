# Голосование

Документация для разработчиков

[Документация для разработчиков](https://dev.1c-bitrix.ru/api_help/)
[Документация по D7](https://dev.1c-bitrix.ru/api_d7/)
[Документация по REST](https://dev.1c-bitrix.ru/rest_help/)
[Пользовательская документация](https://dev.1c-bitrix.ru/user_help/)

Темная тема

[Основные сведения](/user_help/index.php)
[Реализация и системные требования](/user_help/reqintro.php)

[Справочная система и документация](/user_help/help/index.php)

[Контент](/user_help/content/index.php)

[Сайты 24](/user_help/sites24/index.php)

[Маркетинг](/user_help/marketing/index.php)

[Магазин](/user_help/store/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Агрегатор библиотек документов (КП)](/user_help/components/content/webdav/index.php)

[Задачи 2.0 (КП)](/user_help/components/content/tasks/index.php)

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

[Фотогалерея](/user_help/components/content/photogallery/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

[Google Maps](/user_help/components/content/google_maps/index.php)

[Highload инфоблоки](/user_help/components/content/highload/index.php)

[RSS](/user_help/components/content/rss/index.php)

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

[Голосование](/user_help/components/content/infoblocks/iblock_vote.php)

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Медиа](/user_help/components/content/media/index.php)

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

Голосование

# Голосование

### Описание **iblock.vote**

Компонент реализует возможность голосования для пользователей. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Инфоблоки > Голосование*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор необходимого информационного блока. |
| ID элемента | **ELEMENT\_ID** | Указывается числовой код, в котором передается идентификатор элемента. Поле может быть оставлено пустым, если указан **Код элемента**. |
| Код элемента | **ELEMENT\_CODE** | Указывается символьный код элемента. Поле может быть оставлено пустым, если указан **ID элемента**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Максимальный балл | **MAX\_VOTE** | Указывается максимально возможный балл, т.е. число возможных оценок. |
| Подписи к баллам | **VOTE\_NAMES** | Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:  ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. |
| В качестве рейтинга показывать  (кроме шаблонов default, ajax\_photo) | **DISPLAY\_AS\_RATING** | Выбирается что отображать в качестве рейтинга: сам рейтинг, либо среднее значение (сумма голосов поделённая на количество). |
| **Настройки 404 ошибки** | | |
| Устанавливать статус 404, если не найдены элемент или раздел | **SET\_STATUS\_404** | [Y|N] Если система не находит в каталоге элемент или раздел, то при отмеченной опции вместо HTTP статуса 200 будет сообщаться HTTP статус 404. |
| Сообщение для показа (по умолчанию из компонента) | **MESSAGE\_404** | Задается сообщение, которое будет показано в случае возникновения ошибки 404. Если ничего не указывать, то будет использоваться стандартное сообщение из компонента. |

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

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх