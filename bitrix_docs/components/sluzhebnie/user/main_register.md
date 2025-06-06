# Настраиваемая регистрация

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

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[navigation](/user_help/components/sluzhebnie/navigation/index.php)

[Безопасность](/user_help/components/sluzhebnie/security/index.php)

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

[Поиск](/user_help/components/sluzhebnie/search/index.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

[Имя пользователя с тултипом](/user_help/components/sluzhebnie/user/main_user_link.php)
[Настраиваемая регистрация](/user_help/components/sluzhebnie/user/main_register.php)
[Параметры пользователя](/user_help/components/sluzhebnie/user/main_profile.php)
[Запрос согласия пользователя](/user_help/components/sluzhebnie/user/main_userconsent_request.php)
[Компонент для авторизации виджета Битрикс24.Онлайн-чат](/user_help/components/sluzhebnie/user/b24connector_openline_info.php)
[Пароли приложений](/user_help/components/sluzhebnie/user/main_app_passwords.php)
[Управление объединением профилей](/user_help/components/sluzhebnie/user/socserv_auth_split.php)
[Форма авторизации](/user_help/components/sluzhebnie/user/system_auth_form.php)
[Форма инициализации регистрации](/user_help/components/sluzhebnie/user/system_auth_initialize.php)
[Форма отписки от писем](/user_help/components/sluzhebnie/user/main_mail_unsubscribe.php)
[Форма подтверждения регистрации](/user_help/components/sluzhebnie/user/system_auth_confirmation.php)

[Статистика](/user_help/components/sluzhebnie/statistic/index.php)

[Соц. закладки и сети](/user_help/components/sluzhebnie/main_share.php)
[Упрощенный HTML-редактор](/user_help/components/sluzhebnie/fileman_light_editor.php)
[Форма обратной связи](/user_help/components/sluzhebnie/main_feedback.php)
[Элемент управления "Календарь"](/user_help/components/sluzhebnie/main_calendar.php)
[Элемент управления "Палитра"](/user_help/components/sluzhebnie/main_colorpicker.php)
[Элемент управления "Часы"](/user_help/components/sluzhebnie/main_clock.php)
[Журнал изменений](/user_help/components/sluzhebnie/event_list.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

Настраиваемая регистрация

# Настраиваемая регистрация

Компонент позволяет настроить форму регистрации на сайте.

### Описание **main.register**

Компонент позволяет:

* установить, какие параметры будут предложены пользователю для заполнения, какие из них будут обязательны для заполнения;
* настроить ЧПУ;
* установить настройки кеширования;
* регулировать дальнейшие переходы пользователя по страницам сайта после регистрации: по ссылке в параметре backurl или на страницу окончания регистрации и т.д.

Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Пользователь > Настраиваемая регистрация*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Поля, которые показывать в форме | **SHOW\_FIELDS** | Указываются [поля](https://dev.1c-bitrix.ru/api_help/main/reference/cuser/ "Допустимые поля пользователя - в описании класса CUser"), которые будут выведены в дополнение к стандартному набору в форме регистрации. Стандартными полями, обязательными для заполнения, являются:  * **Логин**; * **Пароль**; * **Подтверждение пароля**; * **Адрес E-mail**.  Дополнительными полями являются: имя, фамилия, отчество, профессия и другие личные данные. |
| Поля, обязательные для заполнения | **REQUIRED\_FIELDS** | Указываются обязательные для заполнения поля. Список допустимых значений такой же, что и в предыдущем пункте. |
| **Дополнительные настройки** | | |
| Автоматически авторизовать пользователей | **AUTH** | [Y|N] При отмеченной опции после регистрации пользователь будет автоматически авторизован на сайте. В противном случае после регистрации пользователю будет предоставлена к заполнению форма авторизации. |
| Отправлять пользователя по обратной ссылке, если она есть | **USE\_BACKURL** | [Y|N] При отмеченной опции пользователь будет отправлен по обратной ссылке, если она есть. При наличии в адресной строке параметра backurl пользователь будет перенаправлен по указанной в этом параметре ссылке после заполнения формы регистрации. |
| Страница окончания регистрации | **SUCCESS\_PAGE** | Указывается адрес страницы сайта, которая будет финальной страницей процедуры регистрации, и пользователь будет перенаправлен на нее в случае успешной регистрации. Если пользователь зарегистрирован и авторизован, то при переходе на страницу регистрации он попадет на страницу окончания регистрации.  **Примечание:** один из параметров (**USE\_BACKURL** или **SUCCESS\_PAGE**) лучше заполнить. Если отмечены **оба** параметра, то пользователь будет переведен по **обратной** ссылке. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Регистрация нового пользователя**. |
| Показывать доп. свойства | **USER\_PROPERTY** | Указываются дополнительные пользовательские свойства, если они заданы. |
| Название блока пользовательских свойств | **USER\_PROPERTY\_NAME** | Указывается название блока пользовательских свойств. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.register","",Array(
		"USER_PROPERTY_NAME" => "", 
		"SEF_MODE" => "Y", 
		"SHOW_FIELDS" => Array(), 
		"REQUIRED_FIELDS" => Array(), 
		"AUTH" => "Y", 
		"USE_BACKURL" => "Y", 
		"SUCCESS_PAGE" => "", 
		"SET_TITLE" => "Y", 
		"USER_PROPERTY" => Array(), 
		"SEF_FOLDER" => "/", 
		"VARIABLE_ALIASES" => Array()
	)
);?> 

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 11  **Роберт Басыров** 10.06.2009 14:59:46 |
| --- |
| **Задача**: Необходимо передалать регистрационную форму так, чтобы там появились обязательные поля ФИО, телефон и т.д.    **Решение**:    1. Скопировать стандартный шаблон компонента bitrix.system.auth.registration в папку шаблона сайта |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх