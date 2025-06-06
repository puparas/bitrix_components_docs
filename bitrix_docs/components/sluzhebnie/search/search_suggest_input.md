# Поле ввода поискового запроса

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

[Облако тегов](/user_help/components/sluzhebnie/search/search_tags_cloud.php)
[Поиск по заголовкам](/user_help/components/sluzhebnie/search/search_title.php)
[Поле ввода поискового запроса](/user_help/components/sluzhebnie/search/search_suggest_input.php)
[Стандартная страница поиска](/user_help/components/sluzhebnie/search/search_page.php)
[Форма ввода тегов](/user_help/components/sluzhebnie/search/search_tags_input.php)
[Форма поиска](/user_help/components/sluzhebnie/search/search_form.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

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

[Поиск](/user_help/components/sluzhebnie/search/index.php)

Поле ввода поискового запроса

# Поле ввода поискового запроса

### Описание **search.suggest.input**

Компонент служит для вывода поля ввода поискового запроса с подсказкой. Компонент стандартный и входит в дистрибутив модуля.

Компонент относится к модулю [Поиск](/user_help/settings/search/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Имя поля ввода | **NAME** | Указывается имя поля ввода. |
| Содержимое поля ввода | **VALUE** | Указывается текст, который будет отображаться в поле ввода по умолчанию. |
| Размер поля ввода | **INPUT\_SIZE** | Задается ширина поля ввода в символах. |
| Размер выпадающего списка | **DROPDOWN\_SIZE** | Задается количество пунктов, отображаемых в выпадающем списке. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:search.suggest.input","",Array(
		"NAME" => "search1",
		"VALUE" => "Поиск",
		"INPUT_SIZE" => "60",
		"DROPDOWN_SIZE" => "10"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх