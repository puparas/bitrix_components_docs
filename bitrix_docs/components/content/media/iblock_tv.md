# Видеотека

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

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Медиа](/user_help/components/content/media/index.php)

[Медиа проигрыватель](/user_help/components/content/media/player.php)
[Видеотека](/user_help/components/content/media/iblock_tv.php)
[Просмотр pdf-файлов](/user_help/components/content/media/pdf_viewer.php)

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

[Медиа](/user_help/components/content/media/index.php)

Видеотека

# Видеотека

Одностраничный компонент осуществляет вывод и поочередное проигрывание серии видеороликов в одном **Медиа проигрывателе**. Компонент является стандартным и входит в дистрибутив модуля.

### Описание **iblock.tv**

**Примечание**: при настройке компонента учтите, что часть полей последовательно появляется после выбора вышестоящих параметров.

В визуальном редакторе компонент расположен по пути: *Контент > Медиа > Видеотека*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Общие настройки компонента** | | |
| Тип информационного блока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Информационный блок | **IBLOCK\_ID** | Для выбранного типа инфоблока указывается идентификатор информационного блока, из которого будет выводиться ролики. |
| Разрешить проигрывание swf-файлов (не рекомендуется) | **ALLOW\_SWF** | [Y|N] При отмеченной опции будет разрешено проигрывание файлов формата swf. Не рекомендуется использовать в силу высокой степени опасности XSS-атаки через подключаемый файл. |
| Свойство, в котором хранится путь к ролику | **PATH\_TO\_FILE** | Задается свойство инфоблока, в котором указывается путь к файлу ролика. |
| Свойство, в котором хранится длительность ролика | **DURATION** | Задается свойство инфоблока, в котором указывается длительность воспроизведения ролика. |
| **Настройки плеера** | | |
| Ширина области плеера | **WIDTH** | Указывается ширина области плеера в пикселях (px). |
| Высота области плеера | **HEIGHT** | Указывается высота области плеера в пикселях (px). |
| Логотип | **LOGO** | Указывается путь до файла с логотипом, накладываемым на ролик при просмотре. |
| Секция | **SECTION\_ID** | Указывается раздел, ролики из которого будут отображены. |
| **Статистика показов** | | |
| Увеличить счетчик показов элемента | **SHOW\_COUNTER\_EVENT** | [Y|N] При отмеченной опции будет запущен счетчик показа каждого элемента (ролика). |
| Учитывать события в модуле статистики | **STAT\_EVENT** | [Y|N] При отмеченной опции события будут учитываться в модуле **Веб-аналитика**. При выборе данной опции станут доступны дополнительные поля.     |  |  |  | | --- | --- | --- | | event1 | **STAT\_EVENT1** | Указывается параметр типа события event1. | | event2 | **STAT\_EVENT2** | Указывается параметр типа события event2. | |
| **Настройки списка** | | |
| Маленькое изображение по умолчанию | **DEFAULT\_SMALL\_IMAGE** | Указывается путь до маленького изображения ролика. Изображение будет показано в списке роликов. |
| Большое изображение по умолчанию | **DEFAULT\_BIG\_IMAGE** | Указывается путь до большого изображения ролика. Изображение будет показано на экране плеера перед началом просмотра видеоролика. |
| Поле для первой сортировки роликов | **SORT\_BY1** | Поле для первой сортировки роликов:  * **ID** - по идентификатору; * **NAME** – по заголовку; * **ACTIVE\_FROM** – по дате начала активности; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** - по дате последнего изменения. |
| Направление для первой сортировки роликов | **SORT\_ORDER1** | Направление для первой сортировки роликов:  * **ASC** – по возрастанию; * **DECS** – по убыванию. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:iblock.tv","",Array(
		"DEFAULT_SMALL_IMAGE" => "/bitrix/components/bitrix/iblock.tv/templates/.default/images/default_small.png",
		"DEFAULT_BIG_IMAGE" => "/bitrix/components/bitrix/iblock.tv/templates/.default/images/default_big.png",
		"SORT_BY1" => "ACTIVE_FROM",
		"SORT_ORDER1" => "DESC",
		"IBLOCK_TYPE" => "services",
		"IBLOCK_ID" => "4",
		"ALLOW_SWF" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"CACHE_GROUPS" => "Y",
		"SHOW_COUNTER_EVENT" => "Y",
		"PATH_TO_FILE" => "15",
		"DURATION" => "16",
		"WIDTH" => "400",
		"HEIGHT" => "300",
		"LOGO" => "/bitrix/components/bitrix/iblock.tv/templates/.default/images/logo.png",
		"SECTION_ID" => "9",
		"ELEMENT_ID" => "16",
		"STAT_EVENT" => "Y",
		"STAT_EVENT1" => "player",
		"STAT_EVENT2" => "start_playing"
	)
);?>

```

### Смотрите также

* [Как наполнить видеотеку](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&CHAPTER_ID=04593)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх