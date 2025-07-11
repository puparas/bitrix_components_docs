| Действия | ID | Название | Файл | Профиль | Меню | Агент | Cron | Использован | Кем изменен | Дата изменения |
| --- |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [1] |

| [3] | [4] | [5] | [6] | [7] | [8] | [9] | [10] | [11] |

| Поле | Описание |
| --- |

|
| [1] Действия | Операции, которые могут быть применены к профилю/скрипту экспорта:  * **Экспортировать** - запуск профиля экспорта.* **Добавить профиль** - запуск профиля импорта с возможностью сохранения схемы импорта. Действие недоступно для пользовательских профилей.   * **Список переменных** - отображает в отдельном окне форму со списком экспортируемых элементов.   * **Редактировать** - открывает параметры профиля для изменения. Действие доступно только для пользовательских профилей.   * **Копировать** - копирует параметры профиля в форму создания нового профиля. Действие доступно только для пользовательских профилей.   * **Добавить в меню** - добавление ссылки на профиль экспорта в левое меню административной части сайта. Если ссылка добавлена, то вместо данного пункта отображается **Удалить из меню**.* **Создать агента** - создание PHP функции-агента для автоматического экспорта с использованием данного профиля.* **Повесить на cron** - привязка профиля к системной утилите `cron` для автоматического экспорта.* **Удалить профиль** - удаление профиля. Действие недоступно для профиля "по умолчанию". |
| [2] ID |

|
| [3] Название | Название типа профиля экспорта, например, Yandex, Froogle. **Примечание:**  Для экспорта данных в файлы формата CSV доступно два типа профиля:    **Export CSV**(**new**) - данный формат экспорта доступен при установленном в системе модуле Торговый каталог версии 4.0.5 и старше. Этот формат позволяет выгружать данные с учётом группировки цен товаров, в зависимости от количества приобретаемых товаров, а также снимает ограничение с количества объединяемых таблиц, содержащих информацию о товарах. Кроме того, данный формат позволяет выгружать цены товара в валюте, указанной для каждой цены.    **Export CSV**- данный формат выгрузки используется в системах с версией модуля Торговый каталог ниже 4.0.5. Этот формат накладывает ограничение на количество объединяемых таблиц с информацией о товарах (не более 30), а также не позволяет осуществлять выгрузку групп цен товаров. Кроме того, этот формат позволяет выгружать цены товара только в одной, единой для всех цен товара, валюте.  Если вы не используете разбивку цен товаров торгового каталога в зависимости от количества приобретаемых единиц товара, то данный тип экспорта может быть использован и для старших (4.0.5 и выше) версий модуля **Торговый каталог**. |
| [4] Файл |

|
| [5] Профиль | Название профиля выгрузки.    Профиль "по умолчанию" перед экспортом всегда запрашивает информационный блок, который требуется выгрузить. При экспорте с использованием пользовательского профиля, экспорт осуществляется автоматически, при этом выгружается именно тот информационный блок, который был выбран при создании профиля. |
| [6] Меню |

|
| [7] Агент | Указывает, существует ли агент, осуществляющий в случае необходимости (по истечении определённого интервала времени) автоматическую выгрузку элементов каталога. Создать агента для профиля можно при помощи действия **Создать агента** в колонке **Действия**. |
| [8] Cron |

|
| [9] Использован | Дата и время последнего экспорта с использованием данного профиля. |
| [10] Кем изменен |