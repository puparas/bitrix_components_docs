# Альбом

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

[Фотогалерея 2.0 (комплексный компонент)](/user_help/components/content/photogallery2/photogallery.php)
[Фотогалерея 2.0 (многопользовательская) (комплексный компонент)](/user_help/components/content/photogallery2/photogallery_user_composite.php)
[Альбом](/user_help/components/content/photogallery2/photogallery_section.php)
[Альбом (список)](/user_help/components/content/photogallery2/photogallery_section_list.php)
[Панель](/user_help/components/content/photogallery2/photogallery_user.php)
[Фотогалерея (редактирование)](/user_help/components/content/photogallery2/photogallery_gallery_edit.php)
[Фотогалерея (список)](/user_help/components/content/photogallery2/photogallery_gallery_list.php)
[Фотогалерея (шаблоны)](/user_help/components/content/photogallery2/photogallery_interface.php)
[Flash-слайдшоу](/user_help/components/content/photogallery2/photogallery_imagerotator.php)
[Альбом (редактирование обложки)](/user_help/components/content/photogallery2/photogallery_section_edit_icon.php)
[Альбом (редактирование)](/user_help/components/content/photogallery2/photogallery_section_edit.php)
[Список фото (со слайдером)](/user_help/components/content/photogallery2/photogallery_detail_list_ex.php)
[Фото](/user_help/components/content/photogallery2/photogallery_detail.php)
[Фото (загрузка)](/user_help/components/content/photogallery2/photogallery_upload.php)
[Фото (комментарии)](/user_help/components/content/photogallery2/photogallery_detail_comment.php)
[Фото (редактирование)](/user_help/components/content/photogallery2/photogallery_detail_edit.php)
[Фото (список)](/user_help/components/content/photogallery2/photogallery_detail_list.php)

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

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

Альбом

# Альбом

### Описание **photogallery.section**

Компонент выводит информацию об одном альбоме:

* обложку альбома;
* ссылку на редактирование свойств альбома;
* ссылку на страницу редактирования обложки альбома;
* ссылку на удаление альбома;
* ссылки на список альбомов, на добавление альбома, на загрузку фотографий.

Вместе с данным компонентом на странице обычно используется компонент [Фото (список)](/user_help/components/content/photogallery2/photogallery_detail_list.php), который выводит список фотографий данного альбома. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Контент > Фотогалерея 2.0*.

Компонент относится к модулю [Фотогалерея](/user_help/content/iblock/photogallery/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| ID раздела | **SECTION\_ID** | Указывается числовой код, в котором передается идентификатор раздела. Поле может быть оставлено пустым, если указан **Код раздела**. |
| Код раздела | **SECTION\_CODE** | Указывается символьный код раздела, из которого будут выбраны фотографии. Поле может быть оставлено пустым, если указан **ID раздела**. |
| Код фотогалереи | **USER\_ALIAS** | Задается переменная, в которой будет передаваться символьный код галереи. |
| Режим работы фотогалереи | **BEHAVIOUR** | Указывается режим работы фотогалереи:  * **пустое поле** - простой режим, т.е. один пользователь; * **USER** - многопользовательский режим.  Если параметр принимает значение **USER**, то необходимо настроить параметр **GALLERY\_URL** и **GALLERY\_SIZE**. |
| **Шаблоны ссылок** | | |
| Список разделов | **SECTIONS\_TOP\_URL** | Указывается адрес страницы со списком разделов (альбомов). |
| URL страницы с содержимым раздела | **SECTION\_URL** | Указывается адрес страницы с содержимым раздела (альбома). |
| Альбом (редактирование) | **SECTION\_EDIT\_URL** | Указывается адрес страницы редактирования параметров альбома. Страница может быть создана с помощью компонента [Альбом (редактирование)](/user_help/components/content/photogallery2/photogallery_section_edit.php). |
| Альбом (редактирование обложки) | **SECTION\_EDIT\_ICON\_URL** | Указывается адрес страницы выбора обложки альбома. Страница может быть создана с помощью компонента [Альбом (редактирование обложки)](/user_help/components/content/photogallery2/photogallery_section_edit_icon.php). |
| Страница слайд-шоу | **DETAIL\_SLIDE\_SHOW\_URL** | Указывается адрес страницы просмотра слайд-шоу. |
| Загрузка фото | **UPLOAD\_URL** | Указывается адрес страницы загрузки фотографий. Страница может быть создана с помощью компонента [Фото (загрузка)](/user_help/components/content/photogallery2/photogallery_upload.php). |
| Содержимое галереи | **GALLERY\_URL** | Указывается адрес страницы просмотра содержимого галереи. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Формат вывода даты | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Размер альбома (px) | **ALBUM\_PHOTO\_SIZE** | Указывается размер картинки обложки фотоальбома в пикселях (px). Размер задается для одной стороны картинки, вторая будет высчитана пропорционально для загружаемого изображения. |
| Размер картинки-анонса альбома (px) | **ALBUM\_PHOTO\_THUMBS\_SIZE** | Указывается размер картинки-анонса фотоальбома в пикселях (px). Размер задается для одной стороны картинки, вторая будет высчитана пропорционально для загружаемого изображения. |
| Возвращать массив данных альбома | **RETURN\_SECTION\_INFO** | [Y|N] При отмеченной опции компонент будет возвращать массив данных альбома. |
| Устанавливать статус 404, если не найдены элемент или раздел | **SET\_STATUS\_404** | [Y|N] При отмеченной опции будет установлен статус 404, если не будут найдены элементы или раздел фотогалереи. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **<название\_альбома>**. |
| Размер фотогалереи | **GALLERY\_SIZE** | Указывается размер галереи пользователя в Мб. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:photogallery.section","",Array(
		"IBLOCK_TYPE" => "gallery",
		"IBLOCK_ID" => "9",
		"SECTION_ID" => $_REQUEST["SECTION_ID"],
		"SECTION_CODE" => "",
		"USER_ALIAS" => "",
		"BEHAVIOUR" => "USER",
		"INDEX_URL" => "index.php",
		"SECTION_URL" => "section.php?SECTION_ID=#SECTION_ID#",
		"SECTION_EDIT_URL" => "section_edit.php?SECTION_ID=#SECTION_ID#",
		"SECTION_EDIT_ICON_URL" => "section_edit_icon.php?SECTION_ID=#SECTION_ID#",
		"DETAIL_SLIDE_SHOW_URL" => "slide_show.php?SECTION_ID=#SECTION_ID#&ELEMENT_ID=#ELEMENT_ID#",
		"UPLOAD_URL" => "upload.php?SECTION_ID=#SECTION_ID#",
		"DATE_TIME_FORMAT" => "d.m.Y",
		"ALBUM_PHOTO_SIZE" => "150",
		"ALBUM_PHOTO_THUMBS_SIZE" => "70",
		"RETURN_SECTION_INFO" => "Y",
		"SET_STATUS_404" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"SET_TITLE" => "Y"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх