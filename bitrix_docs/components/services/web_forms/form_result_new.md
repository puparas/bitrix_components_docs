# Заполнение веб-формы

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

Заполнение веб-формы

**Недоступно в редакциях:**Старт

# Заполнение веб-формы

### Описание **form.result.new**

Компонент служит для вывода формы и добавления результата, т.е. для ее заполнения. Компонент стандартный и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Веб-формы > Заполнение веб-формы*.

Компонент относится к модулю [Веб-формы](/user_help/service/form/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| ID веб-формы | **WEB\_FORM\_ID** | Указывается идентификатор веб-формы.  Выбрав пункт **(другое)->**, можно задать внешний идентификатор веб-формы через **$\_REQUEST**. |
| **Внешний вид** | | |
| Игнорировать свой шаблон | **IGNORE\_CUSTOM\_TEMPLATE** | [Y|N] При отмеченной опции для отображения веб-формы будет использоваться шаблон формы по умолчанию, даже если создан свой шаблон. |
| Использовать расширенный вывод сообщений об ошибках | **USE\_EXTENDED\_ERRORS** | [Y|N] При отмеченной опции будет использован расширенный вывод сообщений об ошибках. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить параметр **SEF\_FOLDER**     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. |  . |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Параметры компонента** | | |
| Страница со списком результатов | **LIST\_URL** | Указывается адрес страницы со списком результатов. |
| Страница редактирования результата | **EDIT\_URL** | Указывается адрес страницы редактирования результата. |
| Страница с сообщением об успешной отправке | **SUCCESS\_URL** | Указывается путь к странице с сообщением об успешной отправке результата формы. Используется при отправке результата пользователем без прав редактирования результата. |
| Название дополнительного пункта в навигационной цепочке | **CHAIN\_ITEM\_TEXT** | Указывается название дополнительного пункта в навигационной цепочке. Если оставить незаполненным, то в навигационную цепочку пункт не добавляется. |
| Ссылка на дополнительном пункте в навигационной цепочке | **CHAIN\_ITEM\_LINK** | Указывается ссылка, которая будет показана на дополнительном пункте меню в навигационной цепочке. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:form.result.new","",Array(
		"SEF_MODE" => "Y", 
		"WEB_FORM_ID" => "$_REQUEST["WEB_FORM_ID"]", 
		"LIST_URL" => "result_list.php", 
		"EDIT_URL" => "result_edit.php", 
		"SUCCESS_URL" => "", 
		"CHAIN_ITEM_TEXT" => "", 
		"CHAIN_ITEM_LINK" => "", 
		"IGNORE_CUSTOM_TEMPLATE" => "Y", 
		"USE_EXTENDED_ERRORS" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600", 
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