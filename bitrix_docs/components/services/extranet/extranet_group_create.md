# Экстранет - создание группы (комплексный компонент)

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

[Последние сообщения всех блогов экстранета](/user_help/components/services/extranet/extranet_blog_new_posts_list.php)
[Форма инициализации регистрации](/user_help/components/services/extranet/system_auth_initialize.php)
[Экстранет - создание группы (комплексный компонент)](/user_help/components/services/extranet/extranet_group_create.php)

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

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

Экстранет - создание группы (комплексный компонент)

# Экстранет - создание группы (комплексный компонент)

### Описание **extranet.group\_create**

Комплексный компонент служит для создания группы экстранета. Компонент является стандартным и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Общение > Социальная сеть > Экстранет - создание группы*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следущие параметры: **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. |
| Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - путь к странице создания группы; * **invite** - путь к странице приглашения пользователей. |
| Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами.   При **выключенном** режиме ЧПУ необходимо указать имена следующих переменных:  * **user\_id** - имя переменной для идентификатора пользователя; * **page** - имя переменной для страницы; * **group\_id** - имя переменной для идентификатора группы. |
| **Дополнительные настройки** | | |
| Страница группы | **PATH\_TO\_GROUP** | Указывается путь к странице группы экстранета. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:extranet.group_create","",Array(
		"SEF_MODE" => "Y",
		"PATH_TO_GROUP" => "",
		"SEF_FOLDER" => "/",
		"SEF_URL_TEMPLATES" => Array(
			"index" => "index.php",
			"invite" => "#group_id#/invite/"
		),
		"VARIABLE_ALIASES" => Array(
			"index" => Array(),
			"invite" => Array(),
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх