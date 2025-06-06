# Список своих элементов

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

[Добавление элементов инфоблока (комплексный компонент)](/user_help/components/content/adding/iblock_element_add.php)
[Список своих элементов](/user_help/components/content/adding/iblock_element_add_list.php)
[Форма добавления / редактирования](/user_help/components/content/adding/iblock_element_add_form.php)

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

[Добавление элементов](/user_help/components/content/adding/index.php)

Список своих элементов

# Список своих элементов

### Описание **iblock.element.add.list**

Компонент осуществляет вывод списка доступных пользователю элементов указанного инфоблока, ссылок **Добавить**, **Редактировать**, **Удалить**. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Добавление элементов >Список своих элементов*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Параметры компонента** | | |
| Страница редактирования элемента | **EDIT\_URL** | Указывается адрес страницы редактирования элемента. |
| Количество элементов на странице | **NAV\_ON\_PAGE** | Задается количество элементов на одной странице. Все элементы будут выведены с помощью постраничной навигации. |
| Ограничить кол-во элементов для одного пользователя | **MAX\_USER\_ENTRIES** | Задается максимальное количество элементов, которое может добавить пользователь. |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор необходимого информационного блока. |
| **Параметры доступа** | | |
| Группы пользователей, имеющие право на добавление/редактирование | **GROUPS** | Указываются группы пользователей, имеющие право на добавление/редактирование элементов инфоблока. |
| Редактирование возможно для статуса | **STATUS** | Указываются статусы, находясь в которых элементы будут отображаться пользователям. |
| Привязка к пользователю | **ELEMENT\_ASSOC** | Задается привязка к пользователю:  * **никому** (**N**) - нет привязки, элементы не показываются всем пользователям. В этом случае параметры **ALLOW\_EDIT** и **ALLOW\_DELETE** не доступны. * **создателю** (**CREATED\_BY**) - привязка по создателю: пользователю будут показаны только созданные им элементы. * **по свойству инфоблока -->** (**PROPERTY\_ID**) - привязка по свойству инфоблока. В этом случае доступен параметр **ELEMENT\_ASSOC\_PROPERTY**. |
| по свойству инфоблока --> | **ELEMENT\_ASSOC\_PROPERTY** | Указывается свойство, по которому выполняется привязка. |
| Разрешать редактирование | **ALLOW\_EDIT** | [Y|N] При отмеченной опции будут выведены ссылки на редактирование доступных пользователю элементов. |
| Разрешать удаление | **ALLOW\_DELETE** | [Y|N] При отмеченной опции будут выведены ссылки на удаление доступных пользователю элементов. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:      |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами. |  **SEF\_FOLDER**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.element.add.list","",Array(
		"SEF_MODE" => "Y", 
		"IBLOCK_TYPE" => "articles", 
		"IBLOCK_ID" => "2", 
		"GROUPS" => Array("1", "2", "3", "4", "5", "6", "7", "8"), 
		"STATUS" => Array("2", "3", "1"), 
		"EDIT_URL" => "", 
		"ELEMENT_ASSOC" => "PROPERTY_ID",
		"ELEMENT_ASSOC_PROPERTY" => "2",		 
		"ALLOW_EDIT" => "Y", 
		"ALLOW_DELETE" => "Y", 
		"NAV_ON_PAGE" => "10", 
		"MAX_USER_ENTRIES" => "100000", 
		"SEF_FOLDER" => "/", 
		"VARIABLE_ALIASES" => Array(
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх