# Просмотр pdf-файлов

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

[Агрегатор библиотек документов (КП)](/user_help/components/content/webdav/index.php)

[Задачи 2.0 (КП)](/user_help/components/content/tasks/index.php)

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

[Фотогалерея](/user_help/components/content/photogallery/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

[Google Maps](/user_help/components/content/google_maps/index.php)

[Highload инфоблоки](/user_help/components/content/highload/index.php)

[RSS](/user_help/components/content/rss/index.php)

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Медиа](/user_help/components/content/media/index.php)

[Медиа проигрыватель](/user_help/components/content/media/player.php)
[Видеотека](/user_help/components/content/media/iblock_tv.php)
[Просмотр pdf-файлов](/user_help/components/content/media/pdf_viewer.php)

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Медиа](/user_help/components/content/media/index.php)

Просмотр pdf-файлов

# Просмотр pdf-файлов

### Описание **pdf.viewer**

Одностраничный компонент осуществляет вывод и просмотр файлов формата pdf на сайте. Компонент является стандартным и входит в дистрибутив модуля. В визуальном редакторе компонент расположен по пути: *Контент > Медиа > Просмотр pdf-файлов*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительные параметры** | | |
| Идентификатор просмотрщика | **VIEWER\_ID** | Уникальный идентификатор компонента. Основной контейнер (dom-нода) будет иметь идентификатор `outerContainer_#Идентификатор#`. С его помощью производятся изменения в работе компонента, например: изменение стилей. |
| Путь к файлу | **PATH** | Указывается путь к файлу, который должен открыться. |
| Будет показан во фрейме | **IFRAME** | [Y/N]Если опция установлена, то перед выводом компонента будет очищен буфер страницы, а компонент вставит свои `<html><head>` теги так, как будто это отдельная страница. В этом режиме просмотрщик растягивается на всю ширину экрана. |
| Заголовок | **TITLE** | Если включен режим показа во фрейме, то в настройках можно указать заголовок окна. Если его не указать, то название по умолчанию **Просмотр pdf файла**. |
| Выводить кнопку печати | **PRINT** | [Y/N]Если включен режим показа во фрейме, то при установленной галочке будет выводиться кнопка для отправки файла на печать. |
| Высота | **HEIGHT** | Если не выбран режим показа во фрейме, то в этом поле указывается ширина просмотрщика (в пикселях). |
| Ширина | **WIDTH** | Если не выбран режим показа во фрейме, то в этом поле указывается высота просмотрщика (в пикселях). |
| Ссылка на страницу печати | **PRINT\_URL** | Если не выбран режим показа во фрейме, то по умолчанию кнопка печати не выводится. Если в этом поле указать ссылку, то при клике на кнопку печати произойдёт переход на эту ссылку. Предполагается, что при переходе пользователь увидит страницу, где установлен этот же компонент, но в режиме фрейма, т.к. печать в этом компоненте не работает при выводе в теле страницы. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
    "bitrix:pdf.viewer",
    "",
    Array(
        "HEIGHT" => "600",
        "IFRAME" => "N",
        "PATH" => "/upload/ISR6bMnaRq.pdf",
        "PRINT" => "N",
        "PRINT_URL" => "",
        "TITLE" => "",
        "VIEWER_ID" => "",
        "WIDTH" => "900"
    )
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх