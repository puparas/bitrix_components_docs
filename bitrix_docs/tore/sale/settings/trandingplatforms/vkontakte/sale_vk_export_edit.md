# Создание и редактирование профиля экспорта

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

[Мастер магазина](/user_help/store/storeassist.php)

[Интернет-магазин](/user_help/store/sale/index.php)

[Интернет-магазин. Настройки модуля](/user_help/store/sale/settings_sale.php)
[Конвертация интернет-магазина](/user_help/store/sale/sale_converter.php)
[Интеграция с CRM](/user_help/store/sale/sale_crm.php)
[Синхронизация заказов с Б24](/user_help/store/sale/sale_order_crm.php)

[Заказы](/user_help/store/sale/orders/index.php)

[Кассы ККМ](/user_help/store/sale/cashbox/index.php)

[Покупатели](/user_help/store/sale/user_accounts/index.php)

[Аффилиаты](/user_help/store/sale/affiliates/index.php)

[Отчеты](/user_help/store/sale/statistic/index.php)

[Настройки магазина](/user_help/store/sale/settings/index.php)

[Платежные системы](/user_help/store/sale/settings/sale_pay_system.php)
[Создание и редактирование платежной системы](/user_help/store/sale/settings/sale_pay_system_edit.php)
[Настройка возвратов](/user_help/store/sale/settings/sale_ps_handler_refund.php)
[Обработчики платежных систем](/user_help/store/sale/settings/sale_pay_system_file.php)
[Компании](/user_help/store/sale/settings/sale_company.php)
[Создание и редактирование компании](/user_help/store/sale/settings/sale_company_edit.php)
[Типы плательщиков](/user_help/store/sale/settings/sale_person_type.php)
[Создание и редактирование типа плательщика](/user_help/store/sale/settings/sale_person_type_edit.php)
[Статусы](/user_help/store/sale/settings/sale_status.php)
[Создание и редактирование информационного статуса заказа](/user_help/store/sale/settings/sale_status_edit.php)
[Соответствие значений бизнес-смыслу](/user_help/store/sale/settings/sale_business_value.php)
[Интеграция с 1С](/user_help/store/sale/settings/1c_admin.php)
[Печатные формы](/user_help/store/sale/settings/print_form.php)
[Единицы измерения](/user_help/store/sale/settings/cat_measure_list.php)
[Создание и редактирование единицы измерения](/user_help/store/sale/settings/cat_measure_edit.php)

[Экспорт](/user_help/store/sale/settings/export/index.php)

[Импорт](/user_help/store/sale/settings/import/index.php)

[Свойства заказа](/user_help/store/sale/settings/order_props/index.php)

[Службы доставки](/user_help/store/sale/settings/delivery/index.php)

[Местоположения](/user_help/store/sale/settings/location2/index.php)

[Налоги](/user_help/store/sale/settings/tax/index.php)

[Торговые платформы](/user_help/store/sale/settings/trandingplatforms/index.php)

[Товары ВКонтакте](/user_help/store/sale/settings/trandingplatforms/vkontakte/index.php)

[Список профилей экспорта в магазин ВКонтакте](/user_help/store/sale/settings/trandingplatforms/vkontakte/sale_vk_export_list.php)
[Создание и редактирование профиля экспорта](/user_help/store/sale/settings/trandingplatforms/vkontakte/sale_vk_export_edit.php)

[Цены](/user_help/store/sale/settings/prices/index.php)

[Торговый каталог](/user_help/store/catalog/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

...

[Настройки магазина](/user_help/store/sale/settings/index.php)

[Торговые платформы](/user_help/store/sale/settings/trandingplatforms/index.php)

[Товары ВКонтакте](/user_help/store/sale/settings/trandingplatforms/vkontakte/index.php)

Создание и редактирование профиля экспорта (доступно с версии 17.0.0)

**Недоступно в редакциях:**Стандарт, Старт

# Создание и редактирование профиля экспорта

### Настройки

Данная форма служит для настройки параметров соединения с ВКонтакте.

| Поле | Описание |
| --- | --- |
| Название | Название профиля экспорта для отображения в административном разделе сайта. |
| Настройки соединения | |
| ID приложения | Идентификатор приложения ВКонтакте. Может быть получен в настройках созданного вами приложения. |
| Защищенный ключ | Ключ приложения ВКонтакте, необходимый для внешнего доступа к нему. Может быть получен в настройках созданного вами приложения. |
| После сохранения введенных данных вам станет доступна ссылка **Получить ключ доступа**, при нажатии на которую система затребует разрешение на доступ к вашей группе ВКонтакте. Согласитесь с требованиями и ключ доступа будет получен и сохранен. После получения ключа вам станут доступны дополнительные опции. **Примечание**: Если вы используете технологию многосайтовость на разных доменах    **Многосайтовость на разных доменах** – это название технологии создания сайтов, при которой ядро продукта устанавливается в папку одного из сайтов, а для остальных сайтов настраиваются символьные ссылки (симлинки). Эту технологию можно реализовать и на разных доменах, и на поддоменах.   [Подробнее](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=103&LESSON_ID=287)... , то для получения/переполучения ключа доступа нужно открыть административную часть интернет-магазина с того домена, который указан в настройках приложения Вконтакте (в противном случае появится ошибка `"redirect_uri has wrong domain, check application settings"`). | |
| Настройки ВКонтакте | |
| Группа для импорта товаров | Выбирается группа ВКонтакте, в которую планируется произвести экспорт. Поле доступно после получения ключа доступа. |
| Настройки разделов каталога | |
| Категория ВКонтакте по умолчанию | Категория для добавления товаров. Выбор производится из фиксированного списка. Настройка является обязательной для добавления товаров.  Выбор и настройка разделов, которые будут экспортироваться ВКонтакте, производится на вкладке [Торговые платформы](/user_help/store/catalog/products/cat_section_edit.php#platform) формы редактирования раздела.   Поле доступно после получения ключа доступа. |
| Настройки экспорта | |
| Секция доступна после получения ключа доступа | |
| Перезаписывать изменения | При включении данной опции экспорт будет перезаписывать все изменения, сделанные с товарами ВКонтакте (т.е. если вы произвели экспорт, а затем вручную изменили товар ВКонтакте, то следующий обмен приведет товар в соответствие с сайтом). |
| Экспортировать только доступные товары | При отмеченной опции экспортироваться будут только доступные к покупке товары. |
| Максимальное время выполнения одного шага | Максимальное время выполнения одного шага экспорта в секундах (при стабильной работе не рекомендуется изменять это значение). |
| Количество элементов, обрабатываемых за шаг (не более 25) | Количество товаров, которое обрабатывается за один шаг (при стабильной работе не рекомендуется изменять это значение). |
| Расширенный лог ошибок | При отмеченной опции будет составлять полный лог ошибок. |

### Карта экспорта

Во вкладке отображается список разделов каталога,
отмеченных для экспорта



В административной части сайта перейдите в Магазин > Каталог товаров > Разделы и с помощью пункта контекстного меню **Изменить** произведите настройку экспорта каждого раздела. Необходимые нам настройки расположены на вкладке **Торговые платформы**.
  
  
[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=8695)...
.

| Поле | Описание |
| --- | --- |
| Название | Название профиля экспорта для отображения в административном разделе сайта. |
| Альбом ВКонтакте | Название альбома Вконтакте, в который осуществляется экспорт товаров. |
| Количество товаров | Количество экспортируемых товаров. |
| Разделы каталога | Разделы каталога, товары из которых будут экспортированы в альбом Вконтакте. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх