|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Ключ доступа |

| Указывается ключ доступа, который получается у компании **Яндекс**. Без ключа карта работать не будет. |
| Стартовый тип карты |

| Указывается вид карты, который будет использоваться по умолчанию:  * **схема** (**MAP**) - схематичная карта с именами улиц и объектов; * **спутник** (**SATELLITE**) - карта в виде фото со спутника; * **гибрид** (**HYBRID**) - карта в виде фото со спутника с наложенной на нее схемой основных дорог и объектов. |
| Ширина карты |

| Указывается ширина окна отображаемой карты в пикселях (px) или в процентах (%). Если параметр принмает значение **AUTO**, то ширина окна задается браузером, который будет растягивать его на все доступное место. |
| Высота карты |

| Указывается высота окна отображаемой карты в пикселях (px) или в процентах (%). |
| **Дополнительные настройки** |

| |
| Элементы управления |

| Указываются необходимые элементы управления, которые будут отображены на карте:  * **Панель инструментов** (**TOOLBAR**) - кнопки **Переместить карту**, **Увеличить** и **Измерить расстояние на карте**; * **Ползунок масштаба** (**ZOOM**) - ползунок масштаба для управления масштабированием карты; * **Кнопки масштаба** (**SMALLZOOM**) - кнопки **Увеличить масштаб** и **Уменьшить масштаб** для управления масштабированием; * **Мини-карта** (**MINIMAP**) - включает отображение схематичной карты с крупным масштабом в левом нижнем углу карты; * **Тип карты** (**TYPECONTROL**) - кнопки **Схема**, **Спутник** или **Гибрид** для переключения стартового типа карты; * **Шкала масштаба** (**SCALELINE**) - в правом нижнем углу будет отображена шкала масштаба, показывающая масштаб относительно 1 см карты. |
| Настройки |

| Задаются настройки для управление картой с помощью клавиатуры и мыши:  * **изменение масштаба колесом мыши** (**ENABLE\_SCROLL\_ZOOM**) - позволяет изменять масштаб вращением колеса мыши; * **изменение масштаба двойным щелчком мыши** (**ENABLE\_DBLCLICK\_ZOOM**) - позволяет изменять масштаб карты двойным кликом мыши: левая кнопка - увеличение, правая кнопка - уменьшение; * **перетаскивание карты** (**ENABLE\_DRAGGING**) - позволяет перетаскивать карту указателем мыши; * **горячие клавиши** (**ENABLE\_HOTKEYS**) - позволяет управлять масштабом карты с помощью горячих клавиш. |
| Идентификатор карты |

```
<?$APPLICATION->IncludeComponent("bitrix:map.yandex.system", ".default", array(

	"KEY" => "",

	"INIT_MAP_TYPE" => "SATELLITE",

	"MAP_WIDTH" => "800",

	"MAP_HEIGHT" => "500",

	"CONTROLS" => array(

		0 => "TOOLBAR",

		1 => "ZOOM",

		2 => "MINIMAP",

		3 => "TYPECONTROL",

		4 => "SCALELINE",

	),

	"OPTIONS" => array(

		0 => "ENABLE_SCROLL_ZOOM",

		1 => "ENABLE_DBLCLICK_ZOOM",

		2 => "ENABLE_DRAGGING",				

		3 => "ENABLE_HOTKEYS",

	),

	"MAP_ID" => "testmap"

	)

);

?>
```