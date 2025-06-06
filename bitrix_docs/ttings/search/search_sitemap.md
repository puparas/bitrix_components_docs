# Google Sitemap

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

[Адреса и местоположения](/user_help/settings/location/index.php)

[Избранное](/user_help/settings/favorites/index.php)

[Пользователи](/user_help/settings/users/index.php)

[Поиск](/user_help/settings/search/index.php)

[Поиск. Настройки модуля](/user_help/settings/search/settings.php)
[Переиндексация](/user_help/settings/search/search_reindex.php)
[Google Sitemap](/user_help/settings/search/search_sitemap.php)
[Правила сортировки результатов поиска](/user_help/settings/search/search_customrank_admin.php)
[Создание и редактирование правила сортировки результатов поиска](/user_help/settings/search/search_customrank_edit.php)

[Статистика](/user_help/settings/search/statistic/index.php)

[Проактивная защита](/user_help/settings/security/index.php)

[DAV (КП)](/user_help/settings/dav/index.php)

[Push and Pull](/user_help/settings/pull/index.php)

[REST API](/user_help/settings/rest_api/index.php)

[Валюты](/user_help/settings/currency/index.php)

[Веб-кластер](/user_help/settings/cluster/index.php)

[Веб-сервисы](/user_help/settings/webservice/index.php)

[Диск (КП)](/user_help/settings/disk/index.php)

[Конвертер файлов (КП)](/user_help/settings/transformer/index.php)

[Коннекторы для внешних мессенджеров (КП)](/user_help/settings/imconnector/index.php)

[Открытые линии (КП)](/user_help/settings/imopenlines/index.php)

[Распознавание лиц (КП)](/user_help/settings/faceid/index.php)

[Сервер конвертации файлов (КП)](/user_help/settings/transformercontroller/index.php)

[Служба сообщений](/user_help/settings/message_service/index.php)

[Телефония](/user_help/settings/voximplant/index.php)

[Облако 1С-Битрикс](/user_help/settings/bitrixcloud/index.php)

[Облачные хранилища](/user_help/settings/clouds/index.php)

[AD/LDAP интеграция](/user_help/settings/ldap/index.php)

[Перевод](/user_help/settings/translate/index.php)

[XMPP сервер (КП)](/user_help/settings/xmpp/index.php)

[Настройки продукта (главный модуль)](/user_help/settings/settings/index.php)

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Поиск](/user_help/settings/search/index.php)

Google Sitemap

# Google Sitemap

**Примечание:** данный инструмент устарел в рамках модуля **Поиск**. Ему на смену пришел модуль [Поисковая оптимизация](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2095).
  
Инструмент **Google Sitemap** оставлен в системе для совместимости и на случай отсутствия установленного модуля **Поисковая оптимизация**.

**Google Sitemap** - это простой инструмент управления доставкой информации о страницах сайта в базу данных Google, самой мощной и популярной поисковой системы. Применение **Google Sitemap** особенно важно для динамических сайтов, страницы которых генерируются автоматически, поскольку это гарантирует наличие информации о всех страницах сайта в базе данных Google. Файлы **Google Sitemap** по сути своей являются XML-файлами, однако создание их вручную крайне трудоемко и требует много времени. При помощи формы **Создание Google Sitemap** можно быстро создать карту сайта для передачи ее Google.
  
  
Форма cоздания **Google Sitemap** доступна на странице **Создание Google Sitemap** (*Настройки > Поиск > Google Sitemap*).

#### Закладка "Google Sitemap"

| Поле | Описание |
| --- | --- |
| Сайт | Сайт, для которого требуется создать sitemap. |
| Шаг | Продолжительность каждого шага создания sitemap, указанная в секундах. |
| Максимальное количество документов для обработки на одном шаге | Укажите максимальное количество документов, которое будет обрабатываться на одном шаге. |
| Включать в Google Sitemap только темы форумов, но не сообщения | При отмеченной опции при создании в карту будут писаться только первые сообщения темы форума с датой модификации, равной последнему добавленному в тему сообщению. |
| Не включать в Google Sitemap комментарии к сообщениям блогов | Если опция отмечена, то при создании карты **не** будут включаться комментарии к сообщениям блога. |
| Использовать HTTPS | При отмеченной опции будет использоваться протокол HTTPS. |

Для того чтобы начать генерацию карты сайта, нажмите кнопку **Создать**. Для остановки генерации служит кнопка **Остановить**, а для продолжения - **Продолжить**.

**Внимание!** При создании файлов **Google Sitemap** все файлы вида **sitemap\_\*.xml**, расположенные в корневой папке выбранного сайта, будут перезаписаны.

После создания карты сайта будет отображена страница, содержащая адрес **sitemap** для передачи Google, а также краткие инструкции.

#### Смотрите также:

* [Google Sitemap (учебный курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2068)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх