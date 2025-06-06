# Кнопки социальных сетей

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

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Комментарии к товарам](/user_help/components/content/social_services/catalog_comments.php)
[Кнопки социальных сетей](/user_help/components/content/social_services/catalog_socnets_buttons.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

Кнопки социальных сетей

# Кнопки социальных сетей

### Описание **catalog.socnets.buttons**

Компонент служит для отображения кнопок социальных сетей и размещается на странице, информация которой может быть опубликована в социальных сервисах. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Социальные сервисы > Кнопки социальных сетей*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Адрес публикуемой страницы | **URL\_TO\_LIKE** | Задается адрес страницы, которая публикуется в социальном сервисе. |
| Заголовок публикации | **TITLE** | Заголовок публикации в социальном сервисе. |
| Текст публикации | **DESCRIPTION** | Описание публикации в сервисе. |
| Адрес изображения | **IMAGE** | Задается путь к изображению для публикации. |
| **Настройки Facebook\*** | | |
| Включить использование Facebook\* | **FB\_USE** | [Y|N] При отмеченной опции будет доступна кнопка сервиса Facebook\*. \* Социальная сеть признана экстремистской и запрещена на территории Российской Федерации. |
| **Настройки Twitter** | | |
| Включить использование Twitter | **TW\_USE** | [Y|N] При отмеченной опции будет отображаться кнопка сервиса Twitter, станут доступны дополнительные поля.     |  |  |  | | --- | --- | --- | | С помощью (via) | **TW\_VIA** | Указывается атрибут *via* - информация о владельце публикуемой страницы. | | Отметить (hashtags) | **TW\_HASHTAGS** | Указывается атрибут *hashtags* для публикации. | | Рекомендовать (related) | **TW\_RELATED** | Задается атрибут *related* для публикации. | |
| **Настройки В Контакте** | | |
| Включить использование ВКонтакте | **VK\_USE** | [Y|N] При отмеченной опции будет отображаться кнопка сервиса ВКонтакте. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.socnets.buttons","",
Array(
		"URL_TO_LIKE" => "/examples/article.php",
		"TITLE" => "Моя статья",
		"DESCRIPTION" => "",
		"IMAGE" => "/upload/images/myarticle.png",
		"FB_USE" => "Y",
		"TW_USE" => "Y",
		"GP_USE" => "Y",
		"VK_USE" => "Y",
		"TW_VIA" => "",
		"TW_HASHTAGS" => "",
		"TW_RELATED" => ""
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх