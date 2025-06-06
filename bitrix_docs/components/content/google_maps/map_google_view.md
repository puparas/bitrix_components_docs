# Google: настраиваемая карта

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

[Инструкция получения ключа API Google](/user_help/components/content/google_maps/map_google_key.php)
[Google: настраиваемая карта](/user_help/components/content/google_maps/map_google_view.php)
[Google: поиск по адресу](/user_help/components/content/google_maps/map_google_search.php)

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

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Google Maps](/user_help/components/content/google_maps/index.php)

Google: настраиваемая карта

# Google: настраиваемая карта

### Описание **map.google.view**

Одностраничный компонент осуществляет отображение карты с сервиса **Google Maps**. Компонент позволяет выводить саму карту, задавать на ней стартовую позицию и добавлять на карту дополнительную информацию. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Google Maps > Google: настраиваемая карта*.

Компонент относится к модулю [Управление структурой](/user_help/content/fileman/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Ключ JavaScript API | **API\_KEY** | Ключ можно получить по ссылке https://developers.google.com/maps/documentation/javascript/get-api-key. |
| Стартовый тип карты | **INIT\_MAP\_TYPE** | Указывается вид карты, который будет использоваться по умолчанию:  * **схема** (**MAP**) - схематичная карта с именами улиц и объектов; * **спутник** (**SATELLITE**) - карта в виде фото со спутника; * **гибрид** (**HYBRID**) - карта в виде фото со спутника с наложенной на нее схемой основных дорог и объектов. * **ландшафт** (**TERRAIN**) - карта рельефа местности. |
| Данные выводимые на карте | **MAP\_DATA** | По нажатию кнопки **Изменить** откроется окно **Настройки карты**, предназначенное для редактирования настроек карты: |
| Ширина карты | **MAP\_WIDTH** | Указывается ширина окна отображаемой карты в пикселях (px) или в процентах (%). Если параметр принмает значение **AUTO**, то ширина окна задается браузером, который будет растягивать его на все доступное место. |
| Высота карты | **MAP\_HEIGHT** | Указывается высота окна отображаемой карты в пикселях (px) или в процентах (%). |
| **Дополнительные настройки** | | |
| Элементы управления | **CONTROLS** | Указываются необходимые элементы управления, которые будут отображены на карте:  * **Кнопки масштаба** (**SMALL\_ZOOM\_CONTROL**) - кнопки **Увеличить масштаб** и **Уменьшить масштаб** для управления масштабированием; * **Тип карты** (**TYPECONTROL**) - кнопки **Схема**, **Спутник** или **Гибрид** для переключения типа карты; * **Шкала масштаба** (**SCALELINE**) - в левом нижнем углу будет отображена шкала масштаба, показывающая масштаб в футах/метрах/милях/километрах. |
| Настройки | **OPTIONS** | Задаются настройки для управление картой с помощью клавиатуры и мыши:  * **изменение масштаба колесом мыши** (**ENABLE\_SCROLL\_ZOOM**) - позволяет изменять масштаб вращением колеса мыши; * **изменение масштаба двойным щелчком мыши** (**ENABLE\_DBLCLICK\_ZOOM**) - позволяет изменять масштаб карты двойным кликом мыши: левая кнопка - увеличение, правая кнопка - уменьшение; * **перетаскивание карты** (**ENABLE\_DRAGGING**) - позволяет перетаскивать карту указателем мыши; * **управление с клавиатуры** (**ENABLE\_KEYBOARD**) - позволяет управлять картой с помощью кнопок **"+"**, **"-"**, **"стрелка вверх"**, **"стрелка вниз"**, **"стрелка влево"**, **"стрелка вправо"** на клавиатуре. |
| Идентификатор карты | **MAP\_ID** | Указывается идентификатор карты. Задается произвольный код из цифр и букв латинского алфавита, который можно использовать при создании собственных клиентских сценариев. |

### Пример вызова

```
 <?$APPLICATION->IncludeComponent("bitrix:map.google.view","",Array(
		"API_KEY" => "",
		"INIT_MAP_TYPE" => "HYBRID",
		"MAP_DATA" => "a:4:{s:10:
			\"google_lat\";d:54.7078924801;s:10:
			\"google_lon\";d:20.5828726435;s:12:
			\"google_scale\";i:16;s:10:
			\"PLACEMARKS\";a:1:{i:0;a:3:{s:4:
			\"TEXT\";s:99:
			\"ООО \"1С-Битрикс\", г. Калининград, Московский проспект, 261.\";s:3:
			\"LON\";d:20.58321596625391;s:3:
			\"LAT\";d:54.70787388449525;}}}",
		"MAP_WIDTH" => "600",
		"MAP_HEIGHT" => "500",
		"CONTROLS" => array(
			"SMALL_ZOOM_CONTROL",
			"TYPECONTROL",
			"SCALELINE"
		),
		"OPTIONS" => array(
			"ENABLE_SCROLL_ZOOM",
			"ENABLE_DBLCLICK_ZOOM",
			"ENABLE_DRAGGING",
			"ENABLE_KEYBOARD"
		),
		"MAP_ID" => "gm_1"
	)
);?> 

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 5  **Maks Sidorenko** 22.07.2009 18:41:03 |
| --- |
| В случае необходимости ручного формирования данных для поля MAP\_DATA это следует делать примерно так:  | Код | | --- | | ``` "MAP_DATA" => serialize(     array(        'google_lat' => 54.70803636999584,        'google_lon' => 20.582714080810547,        'google_scale' => 16,        'PLACEMARKS' => array(           array(              'TEXT' => "ООО\"1С-Битрикс\", офис,  Московский проспект, 261.",              'LON' => 20.582714080810547,              'LAT' => 54.70803636999584           ),        ),     )  ) ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх