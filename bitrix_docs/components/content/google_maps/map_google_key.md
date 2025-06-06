# Инструкция получения ключа API Google

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

Инструкция получения ключа API Google

# Инструкция получения ключа API Google

Для корректной работы компонентов с сервисами *Google* вам потребуется
получить API ключи



Прочитать о том, как их получить можно [здесь](https://developers.google.com/maps/documentation/javascript/get-api-key).
, а также настроить ряд библиотек.

В июне 2018 года Google запустил новый функционал [Google Maps Platform](https://cloud.google.com/maps-platform/), а c июля 2018 года вступил в силу новый [тарифный план Google](https://cloud.google.com/maps-platform/pricing/) с оплатой за использование API карт, маршрутов и мест (Maps, Routes or Places).

Процесс получения ключа вам поможет пройти специальный мастер:

1. Войдите в свой аккаунт Google или же создайте новый;
2. Перейдите по адресу <https://cloud.google.com/maps-platform/>;
3. Нажмите кнопку
   Get Started



   ![](/upload/medialibrary/981/googlemaps1.png)
   .
4. На верхней панели раскройте выпадающий список, кликните
   New project



   ![maps1.png](/upload/medialibrary/981/googlemaps2.png)
   , введите произвольное название и нажмите **CREATE**:

![](/upload/medialibrary/981/googlemaps3.png)

5. Настройте свою систему оплаты за использование API.
   Создайте платежный аккаунт



   ![](/upload/medialibrary/981/googlemaps4.png)
   .

1. На первом шаге создания платежного аккаунта выберите страну, условия использования и нажмите
   Продолжить



   ![](/upload/medialibrary/981/googlemaps5.png)
   .
2. На втором шаге Google попросит ввести ваш номер телефона для верификации и пришлет на него код.
   Введите код



   ![](/upload/medialibrary/981/googlemaps6.png)
   в поле и нажмите **VERIFY**.
3. Далее нужно будет внести данные
   банковской карточки



   ![](/upload/medialibrary/981/googlemaps7.png)
   . Google при этом
   проверит карточку



   При проверке карточки Google выдает следующее уведомление:
     
     
   Доступ ко всем продуктам облачной платформы.
     
   Получите все необходимое для создания и запуска ваших приложений, веб-сайтов и служб, включая Firebase и API Карт Google.
   300 долларов США бесплатно.
     
   Положите Google Cloud на работу с 300 долларами на счете, которые можно потратить в течение следующих 90 дней.
   Без автоматического списания после окончания бесплатного пробного периода.
     
   Мы просим вас указать кредитную карту, чтобы убедиться, что вы не робот. С вас не будет взиматься плата, если вы не перейдете на платную учетную запись вручную.
   .

   Когда подключен платежный аккаунт, то на него ежемесячно начисляется бесплатно использование карт, маршрутов или мест на сумму в размере 200 долларов США. Это примерно до 28 000 запросов. Счет на оплату будет выставлен только после того, как использование Google Maps Platform превысит ежемесячный
   лимит в 200 долларов



   У Google существуют разные кредиты. 200 долл/мес - это кредит для карт, маршрутов, мест. Вы можете использовать также кредит Google Cloud Platform (GCP) - 300 долл/3 мес. Он может покрывать как сервис Google Maps, так и другие облачные сервисы. Изучите [документацию](https://developers.google.com/maps/billing-credits#monthly) Google Cloud для понимания, что покрывает каждый кредит.
   .

6. После подключения платежного аккаунта вы получите возможность выбрать и подключить
   необходимые сервисы



   ![](/upload/medialibrary/981/googlemaps8.png)
   : Google Maps JavaScript API, Google Maps Geocoding API, Google Maps Places API и другие. В дальнейшем, при необходимости, вы сможете подключать сервисы
   из библиотеки



   ![](/upload/medialibrary/981/googlemaps9.png)
   .

| API-ключи могут понадобиться для подключения Google Images к Сайтам24 |
| --- |
| Чтобы подключить возможность использовать в карточках Сайтов24 коллекцию картинок Google в библиотеке выберите и подключите сервис Custom Search API:    В настройках модуля Сайты 24 (Настройки > Настройка Продукта > Настройки модулей > Сайты 24) укажите укажите ключ API для Google Images.  После подключения можно будет выбирать в карточках картинки из коллекции Google:  site24_1.png |

7. Выберите пункт меню API и сервисы -> Учетные данные и создайте их. При создании следует выбирать
   Ключ API



   ![](/upload/medialibrary/981/google19.png)
   .
8. Через несколько секунд
   ключ будет создан



   ![](/upload/medialibrary/981/googlemaps11.png)
   .
9. Перед его использованием примените ограничения для него. Минимально необходимые ограничения: протокол (HTTP) и источник перехода (ваш адрес портала в виде <http://ваш_битрикс24.ru/>\*).

Теперь вы можете использовать этот ключ в
настройках



[![Нажмите на рисунок, чтобы увеличить](/upload/medialibrary/a49/google_key-sm.png)](javascript:ShowImg('/upload/medialibrary/a49/google_key.png',1160,531,'Настройки интеграции с Google API'))
вашего портала.

| API-ключи понадобятся для работы обновленного поля «Адрес» |
| --- |
| Настройки модуля **Адреса и местоположения** описаны в курсе [Администратор сервиса Битрикс24 (коробочная версия).](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=020910)   Чтобы в поле «Адрес» в реквизитах компаний автоматически выводились подсказки от Google или чтобы можно было указывать адрес непосредственно на карте:  maps3.png  понадобится 2 ключа:   * Ключ с правами на Google Maps JavaScript API, Places API, Geocoding API для использования в браузере пользователя. * Ключ с правами на Google Places API, Geocoding API для использования на сервере.   Для первого ключа (использование в браузере) задайте ограничения по HTTP-источникам перехода, укажите источник перехода и допустимые API:      Для второго ключа (использование на сервере) задайте соответствующие ограничения по IP-адресам.  Ввести эти ключи нужно будет в настройках модуля:  maps2.png |

Для просмотра уже созданных ключей перейдите по адресу <https://console.developers.google.com/apis/credentials>.

![](/upload/medialibrary/981/googlemaps12.png)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх