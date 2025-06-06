# Форма добавления / редактирования

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

Форма добавления / редактирования

# Форма добавления / редактирования

Компонент осуществляет вывод формы создания (редактирования) элемента указанного информационного блока. Компонент стандартный и входит в дистрибутив модуля. В визуальном редакторе компонент расположен по пути: *Контент > Добавление элементов > Форма добавления / редактирования*. Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается информационный блок, элементы которого необходимо создавать (редактировать). |
| **Параметры компонента** | | |
| Статус после сохранения | **STATUS\_NEW** | Значение поля зависит от того в каком режиме используется инфоблок:  * **Обычный**: с какой активностью создаются элементы (активный/неактивный). * В режиме **документооборота**: указывается статус, в который переводятся элементы при их создании/редактировании. * В режиме **бизнес-процессов**: устанавливается статус **снять с публикации**. |
| Страница со списком своих элементов | **LIST\_URL** | Задается адрес страницы со списком доступных пользователю элементов. После обновления данных редирект происходит именно на эту страницу. |
| Использовать CAPTCHA | **USE\_CAPTCHA** | [Y|N] При отмеченной опции будет выводиться изображение и поле ввода **CAPTCHA** в форме добавления элемента. |
| Сообщение об успешном сохранении | **USER\_MESSAGE\_EDIT** | Задается сообщение, которое выводится при успешном сохранении элемента. |
| Сообщение об успешном добавлении | **USER\_MESSAGE\_ADD** | Задается сообщение, которое выводится при успешном добавлении элемента. |
| Размер полей ввода | **DEFAULT\_INPUT\_SIZE** | Указывается размер полей ввода в форме создания/редактирования элемента. |
| Использовать настройки инфоблока для обработки изображений | **RESIZE\_IMAGES** | [Y|N] При отмеченной функции элементы, добавленные через публичную часть будут преобразовываться согласно настройкам инфоблока. |
| **Свойства инфоблока** | | |
| Свойства, выводимые на редактирование | **PROPERTY\_CODES** | Указываются поля и свойства инфоблока, которые выводятся в форме создания/редактирования элемента. |
| Свойства, обязательные для заполнения | **PROPERTY\_CODES\_REQUIRED** | Указываются обязательно заполняемые поля и свойства инфоблока в форме создания/редактирования элемента.     **Примечание:** указанные здесь поля и свойства должны быть обязательно указаны в параметре **PROPERTY\_CODES**. |
| **Параметры доступа** | | |
| Группы пользователей, имеющие право на добавление/редактирование | **GROUPS** | Указываются группы пользователей, имеющие право на добавление/редактирование элементов инфоблока. |
| Редактирование возможно для статуса | **STATUS** | Значение поля зависит от того в каком режиме используется инфоблок:  * **Обычный**: в каком состоянии активности редактируются элементы (в любом - **any** или в неактивном - **N**). * В режиме **документооборота**: указываются статусы, находясь в которых элементы будут доступны для редактирования и удаления. * В режиме **бизнес-процессов**: бизнес-процессы аналогичны обычному инфоблоку. |
| Привязка к пользователю | **ELEMENT\_ASSOC** | Задается привязка к пользователю:  * **создателю** (**CREATED\_BY**) - привязка по создателю: в дальнейшем пользователю будут показаны только созданные им элементы. * **по свойству инфоблока -->** (**PROPERTY\_ID**) - привязка по свойству инфоблока. В этом случае доступен параметр **ELEMENT\_ASSOC\_PROPERTY**. |
| по свойству инфоблока --> | **ELEMENT\_ASSOC\_PROPERTY** | Указывается свойство, по которому выполняется привязка. |
| Ограничить кол-во элементов для одного пользователя | **MAX\_USER\_ENTRIES** | Указывается максимальное количество элементов, которые может добавить пользователь. |
| Ограничить кол-во рубрик, в которые можно добавлять элемент | **MAX\_LEVELS** | Указывается максимальное количество разделов инфоблока, в которые пользователь может добавить один и тот же элемент. |
| Разрешить добавление только на последний уровень рубрикатора | **LEVEL\_LAST** | [Y|N] При отмеченной опции пользователям разрешено добавлять элементы только в последний раздел дерева разделов инфоблока. |
| Максимальный размер загружаемых файлов, байт (0 - не ограничивать) | **MAX\_FILE\_SIZE** | Указывается максимальный размер загружаемых файлов. Если указано **0**, то размер файлов не ограничен. |
| Использовать визуальный редактор для редактирования текста анонса | **PREVIEW\_TEXT\_USE\_HTML\_EDITOR** | [Y|N] При отмеченной опции будет использоваться визуальный редактор для редактирования текста анонса. |
| Использовать визуальный редактор для редактирования подробного текста | **DETAIL\_TEXT\_USE\_HTML\_EDITOR** | [Y|N] При отмеченной опции будет использоваться визуальный редактор для редактирования подробного текста. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.     Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами. |  **SEF\_FOLDER**. |
| **Собственные названия полей** | | |
| \*поле\_инфоблока\* | **CUSTOM\_TITLE\_<поле\_инфоблока>** | Задаются названия полей инфоблока для отображения пользователям. Вместо **<поле\_инфоблока>** указывается следующее:  * **NAME** - наименование; * **TAGS** - теги; * **DATE\_ACTIVE\_FROM** - дата начала; * **DATE\_ACTIVE\_TO** - дата завершения; * **IBLOCK\_SECTION** - раздел инфоблока; * **PREVIEW\_TEXT** - текст анонса; * **PREVIEW\_PICTURE** - картинка анонса; * **DETAIL\_TEXT** - подробный текст; * **DETAIL\_PICTURE** - подробная картинка. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.element.add.form","",Array(
		"SEF_MODE" => "Y",
		"IBLOCK_TYPE" => "news",
		"IBLOCK_ID" => "1",
		"PROPERTY_CODES" => array("NAME","TAGS","DATE_ACTIVE_FROM","DATE_ACTIVE_TO","IBLOCK_SECTION","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT","DETAIL_PICTURE"),
		"PROPERTY_CODES_REQUIRED" => array("NAME","TAGS","DATE_ACTIVE_FROM","DATE_ACTIVE_TO","IBLOCK_SECTION","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT","DETAIL_PICTURE"),
		"GROUPS" => array("1"),
		"STATUS_NEW" => "2",
		"STATUS" => array("2"),
		"LIST_URL" => "",
		"ELEMENT_ASSOC" => "PROPERTY_ID",
		"ELEMENT_ASSOC_PROPERTY" => "",
		"MAX_USER_ENTRIES" => "100000",
		"MAX_LEVELS" => "100000",
		"LEVEL_LAST" => "Y",
		"USE_CAPTCHA" => "Y",
		"USER_MESSAGE_EDIT" => "",
		"USER_MESSAGE_ADD" => "",
		"DEFAULT_INPUT_SIZE" => "30",
		"RESIZE_IMAGES" => "Y",
		"MAX_FILE_SIZE" => "0",
		"PREVIEW_TEXT_USE_HTML_EDITOR" => "Y",
		"DETAIL_TEXT_USE_HTML_EDITOR" => "Y",
		"CUSTOM_TITLE_NAME" => "",
		"CUSTOM_TITLE_TAGS" => "",
		"CUSTOM_TITLE_DATE_ACTIVE_FROM" => "",
		"CUSTOM_TITLE_DATE_ACTIVE_TO" => "",
		"CUSTOM_TITLE_IBLOCK_SECTION" => "",
		"CUSTOM_TITLE_PREVIEW_TEXT" => "",
		"CUSTOM_TITLE_PREVIEW_PICTURE" => "",
		"CUSTOM_TITLE_DETAIL_TEXT" => "",
		"CUSTOM_TITLE_DETAIL_PICTURE" => "",
		"SEF_FOLDER" => "/",
		"VARIABLE_ALIASES" => Array(
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 5  **Алексей Борисенко** 06.11.2014 06:44:51 |
| --- |
| В рамках стандартного компонента системы Форма добавления/редактирования (iblock.element.add.form) на данный момент не реализована возможность добавлять описание к свойству типа "Файл". При необходимости добавления пользователем описание к файлу, нужно подправить компонент.  Для этого в файле компонента /bitrix/components/bitrix/iblock.element.add.form/component.php перед ~755 строкой  | Код | | --- | | ``` $sAction = "ADD";  ``` | вставить   | Код | | --- | | ``` foreach ($arUpdateValues['PROPERTY_VALUES'][#PROPERTY_ID#] as $k => &$value) {     if (isset($_REQUEST['DESCRIPTION'][#PROPERTY_ID#][$k])) {         $value = array(             'VALUE' => $value,             'DESCRIPTION' => $_REQUEST['DESCRIPTION'][#PROPERTY_ID#][$k],         );     } }  ``` | и в своем шаблоне использовать следующий input   | Код | | --- | | ``` <input type="text" name="DESCRIPTION[#PROPERTY_ID#][$k]" value="">  ``` | где #PROPERTY\_ID# - ID нашего свойства типа Файл. |
|  |

| 4  **Роберт Басыров** 29.05.2009 14:57:41 |
| --- |
| В рамках стандартного компонента системы Форма добавления/редактирования (iblock.element.add.form) на данный момент не реализована возможность ресайза согласно настройкам выставленным в административной части.  При необходимости добавления пользователями изображений в нужном размере на странице добавления элемента инфоблока вставьте в начало такой код   | Код | | --- | | ``` <?  AddEventHandler("iblock", "OnBeforeIBlockElementAdd", Array("MyClass", "OnBeforeIBlockElementAddHandler"));  class MyClass  {      // создаем обработчик события "OnBeforeIBlockElementAdd"      function OnBeforeIBlockElementAddHandler(&$arFields)      {          if (is_array($arFields["DETAIL_PICTURE"]))          {             if(copy($arFields["DETAIL_PICTURE"]["tmp_name"], $arFields["DETAIL_PICTURE"]["tmp_name"]."~"))             {               $arFields["PREVIEW_PICTURE"] = $arFields["DETAIL_PICTURE"];               $arFields["PREVIEW_PICTURE"]["tmp_name"] .= "~";               $arFields["PREVIEW_PICTURE"] = CIBlock::ResizePicture($arFields["PREVIEW_PICTURE"], array("WIDTH" => 100, "HEIGH" => 100, "METHOD" => "resample",));             }             $arFields["DETAIL_PICTURE"] = CIBlock::ResizePicture($arFields["DETAIL_PICTURE"], array("WIDTH" => 400, "HEIGHT" => 400, "METHOD" => "resample",));          }       }  }  ?> ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх