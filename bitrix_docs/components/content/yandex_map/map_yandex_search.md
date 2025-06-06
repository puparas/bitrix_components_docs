# Яндекс: поиск по адресу

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

[Яндекс.Карты (системный компонент)](/user_help/components/content/yandex_map/map_yandex_system.php)
[Яндекс: настраиваемая карта](/user_help/components/content/yandex_map/map_yandex_view.php)
[Яндекс: поиск по адресу](/user_help/components/content/yandex_map/map_yandex_search.php)

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

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

Яндекс: поиск по адресу

# Яндекс: поиск по адресу

### Описание **map.yandex.search**

Одностраничный компонент осуществляет отображение карты с сервиса **Яндекс.Карты** и предоставляет возможность поиска по адресу. Поддержка детального поиска (по улице и дому) осуществляется в соответствии с возможностями сервиса **Яндекс.Карты**. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Яндекс.Карты > Яндекс.Карты: поиск по адресу*.

Компонент относится к модулю [Управление структурой](/user_help/content/fileman/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Стартовый тип карты | **INIT\_MAP\_TYPE** | Указывается вид карты, который будет использоваться по умолчанию:  * **схема** (**MAP**) - схематичная карта с именами улиц и объектов; * **спутник** (**SATELLITE**) - карта в виде фото со спутника; * **гибрид** (**HYBRID**) - карта в виде фото со спутника с наложенной на нее схемой основных дорог и объектов. * **народная карта** (**PUBLIC**) - карта, составляемая пользователями Яндекса. * **народный гибрид** (**PUBLIC\_HYBRID**) - карта в виде фото со спутника с наложенной на нее народной картой. |
| Ширина карты | **MAP\_WIDTH** | Указывается ширина окна отображаемой карты в пикселях (px) или в процентах (%). Если параметр принмает значение **AUTO**, то ширина окна задается браузером, который будет растягивать его на все доступное место. |
| Высота карты | **MAP\_HEIGHT** | Указывается высота окна отображаемой карты в пикселях (px) или в процентах (%). |
| Начальная позиция карты | **MAP\_DATA** | По нажатию кнопки **Изменить** откроется окно **Настройки карты**, предназначенное для редактирования настроек карты: |
| **Дополнительные настройки** | | |
| Элементы управления | **CONTROLS** | Указываются необходимые элементы управления, которые будут отображены на карте:  * **Панель инструментов** (**TOOLBAR**) - кнопки **Переместить карту**, **Увеличить** и **Измерить расстояние на карте**; * **Ползунок масштаба** (**ZOOM**) - ползунок масштаба для управления масштабированием карты; * **Кнопки масштаба** (**SMALLZOOM**) - кнопки **Увеличить масштаб** и **Уменьшить масштаб** для управления масштабированием; * **Мини-карта** (**MINIMAP**) - включает отображение схематичной карты с крупным масштабом в левом нижнем углу карты; * **Тип карты** (**TYPECONTROL**) - кнопки **Схема**, **Спутник** или **Гибрид** для переключения стартового типа карты; * **Шкала масштаба** (**SCALELINE**) - в правом нижнем углу будет отображена шкала масштаба, показывающая масштаб относительно 1 см карты. * **Поиск по карте** (**SEARCH**) - поле и кнопка для поиска по карте. |
| Настройки | **OPTIONS** | Задаются настройки для управление картой с помощью клавиатуры и мыши:  * **изменение масштаба колесом мыши** (**ENABLE\_SCROLL\_ZOOM**) - позволяет изменять масштаб вращением колеса мыши; * **изменение масштаба двойным щелчком мыши** (**ENABLE\_DBLCLICK\_ZOOM**) - позволяет изменять масштаб карты двойным кликом мыши: левая кнопка - увеличение, правая кнопка - уменьшение; * **изменение масштаба правой кнопкой мыши** (**ENABLE\_RIGHT\_MAGNIFIER**) - позволяет с помощью щелчка правой кнопки мыши выделить и увеличить нужную область карты; * **перетаскивание карты** (**ENABLE\_DRAGGING**) - позволяет перетаскивать карту указателем мыши; |
| Идентификатор карты | **MAP\_ID** | Указывается идентификатор карты. Задается произвольный код из цифр и букв латинского алфавита, который можно использовать при создании собственных клиентских сценариев. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:map.yandex.search",".default",array(
	"INIT_MAP_TYPE" => "MAP",
	"MAP_WIDTH" => "auto",
	"MAP_HEIGHT" => "500",
	"MAP_DATA" => "a:3:{s:10:
            \"yandex_lat\";d:54.704461192577305;s:10:
			\"yandex_lon\";d:20.51420630589147;s:12:
			\"yandex_scale\";i:13;}",
	"CONTROLS" => array(
		"TOOLBAR",
		"ZOOM",
		"MINIMAP",
		"TYPECONTROL",
		"SCALELINE"
	),
	"OPTIONS" => array(
		"ENABLE_DBLCLICK_ZOOM",
		"ENABLE_DRAGGING"
	),
	"MAP_ID" => "searchmap"
	)
);
?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх