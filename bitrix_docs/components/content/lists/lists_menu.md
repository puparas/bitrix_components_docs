# Меню списков

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

[Универсальные списки](/user_help/components/content/lists/lists.php)
[Списки](/user_help/components/content/lists/lists_lists.php)
[Список](/user_help/components/content/lists/lists_list.php)
[Разделы списка](/user_help/components/content/lists/lists_sections.php)
[Редактирование элемента](/user_help/components/content/lists/lists_element_edit.php)
[Настройки списка](/user_help/components/content/lists/lists_list_edit.php)
[Поля списка](/user_help/components/content/lists/lists_fields.php)
[Настройки поля списка](/user_help/components/content/lists/lists_field_edit.php)
[Навигационная цепочка](/user_help/components/content/lists/lists_element_navchain.php)
[Меню списков](/user_help/components/content/lists/lists_menu.php)
[Скачивание файла](/user_help/components/content/lists/lists_file.php)

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

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

Меню списков

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Меню списков

### Описание **lists.menu**

Компонент добавляет в меню пункты, ведущие на страницы списков. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Универсальные списки > Меню списков*.

Компонент относится к модулю [Универсальные списки](/user_help/content/lists/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE\_ID** | Указывается тип информационных блоков, откуда будет использоваться информация. |
| **Шаблоны ссылок** | | |
| Включить режим совместимости с поддержкой ЧПУ | **IS\_SEF** | Установка флажка включает режим использвоания ЧПУ. Если режим поддержки ЧПУ включен, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_BASE\_URL** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Основа ЧПУ URL списка | **SEF\_LIST\_BASE\_URL** | Указывается основа для построения шаблона ссылок универсального списка. | | URL списка | **SEF\_LIST\_URL** | Указывается шаблон ссылки на универсальный список. |  **SEF\_BASE\_URL**, **SEF\_LIST\_BASE\_URL** и **SEF\_LIST\_URL**.  Если режим поддержки ЧПУ выключен, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | URL списка | **LIST\_URL** | Указывается шаблон ссылки на универсальный список. | | ID списка для подсветки пункта меню | **LIST\_ID** | Указывается шаблон пункта меню для подсветки. |  **LIST\_URL** и **LIST\_ID**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```
 <?$APPLICATION->IncludeComponent(
	"bitrix:lists.menu",
	"",
	Array(
		"IBLOCK_TYPE_ID" => "lists",
		"IS_SEF" => "N",
		"LIST_URL" => "lists.list.php?list_id=#list_id#",
		"LIST_ID" => $_REQUEST["list_id"],
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"CACHE_NOTES" => ""
	)
); ?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх