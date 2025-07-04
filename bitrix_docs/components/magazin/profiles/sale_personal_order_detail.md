|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Не показывать свойства для типа плательщика **<название\_плательщика>** |

| Для каждого типа плательщика **<название\_плательщика>** (**N** - идентификатор типа плательщика) задается массив свойств, которые не должны быть отображены. |
| **Внешний вид** |

| |
| Формат показа даты |

| Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Ограничение по ширине для анонсного изображения, px |

| Указывается ширина (в пикселах) изображения товара при подробном просмотре заказа. |
| Ограничение по высоте для анонсного изображения, px |

| Указывается высота (в пикселах) изображения товара при подробном просмотре заказа. |
| Тип масштабирования |

| Из выпадающего списка выбирается тип масштабирования изображений:  * С сохранением пропорций, улучшенная обработка; * С сохранением пропорций; * С обрезанием. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| Учитывать права доступа |

| [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** |

| |
| Страница со списком заказов |

| Указывается путь к странице со списком заказов. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Список заказов](/user_help/store/sale/components_2/personal/sale_personal_order_list.php). |
| Страница отмены заказа |

| Указывается путь к странице отмены заказа. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Отмена заказа](/user_help/store/sale/components_2/personal/sale_personal_order_cancel.php). Необходимо передавать идентификатор заказа в качестве параметра. |
| Страница повторения заказа |

| Указывается путь к странице повтора заказа. Можно указать путь к странице, где происходит копирование заказа. Если указать путь к корзине, то заказ будет скопирован и можно будет начать оформление заказа. |
| Страница подключения платежной системы |

| Указывается путь к странице подключения платежной системы. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Подключение платежной системы](/user_help/store/sale/components_2/order/sale_order_payment.php). |
| Идентификатор заказа |

| Указывается код, результатом которого является получение идентификатора заказа. По умолчанию **={$ID}**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Мой заказ № <идентификатор\_заказа>**. |
| Дополнительные свойства инфоблока |

| Задаются коды свойств инфоблока, которые необходимо вывести при детальном просмотре заказа. Следует задавать для вывода только строковые и числовые типы свойств. |
| Запретить смену платежной системы у заказов в статусах |

| Указываются статусы заказов по достижении которых нельзя сменить платёжную систему. |
| Пересчитывать заказ после смены платежной системы |

| Разрешение на пересчёт заказа после смены платёжной системы |
| Разрешить оплату с внутреннего счета |

| Разрешение на оплату с внутреннего счёта |
| Разрешить оплату с внутреннего счета только в полном объеме |

| Разрешение на оплату с внутреннего счёта при условии наличия на счёте полной суммы заказа. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sale.personal.order.detail","",Array(

		"PATH_TO_LIST" => "order_list.php",

		"PATH_TO_CANCEL" => "order_cancel.php",

		"PATH_TO_PAYMENT" => "payment.php",

		"PATH_TO_COPY" => "",

		"ID" => $ID,

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_GROUPS" => "Y",

		"SET_TITLE" => "Y",

		"ACTIVE_DATE_FORMAT" => "d.m.Y",

		"PICTURE_WIDTH" => "110",

		"PICTURE_HEIGHT" => "110",

		"PICTURE_RESAMPLE_TYPE" => "1",

		"CUSTOM_SELECT_PROPS" => array(),

		"PROP_1" => Array(),

		"PROP_2" => Array()

	)

);?>


```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 1  **Иван Рычков** 31.08.2020 13:58:52 |
| --- |
| Скрытый параметр GUEST\_MODE = Y/N отвечает за режим только для чтения. |
|  |

```
<?$APPLICATION->IncludeComponent("bitrix:sale.personal.order.detail","",Array(

		"PATH_TO_LIST" => "order_list.php",

		"PATH_TO_CANCEL" => "order_cancel.php",

		"PATH_TO_PAYMENT" => "payment.php",

		"PATH_TO_COPY" => "",

		"ID" => $ID,

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_GROUPS" => "Y",

		"SET_TITLE" => "Y",

		"ACTIVE_DATE_FORMAT" => "d.m.Y",

		"PICTURE_WIDTH" => "110",

		"PICTURE_HEIGHT" => "110",

		"PICTURE_RESAMPLE_TYPE" => "1",

		"CUSTOM_SELECT_PROPS" => array(),

		"PROP_1" => Array(),

		"PROP_2" => Array()

	)

);?>


```