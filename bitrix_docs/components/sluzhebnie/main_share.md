# Соц. закладки и сети

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

Соц. закладки и сети

# Соц. закладки и сети

### Описание **main.share**

Компонент выводит панель закладок со значками соц. сетей. Он позволяет быстро запустить окно соц. сети и оставить сообщение о вашей странице сайта, например, о новостях или сообщениях форума и т.д. Компонент является стандартным и входит в дистрибутив модуля.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительно** | | |
| Скрыть панель закладок по умолчанию | **HIDE** | [Y|N] При отмеченной опции панель со значками соц. сетей будет скрыта по умолчанию. При работе с сайтом пользователь сможет развернуть ее. |
| Используемые соц. закладки и сети | **HANDLERS** | В виде массива перечисляются соц.закладки и сети, которые требуется отобразить в выводимой панели. |
| URL страницы относительно корня сайта | **PAGE\_URL** | На основании введенного URL будет сформирована ссылка, ведущая на вашу страницу. Ссылка отобразится по умолчанию в коротком сообщении в выбранной соц. сети. |
| Заголовок страницы | **PAGE\_TITLE** | Введенный заголовок страницы будет использован при формировании сообщения пользователя, размещающего микроблог. |
| Логин для bit.ly | **SHORTEN\_URL\_LOGIN** | Зарегистрируйтесь на ресурсе <http://bit.ly/> и введите ваш логин оттуда. |
| Ключ API для bit.ly | **SHORTEN\_URL\_KEY** | После регистрации на ресурсе <http://bit.ly/> вы получите **API Key**. Его необходимо ввести в данном поле. После проведенных настроек ссылка на ваш сайт будет автоматически укорачиваться средствами **bit.ly** и примет такой вид **http://bit.ly/aLj59v**. Данная технология применена к **twitter**, где критична длина сообщения. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.share","",Array(
	"HIDE" => "N",
	"HANDLERS" => array
         ("delicious","twitter","vk"),
	"PAGE_URL" => "/examples/test.php",
	"PAGE_TITLE" => "Моя страница",
	"SHORTEN_URL_LOGIN" => "my_login",
	"SHORTEN_URL_KEY" => "K_edgd354df5454g5dg1b34a6cd1b10ffe05e30",
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх