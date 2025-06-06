# Упрощенный HTML-редактор

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

Упрощенный HTML-редактор

# Упрощенный HTML-редактор

### Описание **fileman.light\_editor**

Компонент выводит упрощенный визуальный HTML-редактор. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Упрощенный HTML-редактор*.

Компонент относится к модулю [Управление структурой](/user_help/content/fileman/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные настройки** | | |
| Содержимое | **CONTENT** | Задается произвольный текст, который будет отображен в поле редактора. |
| Имя элемента управления | **INPUT\_NAME** | Указывается имя текстового поля (добавляется в **Содержимое**). Необходимо для обработки сообщения при вводе. |
| ID элемента управления | **INPUT\_ID** | Указывается идентификатор элемента управления. Если данные из текстового поля будут обрабатываться с помощью JavaScript, то сам элемент удобно "взять" зная это ID. |
| Ширина редактора | **WIDTH** | Указывается ширина окна редактора в пикселях (px) или в процентах (%). |
| Высота редактора | **HEIGHT** | Указывается высота окна редактора в пикселях (px). |
| Разрешить пользователю изменять высоту области редактирования | **RESIZABLE** | [Y|N] При отмеченной опции пользователю будет разрешено изменять высоту области редактирования. |
| Автоматическое увеличение области редактирования при наборе текста | **AUTO\_RESIZE** | [Y|N] При отмеченной опции высота области редактирования будет автоматически увеличиваться по мере набора текста. Доступно только при отмеченной опции **Разрешить пользователю изменять высоту области редактирования**. |
| **Настройки вставки видео** | | |
| Разрешить вставку видео | **VIDEO\_ALLOW\_VIDEO** | [Y|N] При отмеченной опции будет разрешена вставка видео средствами упрощенного HTML-редактора. Станут доступны для заполнения дополнительные поля.     |  |  |  | | --- | --- | --- | | Максимальная ширина видео | **VIDEO\_MAX\_WIDTH** | Указывается максимальная ширина окна для видео в пикселях (px). | | Максимальная высота видео | **VIDEO\_MAX\_HEIGHT** | Указывается максимальная высота окна для видео в пикселях (px). | | Размер буфера в секундах | **VIDEO\_BUFFER** | Указывается размер буфера в секундах (т.е. промежуток времени ролика, который будет сохранен в буфер перед началом воспроизведения). Рекомендуется для медленного трафика. | | Путь к изображению авторского знака | **VIDEO\_LOGO** | Указывается путь к изображению авторского логотипа, который будет накладываться на видео. | | Режим окна (WMode) (Только для Flash-плеера) | **VIDEO\_WMODE** | Указывается режим окна только для Flash-плеера:  * **Обычный** (**window**) - медиафайл будет проигрываться на странице в собственном прямоугольном окне. Этот вариант дает наибольший выигрыш в скорости воспроизведения анимации; * **Непрозрачный** (**opaque**) - медиафайл будет помещен на задний план страницы. * **Прозрачный** (**transparent**) - фон страницы будет "проглядывать" через все прозрачные места медиафайла при проигрывании. Этот вариант может замедлить скорость воспроизведения анимации. | | Режим окна (windowless) (Только для Silverlight-плеера) | **VIDEO\_WINDOWLESS** | [Y|N] При отмеченной опции только для Silverlight-плеера будет использоваться режима окна **Прозрачный (windowless)**. Окно плеера будет отображаться непосредственно в клиентской области обозревателя или внутри специально созданного окна. | | Путь к скину (Только для Flash-плеера) | **VIDEO\_SKIN** | Указывается путь к скину только для Flash-плеера. Пользовательские скины должны храниться в директории, не затрагиваемой системой обновлений. | |
| **Дополнительные настройки** | | |
| Разрешить использование файлового диалога | **USE\_FILE\_DIALOGS** | [Y|N] При отмеченной опции будет разрешено использование файлового диалога системы (например, диалоги для указания путей загружаемых картинок или видеофайлов). |
| Служебный ID элемента управления | **ID** | Указывается служебный идентификатор элемента управления. Имеет значение при работе с API на JavaScript. |
| Имя Javascript-объекта | **JS\_OBJ\_NAME** | Указывается имя используемого JavaScript-объекта. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:fileman.light_editor","",Array(
	"CONTENT" => "",
	"INPUT_NAME" => "",
	"INPUT_ID" => "",
	"WIDTH" => "100%",
	"HEIGHT" => "300px",
	"RESIZABLE" => "Y",
	"AUTO_RESIZE" => "Y",
	"VIDEO_ALLOW_VIDEO" => "Y",
	"VIDEO_MAX_WIDTH" => "640",
	"VIDEO_MAX_HEIGHT" => "480",
	"VIDEO_BUFFER" => "20",
	"VIDEO_LOGO" => "",
	"VIDEO_WMODE" => "transparent",
	"VIDEO_WINDOWLESS" => "Y",
	"VIDEO_SKIN" => "/bitrix/components/bitrix/player/mediaplayer/skins/bitrix.swf",
	"USE_FILE_DIALOGS" => "Y",
	"ID" => "",	
	"JS_OBJ_NAME" => ""
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх