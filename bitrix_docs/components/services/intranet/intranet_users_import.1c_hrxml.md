# Импорт оргструктуры из 1С:ЗУП (hrxml)

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

[Расчетные листки сотрудников](/user_help/components/services/intranet/payroll_1c.php)
[Интерфейс 1с 8.2](/user_help/components/services/intranet/intranet_1c82_interface.php)
[Импорт оргструктуры из 1С:ЗУП](/user_help/components/services/intranet/intranet_users_import_1c.php)
[Импорт оргструктуры из 1С:ЗУП (hrxml)](/user_help/components/services/intranet/intranet_users_import.1c_hrxml.php)

[Задачи 1.0](/user_help/components/services/intranet/intranet_tasks/index.php)

[Календарь событий](/user_help/components/services/intranet/intranet_event/index.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Контроллер](/user_help/components/services/controller/index.php)

[Частые вопросы](/user_help/components/services/faq/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

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

[Интранет (КП)](/user_help/components/services/intranet/index.php)

Импорт оргструктуры из 1С:ЗУП (hrxml)

# Импорт оргструктуры из 1С:ЗУП (hrxml)

### Описание **intranet.users.import.1c.hrxml**

Компонент позволяет подключаться к "1С:ЗУП" и производить импорт организационной структуры в формате HR-XML. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Контент > Каталог > Импорт оргструктуры из 1С:ЗУП*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается тип инфоблока, в который будут импортироваться данные оргструктуры. |
| Инфоблок подразделений | **DEPARTMENTS\_IBLOCK\_ID** | Указывается инфоблок подразделений. |
| Инфоблок графика отсутствий | **ABSENCE\_IBLOCK\_ID** | Указывается инфоблок графика отсутствий. |
| Инфоблок кадровых перестановок | **STATE\_HISTORY\_IBLOCK\_ID** | Указывается инфоблок кадровых перестановок. |
| Сайт для привязки пользователей | **SITE\_ID** | Указывается идентификатор сайта, к которому будет привязка пользователей. |
| Группы, пользователям которых разрешена загрузка | **GROUP\_PERMISSIONS** | Указываются группы пользователей, которым разрешен импорт оргструктуры. |
| E-mail по умолчанию | **DEFAULT\_EMAIL** | Указывается e-mail, на который по умолчанию будут направляться информационные сообщения. Например, сообщения об успешном импорте, ошибках и т.д. |
| Формировать уникальный e-mail | **UNIQUE\_EMAIL** | [Y|N] При отмеченной опции будет формироваться уникальный e-mail |
| Шаблон автоматического формирования логина | **LOGIN\_TEMPLATE** | Указывается шаблон автоматического формирования логина пользователей. |
| Обновляемые свойства | **UPDATE\_PROPERTIES** | Указываются свойства, которые будут обновляться при импорте оргструктуры. |
| **Уведомление пользователей** | | |
| E-mail-уведомление новым пользователям | **EMAIL\_NOTIFY** | Выбор действия отсылки e-mail-уведомлений новым пользователям:  * **N** - не отсылать; * **E** - только если указан e-mail; * **Y** - всем. |
| Отсылать уведомления сразу | **EMAIL\_NOTIFY\_IMMEDIATELY** | [Y|N] При отмеченной опции e-mail-уведомлений новым пользователям будут отправлять сразу при импорте данных. |
| **LDAP** | | |
| XML-идентификатор свойства "Учетная запись AD" | **LDAP\_ID\_PROPERTY\_XML\_ID** | Указывается XML-идентификатор свойства "Учетная запись AD". |
| Сервер LDAP | **LDAP\_SERVER** | Указывается сервер LDAP. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:intranet.users.import.1c.hrxml","",
	Array(
		"IBLOCK_TYPE" => "structure",
		"DEPARTMENTS_IBLOCK_ID" => "5",
		"ABSENCE_IBLOCK_ID" => "3",
		"STATE_HISTORY_IBLOCK_ID" => "6",
		"SITE_ID" => "s1",
		"GROUP_PERMISSIONS" => array("1"),
		"FILE_SIZE_LIMIT" => "204800",
		"USE_ZIP" => "Y",
		"DEFAULT_EMAIL" => "admin@myexample.com",
		"UNIQUE_EMAIL" => "Y",		
		"LOGIN_TEMPLATE" => "user_#",
		"EMAIL_NOTIFY" => "E",
		"EMAIL_NOTIFY_IMMEDIATELY" => "Y",
		"UPDATE_PROPERTIES" => array("NAME", "SECOND_NAME", "LAST_NAME", "PERSONAL_PROFESSION", "PERSONAL_WWW", "PERSONAL_BIRTHDAY", "PERSONAL_ICQ", "PERSONAL_GENDER", "PERSONAL_PHOTO", "PERSONAL_PHONE", "PERSONAL_FAX", "PERSONAL_MOBILE", "PERSONAL_PAGER", "PERSONAL_STREET", "PERSONAL_CITY", "PERSONAL_STATE", "PERSONAL_ZIP", "PERSONAL_COUNTRY", "WORK_POSITION", "WORK_PHONE", "UF_DEPARTMENT", "UF_PHONE_INNER", "UF_INN", "UF_DISTRICT", "UF_SKYPE", "UF_TWITTER", "UF_LINKEDIN", "UF_XING", "UF_WEB_SITES", "UF_SKILLS", "UF_INTERESTS", "UF_BXDAVEX_CALSYNC", "UF_PUBLIC", "UF_WORK_BINDING", "UF_TIMEMAN", "UF_TM_MAX_START", "UF_TM_MIN_FINISH", "UF_TM_MIN_DURATION", "UF_TM_REPORT_REQ", "UF_TM_REPORT_TPL", "UF_TM_FREE", "UF_TM_TIME", "UF_TM_DAY", "UF_TM_REPORT_DATE", "UF_REPORT_PERIOD", "UF_DELAY_TIME", "UF_LAST_REPORT_DATE", "UF_SETTING_DATE", "UF_TM_ALLOWED_DELTA"),
		"LDAP_ID_PROPERTY_XML_ID" => ""
	),
false
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх