# Список страниц

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

[Управление](/user_help/components/landing/landing_start.php)
[Наполнение страницы](/user_help/components/landing/landing_landing_view.php)
[Предпросмотр шаблона](/user_help/components/landing/landing_demo_preview.php)
[Публикация страницы](/user_help/components/landing/landing_pub.php)
[Редактирование домена](/user_help/components/landing/landing_domain_edit.php)
[Редактирование сайта](/user_help/components/landing/landing_site_edit.php)
[Редактирование страницы](/user_help/components/landing/landing_landing_edit.php)
[Создание сайта / страницы по шаблону](/user_help/components/landing/landing_demo.php)
[Список доменов](/user_help/components/landing/landing_domains.php)
[Список сайтов](/user_help/components/landing/landing_sites.php)
[Список страниц](/user_help/components/landing/landing_landings.php)
[Фильтр](/user_help/components/landing/landing_filter.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сайты 24](/user_help/components/landing/index.php)

Список страниц

# Список страниц

### Описание **landing.landings**

Компонент служит для выводит список страниц сайта.
Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Сайты 24 > Список страница.*

Компонент относится к модулю [Сайты 24](/user_help/components/landing/index.php).

### Параметры

|  |  |  |  |
| --- | --- | --- | --- |
| **Поле** | **Параметр** | **Описание** | **Примечание** |
| **Дополнительные настройки** | | | |
| Тип сайта | **TYPE** | Выбирается тип сайта из списка:    * **Лендинг** * **Магазин** * **Проект** * **База знаний** * **Группы** |  |
| ID сайта (обязательно) | **SITE\_ID** | Указывается идентификатор сайта. |  |
| Ссылка на редактирование лендинга | **PAGE\_URL\_LANDING\_EDIT** | Прописывается ссылка на страницу редактирования лендинга. |  |
| Ссылка на просмотр (наполнение) лендинга | **PAGE\_URL\_LANDING\_VIEW** | Прописывается ссылка на страницу просмотра и наполнения лендинга. |  |

### Пример вызова

```

$APPLICATION-IncludeComponent(
	"bitrix:landing.landings",
	"",
	Array(
		"PAGE_URL_LANDING_EDIT" => "",
		"PAGE_URL_LANDING_VIEW" => "",
		"SITE_ID" => "",
		"TYPE" => "PAGE"
	)
);?>  

 
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх