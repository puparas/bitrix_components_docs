# Просмотр результата

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

[Сервисы](/user_help/components/services/index.php)

[Видеоконференции (КП)](/user_help/components/services/video/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Контроллер](/user_help/components/services/controller/index.php)

[Частые вопросы](/user_help/components/services/faq/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Веб-форма (комплексный компонент)](/user_help/components/services/web_forms/form.php)
[Заполнение веб-формы](/user_help/components/services/web_forms/form_result_new.php)
[Просмотр результата](/user_help/components/services/web_forms/form_result_view.php)
[Редактирование результата](/user_help/components/services/web_forms/form_result_edit.php)
[Список результатов](/user_help/components/services/web_forms/form_result_list.php)
[Список своих результатов](/user_help/components/services/web_forms/form_result_list_my.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

Просмотр результата

**Недоступно в редакциях:**Старт

# Просмотр результата

### Описание **form.result.view**

Компонент служит для просмотра результата заполнения веб-формы. Обычно используется в сочетании с компонентом **Список результатов**. При самостоятельном использовании данного компонента необходимо явно указывать идентификатор результата, чтобы соответствующий результат веб-формы был выведен в публичном разделе. Компонент стандартный и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Веб-формы > Просмотр результата*.

Компонент относится к модулю [Веб-формы](/user_help/service/form/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| ID результата | **RESULT\_ID** | Указывается идентификатор результата. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **view** - cтраница просмотра результата. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| **Дополнительные настройки** | | |
| Отображение имени | **NAME\_TEMPLATE** | Указывается формат для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| **Параметры компонента** | | |
| Показать дополнительные поля веб-формы | **SHOW\_ADDITIONAL** | [Y|N] При отмеченной опции будут выведены дополнительные поля формы при их наличии. |
| Показать значение параметра ANSWER\_VALUE | **SHOW\_ANSWER\_VALUE** | [Y|N] При отмеченной опции для показа будет выведено значение параметра **ANSWER\_VALUE** вопроса веб-формы (выводится рядом со значением ответа). |
| Показать текущий статус результата | **SHOW\_STATUS** | [Y|N] При отмеченной опции статуса текущего результата будет отображатся на странице со списком результатов. |
| Страница редактирования результата | **EDIT\_URL** | Указывается адрес страницы редактирования результата. |
| Название дополнительного пункта в навигационной цепочке | **CHAIN\_ITEM\_TEXT** | Указывается название дополнительного пункта в навигационной цепочке. Если оставить незаполненным, то в навигационную цепочку пункт не добавляется. |
| Ссылка на дополнительном пункте в навигационной цепочке | **CHAIN\_ITEM\_LINK** | Указывается ссылка, которая будет показана на дополнительном пункте меню в навигационной цепочке. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:form.result.view","",Array(
		"SEF_MODE" => "Y", 
		"RESULT_ID" => "$_REQUEST[\"RESULT_ID\"]", 
		"SHOW_ADDITIONAL" => "Y", 
		"SHOW_ANSWER_VALUE" => "Y", 
		"SHOW_STATUS" => "Y", 
		"EDIT_URL" => "result_edit.php", 
		"NAME_TEMPLATE" => "#LAST_NAME# #NAME#",
		"CHAIN_ITEM_TEXT" => "", 
		"CHAIN_ITEM_LINK" => "", 
		"SEF_FOLDER" => "/", 
		"SEF_URL_TEMPLATES" => Array(
			"view" => "#RESULT_ID#/"
		),
		"VARIABLE_ALIASES" => Array(
			"view" => Array(),
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх