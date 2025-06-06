# Меню для мобильной платформы

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

[Выбор сайта](/user_help/components/sluzhebnie/navigation/main_site_selector.php)
[Меню](/user_help/components/sluzhebnie/navigation/menu.php)
[Меню для мобильной платформы](/user_help/components/sluzhebnie/navigation/mobileapp_menu.php)
[Навигационная цепочка](/user_help/components/sluzhebnie/navigation/breadcrumb.php)
[Пункты меню](/user_help/components/sluzhebnie/navigation/menu_section.php)

[Безопасность](/user_help/components/sluzhebnie/security/index.php)

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

[Поиск](/user_help/components/sluzhebnie/search/index.php)

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

[navigation](/user_help/components/sluzhebnie/navigation/index.php)

Меню для мобильной платформы

# Меню для мобильной платформы

### Описание **mobileapp.menu**

Компонент служит для построения меню мобильного приложения административной части интернет - магазина .

В визуальном редакторе компонент расположен по пути: *Служебные > Навигация > Меню для мобильной платформы*.

Компонент относится к модулю [Мобильное приложение](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=80&LESSON_ID=5466).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| Путь к скриптам | **SYNC\_REQUEST\_PATH** | Указывается путь, где расположены административные скрипты |
| Путь к файлу меню | **MENU\_FILE\_PATH** | Указывается путь |
| Имя события | **BUILD\_MENU\_EVENT\_NAME** | Наименование события формирования пунктов меню |
| Заголовок меню | **MENU\_TITLE** | Указывается заголовок |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
'bitrix:mobileapp.menu',
'.default',
[
'SYNC_REQUEST_PATH' => '/bitrix/admin/mobile',
'MENU_FILE_PATH' => '/bitrix/admin/mobile/.mobile_menu.php',
'BUILD_MENU_EVENT_NAME' => 'OnBeforeAdminMobileMenuBuild',
'MENU_TITLE' => 'Администратор'
],
false,
Array('HIDE_ICONS' => 'Y'));
?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх