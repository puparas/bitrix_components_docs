# Экспорт каталога в 1C

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

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Импорт каталога из 1С](/user_help/components/content/1c_exchange/catalog_import_1c.php)
[Экспорт каталога в 1C](/user_help/components/content/1c_exchange/export_1c.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

Экспорт каталога в 1C

# Экспорт каталога в 1C

### Описание **catalog.export.1c**

Компонент выполняет экспорт данных в 1С в формате CommerceML v2. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Обмен с 1С > Экспорт каталога в 1с*.

Компонент относится к модулю [Торговый каталог](/user_help/store/catalog/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Инфоблок каталога | **IBLOCK\_ID** | Выбирается инфоблок для экспорта. |
| Интервал одного шага в секундах (0 - выполнять выгрузку за один шаг) | **INTERVAL** | Указывается интервал одного шага в секундах при экспорте каталога. **0** - выполнять выгрузку за один шаг. |
| Количество элементов выгружаемых за один шаг (0 - выполнять выгрузку за один шаг) | **ELEMENTS\_PER\_STEP** | Указывается число элементов, выгружаемых за один шаг. **0** - выполнять выгрузку за один шаг. |
| Группы пользователям которых разрешена выгрузка | **GROUP\_PERMISSIONS** | Указывается группа(-ы), пользователей которые имеют права на выгрузку заказов в 1С. |
| Использовать сжатие zip, если доступно | **USE\_ZIP** | [Y|N] При отмеченной опции данные сжимаются ZIP форматом (если доступно). Это позволяет заметно уменьшить размер файлов. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent
"bitrix:catalog.export.1c",
	"",
	Array(
		"IBLOCK_ID" => "5",
		"INTERVAL" => "30",
		"ELEMENTS_PER_STEP" => "100",
		"GROUP_PERMISSIONS" => array(),
		"USE_ZIP" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх