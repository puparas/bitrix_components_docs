# Список записей

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

[Запись детально](/user_help/components/content/highload/highloadblock_view.php)
[Список записей](/user_help/components/content/highload/highloadblock_list.php)

[RSS](/user_help/components/content/rss/index.php)

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

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

[Highload инфоблоки](/user_help/components/content/highload/index.php)

Список записей

# Список записей

Одностраничный компонент выводит список записей из одного Highload-блока. Компонент стандартный и входит в дистрибутив модуля.

### Описание **highloadblock.list**

В визуальном редакторе компонент расположен по пути: *Контент > Highload инфоблоки > Список записей*.

Компонент относится к модулю [Highload-блоки](/user_help/content/highloadblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID инфоблока | **BLOCK\_ID** | Идентификатор Highload-блока, записи которого будут выводиться. |
| Путь к странице просмотра записи | **DETAIL\_URL** | Задается адрес, ведущий на страницу с детальной информацией записи Highload-блока. |
| Разбить по страницам количеством | **ROWS\_PER\_PAGE** | Указывается количество записей Highload-блока, отображаемых на одной страницы. |
| Идентификатор страницы | **PAGEN\_ID** | Идентификатор страницы для постраничной навигации. |
| Идентификатор фильтра | **FILTER\_NAME** | Указывается идентификатор фильтра для передачи в компонент внешней фильтрации. |
| Поле сортировки | **SORT\_FIELD** | Укажите поле, по которому компонент будет сортировать список. |
| Направление сортировки | **SORT\_ORDER** | Укажите направление сортировки: по возрастанию или по убыванию. |
| Проверять права доступа | **CHECK\_PERMISSIONS** | [Y|N] При отмеченной опции для текущего пользователя будет проверяться право доступа к Highload-блоку. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:highloadblock.list","",Array(
		"BLOCK_ID" => "1",
		"CHECK_PERMISSIONS" => "Y",
		"DETAIL_URL" => "detail.php?BLOCK_ID=#BLOCK_ID#&ROW_ID=#ID#",
		"FILTER_NAME" => "myfilter",
		"PAGEN_ID" => "page",
		"ROWS_PER_PAGE" => "5"		
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх