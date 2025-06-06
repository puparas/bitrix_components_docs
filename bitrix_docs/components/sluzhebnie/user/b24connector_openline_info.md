# Компонент для авторизации виджета Битрикс24.Онлайн-чат

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

Компонент для авторизации виджета Битрикс24.Онлайн-чат

# Компонент для авторизации виджета Битрикс24.Онлайн-чат

### Описание **b24connector.openline.info**

Компонент автоматически передаёт виджету контактные данные авторизованного клиента, позволяет настроить и дополнительно передаваемые данные.

В визуальном редакторе компонент расположен по пути: *Служебные > Пользователь*.

Компонент относится к модулю [Интеграция с Битрикс24](/user_help/clients/clientscomm.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| Поле | Параметр | Описание |
| **Управление адресами страниц** | | |
| Дополнительные данные | DATA | Любой текст, добавленный в это поле, транслируется в ОЛ. |
| Добавлять метку при отправке сообщения для Google Analytics | GA\_MARK | Указывается метка Google Analytics. На странице с компонентом должна быть [подключена Google Analytics](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=5818). Как только пользователь что-то напишет, то данная метка будет передана в аналитику для подсчета достижения цели (dataLayer, подробнее: [Google Analytics](https://ru.advertisercommunity.com/t5/Stati/DataLayer-v-Google-Tag-Manager-chto-eto-takoe-i-kak-rabotaet/ba-p/316473).) |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:b24connector.openline.info","", Array(
		"COMPOSITE_FRAME_MODE" => "A",
		"COMPOSITE_FRAME_TYPE" => "AUTO",
		"DATA" => "",
		"GA_MARK" => ""
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх