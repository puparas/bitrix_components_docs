|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Использовать простой режим настройки |

| [Y|N] При отмеченной опции будет использоваться простой режим настройки фотогалереи (значения остальных параметров будут по умолчанию). |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок |

| Для выбранного типа инфоблоков указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| Группы пользователей, которым разрешено создавать галерею |

| Указываются группы пользователей, которым разрешено создавать галерею. |
| Включить премодерацию фото |

| [Y|N] При отмеченной опции будет использоваться механизм премодерации фото. |
| Путь к профилю пользователя |

| Указывается шаблон пути к профилю пользователя. |
| Отображать навигационную цепочку 'хлебные крошки' в рамках комплексного компонента |

| [Y|N] При отмеченной опции на странице фотогалереи будет отображаться навигационная цепочка ('хлебные крошки').. |
| Анализировать параметры соц.сети |

| [Y|N] При отмеченной опции будет производится проверка прав доступа пользователя к модулю **Социальная сеть**. |
| **Настройки фотогалереи** |

| |
| Размер картинки галереи (px) |

| Указывается размер аватара владельца галереи в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Размер картинки-анонса фотоальбома (px) |

| Указывается размер картинки-анонса фотоальбома в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Размер фотографии-анонса (px) |

| Указывается размер картинки-анонса альбома в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Размер картинки в предпросмотре в списке альбомов (px) |

| Указывается размер картинки в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Обязательно ограничивать размер оригинала (px) (при значении 0 ограничение не происходит) |

| Задается размер оригинала фотографии в пикселях. Фотография будет уменьшена до указанной величины. Если указано значение 0, то изменение размера не происходит. Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ.    Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:    Настраиваемые параметры при включенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - страница со списком альбомов; * **galleries** - страница со списком галерей; * **gallery** - страница с содержимым галереи; * **gallery\_edit** - страница редактирования параметров галереи; * **section** - страница просмотра альбомов; * **section\_edit** - страница редактирования параметров альбома; * **section\_edit\_icon** - страница выбора обложки альбома; * **upload** - страница загрузки фотографий; * **detail** - страница просмотра фотографий; * **detail\_edit** - страница редактирования параметров фотографии; * **detail\_slide\_show** - страница слайд-шоу; * **detail\_list** - страница со списком фотографий; * **search** - страница поиска; * **tags** - страница тегов. |  **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**.    Если режим поддержки ЧПУ **выключен**, то необходимо настроить массив переменных    Настраиваемые параметры при выключенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | ID пользователя | **USER\_ID** | Задается переменная, в которой будет передаваться идентификатор пользователя. | | Код галереи | **USER\_ALIAS** | Задается переменная, в которой будет передаваться символьный код галереи. | | Идентификатор раздела | **SECTION\_ID** | Задается переменная, в которой будет передаваться идентификатор раздела (альбома). | | Идентификатор элемента | **ELEMENT\_ID** | Задается переменная, в которой будет передаваться идентификатор элемента (фотографии). | | Идентификатор страницы | **PAGE\_NAME** | Задается переменная, в которой будет передаваться идентификатор страницы. | | Идентификатор действия | **ACTION** | Задается переменная, в которой будет передаваться идентификатор действия. |  **VARIABLE\_ALIASES**, который включает в себя: **USER\_ID**, **USER\_ALIAS**, **SECTION\_ID**, **ELEMENT\_ID**, **PAGE\_NAME**, **ACTION**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Фотографии**. |
| [Главная страница] Количество фото на главной странице |

| Указывается количество фотографий, выводимых на главной странице фотогалереи. |
| [Главная страница] Показывать только опубликованные фото |

| [Y|N] При отмеченной опции только на главной странице будут выводится только опубликованные фотографии.    Если опция отмечена, то необходимо настроить следущие параметры: **PUBLIC\_BY\_DEFAULT** и **MODERATE**. |
| Показывать секцию кнопок управления |

| [Y|N] При отмеченной опции на Главной странице пользовательской галереи будут показываться кнопки управления (например **Мои фото**, **Мои галереи**, **Загрузить фото**). Параметр доступен только при использовании шаблона **default**. |
| **Настройки голосования** |

| |
| Разрешить голосование |

| [Y|N] При отмеченной опции посетители смогут голосовать за фотографии, выставляя баллы, на странице с детальной информацией. При установленной опции становятся доступными следующие поля.    Доступные поля:  |  |  |  | | --- | --- | --- | | Максимальный балл | **MAX\_VOTE** | Указывается максимально возможный балл, т.е. число возможных оценок. | | Подписи к баллам | **VOTE\_NAMES** | Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:   ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. | | В качестве рейтинга показывать | **DISPLAY\_AS\_RATING** | Указывается одно из значений, которое должно быть показано в качестве рейтинга:  * **Рейтинг** (**rating**) - высчитывается на основе формулы: **Rating** = (SUM(vote)+3.125\*10) / (COUNT(\*)+10), где:  3.125 - это стартовый рейтинг. То есть изначально (при отсутствии голосов) рейтинг фотографии равен 3.125.  10 - это константа, определяющая количество голосов, "утяжеляющих" первоначальное значение рейтинга (3.125). Это исключает случай, когда, например, трое проголосовавших человека могут вознести или опустить фотографию всего тремя голосами.  При такой формуле расчета значение рейтинга получается более "плавное" и не так скачет при небольшом количестве голосующих. Чем больше голосов, тем больше рейтинг приближается к среднему арифметическому. * **Среднее значение** (**vote\_avg**) - высчитывается как среднее арифметическое всех баллов к фотографии; * **Рейтинг (главного модуля)** (**rating\_main**) - использование [рейтинга главного модуля](/user_help/service/rating/rating_settings.php). **Подробнее:** - см. главу [Рейтинги](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=1232);     - в блоге [Рейтинги: создание собственного критерия рейтингования](http://dev.1c-bitrix.ru/community/blogs/hazz/2303.php);    - в блоге [Саморегулируемое сообщество, построенное на двухфакторном рейтинге](http://dev.1c-bitrix.ru/community/blogs/rsv-dev/2386.php). |  Вид кнопок рейтинга | **RATING\_MAIN\_TYPE** | Указывается одно из значений, которое должно быть показано в качестве рейтинга:  * **по умолчанию**; * **Плюс / минус** (**standart**); * **Мне нравится** (**like**).    Параметр доступен только если выбран **Рейтинг (главного модуля)** (**rating\_main**). | |

| **Настройки тегов** | | |
| Показывать теги |

| [Y|N] При отмеченной опции будет показано облако тегов фотогалереи. Станут активными дополнительные поля     Максимальный размер шрифта (px) | **TAGS\_FONT\_MAX** | Указывается максимальный размер шрифта отображения тегов (в пикселах). | |
| Минимальный размер шрифта (px) |

| Указывается минимальный размер шрифта отображения тегов (в пикселах). |
| Цвет более позднего тега (пример: "C0C0C0") |

| Указывается код цвета тегов, дата создания которых наиболее поздняя (пример: "C0C0C0"). |
| Цвет более раннего тега (пример: "FEFEFE") |

| Указывается код цвета тегов, дата создания которых наиболее ранняя (пример: "FEFEFE"). |
| **Загрузка фото** |

| |
| Тип загрузчика |

| Указывается тип загрузчика фотографий в фотогалерею:  * Одиночная загрузка через форму (**form**); * Множественный загрузчик (Java/ActiveX) (**applet**); * Множественный Flash-загрузчик (**flash**).  **Параметр устарел с версии 15.0.0.** |
| Схема множественного загрузчика |

| Параметр определяет тип загрузчика в фотогалерии по умолчанию:  * **Стандартный шаблон** (**extended**); * **Упрощенный шаблон загрузчика** (**simple**).  Выбор параметра доступен только при выборе параметра "Тип загрузчика" (**PHOTO\_UPLOADER\_TYPE**) равным "Множественный загрузчик (Java/ActiveX)" (**applet**).   **Параметр устарел с версии 15.0.0.** |
| Максимальный размер загружаемого файла (не должен превышать 1024Mб) (Мб) |

| Указывается максимальный размер загружаемого файла в Мб (не должен превышать 1024Mб). |
| Наносить авторский знак |

| **Внимание!** Функционал авторского знака устарел и не поддерживается с версии **14.5.0** Главного модуля (**main**).  [Y|N] При отмеченной опции при загрузке фотографий можно будет наносить авторский знак. Станут доступны поля настройки авторского знака.    Поля настройки авторского знака:  |  |  |  | | --- | --- | --- | | Правила нанесения авторского знака | **WATERMARK\_RULES** | Указывается правило нанесения авторского знака:  * **На усмотрение пользователя** (**USER**); * **Обязательно наносить авторский знак** (**ALL**).  Если выбрано значение **ALL**, то необходимо настроить дополнительные параметры (приведены в таблице ниже). | | Файл со шрифтом для авторского знака | **PATH\_TO\_FONT** | Указывается файл со шрифтом для создания авторского знака (будет использоваться также и при множественной загрузке). Шрифты предварительно загружаются в директорию **\bitrix\modules\photogallery\fonts\**. Поддерживаются **TTF**-, **OTF**- и **PS**-шрифты. | | Минимальный размер фото для авторского знака (px) | **WATERMARK\_MIN\_PICTURE\_SIZE** | Указывается минимальный размер фото, на которых будет нанесен авторский знак в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. На фотографии меньшего размера знак добавлен не будет. |   **Дополнительные параметры,** заполняемые при выборе правила **Обязательно наносить авторский знак** |
| **Настройки отзывов** |

| |
| Разрешить отзывы |

| [Y|N] При отмеченной опции будет доступен функционал отзывов, станут активны дополнительные поля.    Дополнительные поля:  |  |  |  | | --- | --- | --- | | Компонент комментариев | **COMMENTS\_TYPE** | Указывается компонент, с помощью которого будут добавляться комментарии:  * **Блоги** (**blog**); * **Форум** (**forum**).  Если указать **Блоги**, то необходимо настроить параметр **BLOG\_URL**.    Если указать **Форум**, то необходимо настроить параметр **FORUM\_ID**. | | Блог для комментариев | **BLOG\_URL** | Указывается блог, в котором будут храниться комментарии. | | ID форума для отзывов | **FORUM\_ID** | Указывается один из созданных в системе форумов, который будет использован для комментариев. | |

### Параметры. Расширенный режим

|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Настройки постраничной навигации** |

| |
| Количество альбомов на странице |

| Указывается количество альбомов, отображаемых на одной странице. Остальные альбомы будут выведены с помощью постраничной навигации. |
| Количество фото на странице |

| Указывается количество фотографий, отображаемых на одной странице. Остальные фотографии будут выведены с помощью постраничной навигации. |
| Шаблон для постраничной навигации |

| Указываются название шаблона для постраничной навигации. |
| **Основные параметры** |

| |
| Использовать простой режим настройки |

| [Y|N] При отмеченной опции будет использоваться простой режим настройки фотогалереи (значения остальных параметров будут по умолчанию). |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок |

| Для выбранного типа инфоблоков указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| Группы пользователей, которым разрешено создавать галерею |

| Указываются группы пользователей, которым разрешено создавать галерею. |
| Разрешать создавать пользователям только одну галерею (группы пользователей, имеющие доступ на запись к инфоблоку, могут создавать неограниченное количество галерей) |

| [Y|N] При отмеченной опции пользователям будет разрешено создать только одну галерею. Группы пользователей, имеющие доступ на запись к инфоблоку, могут создавать неограниченное количество галерей. |
| Включить премодерацию фото |

| [Y|N] При отмеченной опции будет использоваться механизм премодерации фото. |
| По какому полю сортируем альбомы |

| Указывается поле, по которому будет происходить сортировка альбомов:  * **ID** - по идентификатору; * **NAME** - по названию; * **SORT** - по индексу сортировки; * **ELEMENTS\_CNT** - по количесву фото в альбоме; * **UF\_DATE** - по дате. |
| Порядок сортировки альбомов |

| Задается порядок сортировки альбомов:  * **ASC** – **по возрастанию**; * **DESC** – **по убыванию**. |
| По какому полю сортируем фото |

| Указывается поле, по которому будет происходить сортировка фотографий:  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **RATING** – по популярности; * **COMMENTS** – по комментариям. * **rand** – выведет элементы в произвольном порядке. |
| Порядок сортировки фото в альбомах |

| Задается порядок сортировки фотографий в альбомах:  * **ASC** – **по возрастанию**; * **DESC** – **по убыванию**. |
| Путь к профилю пользователя |

| Указывается шаблон пути к профилю пользователя. |
| Отображать навигационную цепочку 'хлебные крошки' в рамках комплексного компонента |

| [Y|N] При отмеченной опции на странице фотогалереи будет отображаться навигационная цепочка ('хлебные крошки').. |
| Анализировать параметры соц.сети |

| [Y|N] При отмеченной опции будет производится проверка прав доступа пользователя к модулю **Социальная сеть**. |
| **Настройки фотогалереи** |

| |
| Размер картинки галереи (px) |

| Указывается размер аватара владельца галереи в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Размер картинки-анонса фотоальбома (px) |

| Указывается размер картинки-анонса фотоальбома в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Размер фотографии-анонса (px) |

| Указывается размер картинки-анонса альбома в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
 Размер картинки в предпросмотре в списке альбомов (px) | **SECTION\_LIST\_THUMBS\_SIZE** | Указывается размер картинки в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. || Обязательно ограничивать размер оригинала (px) (при значении 0 ограничение не происходит) | **ORIGINAL\_SIZE** | Задается размер оригинала фотографии в пикселях. Фотография будет уменьшена до указанной величины. Если указано значение 0, то изменение размера не происходит. Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. |
| Качество фотографии-анонса (%) |

| Указывается качество фотографии-анонса в процентах (100% - самое высокое качество). |
| Качество загружаемой фотографии (%) |

| Указывается качество загружаемой фотографии в процентах (100% - самое высокое качество). |
| Дополнительные эскизы |

| Указываются типы для эскизов фотографий, которые должны быть показаны. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:    Настраиваемые параметры при включенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - страница со списком альбомов; * **galleries** - страница со списком галерей; * **gallery** - страница с содержимым галереи; * **gallery\_edit** - страница редактирования параметров галереи; * **section** - страница просмотра альбомов; * **section\_edit** - страница редактирования параметров альбома; * **section\_edit\_icon** - страница выбора обложки альбома; * **upload** - страница загрузки фотографий; * **detail** - страница просмотра фотографий; * **detail\_edit** - страница редактирования параметров фотографии; * **detail\_slide\_show** - страница слайд-шоу; * **detail\_list** - страница со списком фотографий; * **search** - страница поиска; * **tags** - страница тегов. |  **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**.   Если режим поддержки ЧПУ **выключен**, то необходимо настроить массив переменных     Настраиваемые параметры при выключенном режиме поддержки ЧПУ:  |  |  |  | | --- | --- | --- | | ID пользователя | **USER\_ID** | Задается переменная, в которой будет передаваться идентификатор пользователя. | | Код галереи | **USER\_ALIAS** | Задается переменная, в которой будет передаваться символьный код галереи. | | Идентификатор раздела | **SECTION\_ID** | Задается переменная, в которой будет передаваться идентификатор раздела (альбома). | | Идентификатор элемента | **ELEMENT\_ID** | Задается переменная, в которой будет передаваться идентификатор элемента (фотографии). | | Идентификатор страницы | **PAGE\_NAME** | Задается переменная, в которой будет передаваться идентификатор страницы. | | Идентификатор действия | **ACTION** | Задается переменная, в которой будет передаваться идентификатор действия. |  **VARIABLE\_ALIASES**, который включает в себя: **USER\_ID**, **USER\_ALIAS**, **SECTION\_ID**, **ELEMENT\_ID**, **PAGE\_NAME**, **ACTION**. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| **Дополнительные настройки** |

| |
| Формат вывода даты альбома |

| Указывается формат показа даты и времени альбома. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат вывода даты фото |

| Указывается формат показа даты и времени фотографии. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Галерея**. |
| [Главная страница] Количество фото на главной странице |

| Указывается количество фотографий, выводимых на главной странице фотогалереи. |
| [Главная страница] Показывать только опубликованные фото |

| [Y|N] При отмеченной опции только на главной странице будут выводится только опубликованные фотографии.    Если опция отмечена, то необходимо настроить следущие параметры: **PUBLIC\_BY\_DEFAULT** и **MODERATE**. |
| Показывать секцию кнопок управления |

| [Y|N] При отмеченной опции на Главной странице пользовательской галереи будут показываться кнопки управления (например **Мои фото**, **Мои галереи**, **Загрузить фото**). |
| **Настройки голосования** |

| |
| Разрешить голосование |

| [Y|N] При отмеченной опции посетители смогут голосовать за фотографии, выставляя баллы, на странице с детальной информацией. При установленной опции становятся доступными следующие поля.    Доступные поля:  |  |  |  | | --- | --- | --- | | Максимальный балл | **MAX\_VOTE** | Указывается максимально возможный балл, т.е. число возможных оценок. | | Подписи к баллам | **VOTE\_NAMES** | Указываются подписи к каждому баллу. В коде вводится массив, в котором задаются подписи к баллам в таком виде:   ``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```  Если подписи заданы, то они будут выведены вместо оценок-цифр. Если массив не задан, то будут использованы значения по умолчанию. | | В качестве рейтинга показывать | **DISPLAY\_AS\_RATING** | Указывается одно из значений, которое должно быть показано в качестве рейтинга:  * **Рейтинг** (**rating**) - высчитывается на основе формулы: **Rating** = (SUM(vote)+3.125\*10) / (COUNT(\*)+10), где:  3.125 - это стартовый рейтинг. То есть изначально (при отсутствии голосов) рейтинг фотографии равен 3.125.  10 - это константа, определяющая количество голосов, "утяжеляющих" первоначальное значение рейтинга (3.125). Это исключает случай, когда, например, трое проголосовавших человека могут вознести или опустить фотографию всего тремя голосами.  При такой формуле расчета значение рейтинга получается более "плавное" и не так скачет при небольшом количестве голосующих. Чем больше голосов, тем больше рейтинг приближается к среднему арифметическому. * **Среднее значение** (**vote\_avg**) - высчитывается как среднее арифметическое всех баллов к фотографии; * **Рейтинг (главного модуля)** (**rating\_main**) - использование [рейтинга главного модуля](/user_help/service/rating/rating_settings.php). **Подробнее:** - см. главу [Рейтинги](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=1232);     - в блоге [Рейтинги: создание собственного критерия рейтингования](http://dev.1c-bitrix.ru/community/blogs/hazz/2303.php);    - в блоге [Саморегулируемое сообщество, построенное на двухфакторном рейтинге](http://dev.1c-bitrix.ru/community/blogs/rsv-dev/2386.php). |  Вид кнопок рейтинга | **RATING\_MAIN\_TYPE** | Указывается одно из значений, которое должно быть показано в качестве рейтинга:  * **по умолчанию**; * **Плюс / минус** (**standart**); * **Мне нравится** (**like**).    Параметр доступен только если выбран **Рейтинг (главного модуля)** (**rating\_main**). | |

| **Настройки тегов** | | |
| Показывать теги |

| [Y|N] При отмеченной опции будет показано облако тегов фотогалереи.    Облако тегов:  |  |  |  | | --- | --- | --- | | Количество тегов | **TAGS\_PAGE\_ELEMENTS** | Указывается количество тегов, отображаемых в облаке. | | Период выборки тегов (дней) | **TAGS\_PERIOD** | Указывается количество дней, за которые происходит выборка тегов. | | Сужать область поиска | **TAGS\_INHERIT** | [Y|N] При отмеченной опции выбранные теги добавляются в фильтр поиска. |  Максимальный размер шрифта (px) | **TAGS\_FONT\_MAX** | Указывается максимальный размер шрифта отображения тегов (в пикселах). | |
| Минимальный размер шрифта (px) |

| Указывается минимальный размер шрифта отображения тегов (в пикселах). |
| Цвет более позднего тега (пример: "C0C0C0") |

| Указывается код цвета тегов, дата создания которых наиболее поздняя (пример: "C0C0C0"). |
| Цвет более раннего тега (пример: "FEFEFE") |

| Указывается код цвета тегов, дата создания которых наиболее ранняя (пример: "FEFEFE"). |
| Показывать цепочку навигации |

| [Y|N] При отмеченной опции будет показана цепочка навигации. Параметр работает, если параметр **TAGS\_INHERIT** принимает значение **Y**. |
| **Загрузка фото** |

| |
| Тип загрузчика |

| Указывается тип загрузчика фотографий в фотогалерею:  * Одиночная загрузка через форму (**form**); * Множественный загрузчик (Java/ActiveX) (**applet**); * Множественный Flash-загрузчик (**flash**).  **Параметр устарел с версии 15.0.0.** |
| Схема множественного загрузчика |

| Параметр определяет тип загрузчика в фотогалерии по умолчанию:  * **Стандартный шаблон** (**extended**); * **Упрощенный шаблон загрузчика** (**simple**).  Выбор параметра доступен только при выборе параметра "Тип загрузчика" (**PHOTO\_UPLOADER\_TYPE**) равным "Множественный загрузчик (Java/ActiveX)" (**applet**).   **Параметр устарел с версии 15.0.0.** |
| Максимальный размер загружаемого файла (не должен превышать 1024Mб) (Мб) |

| Указывается максимальный размер загружаемого файла в Мб (не должен превышать 1024Mб). |
| Наносить авторский знак |

| **Внимание!** Функционал авторского знака устарел и не поддерживается с версии **14.5.0** Главного модуля (**main**).  [Y|N] При отмеченной опции при загрузке фотографий можно будет наносить авторский знак.Станут доступны поля настройки авторского знака.    Поля настройки авторского знака:  |  |  |  | | --- | --- | --- | | Правила нанесения авторского знака | **WATERMARK\_RULES** | Указывается правило нанесения авторского знака:  * **На усмотрение пользователя** (**USER**); * **Обязательно наносить авторский знак** (**ALL**).  Если выбрано значение **Обязательно наносить авторский знак**, то необходимо настроить дополнительные параметры (приведены в таблице ниже). | | Файл со шрифтом для авторского знака | **PATH\_TO\_FONT** | Указывается файл со шрифтом для создания авторского знака (будет использоваться также и при множественной загрузке). Шрифты предварительно загружаются в директорию **\bitrix\modules\photogallery\fonts\**. Поддерживаются **TTF**-, **OTF**- и **PS**-шрифты. | | Минимальный размер фото для авторского знака (px) | **WATERMARK\_MIN\_PICTURE\_SIZE** | Указывается минимальный размер фото, на которых будет нанесен авторский знак в пикселях (px). Размер задается для большей стороны картинки, другая сторона загружаемого изображения будет высчитана пропорционально. На фотографии меньшего размера знак добавлен не будет. |   **Дополнительные параметры,** заполняемые при выборе правила **Обязательно наносить авторский знак** |
| **Настройки отзывов** |

| |
| Разрешить отзывы |

``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```

``` "VOTE_NAMES" => Array("0","1","2","3","4","5"),  ```

```
<?$APPLICATION->IncludeComponent("bitrix:photogallery_user","",Array(

		"INDEX_PAGE_TOP_ELEMENTS_COUNT" => "45",

		"SHOW_ONLY_PUBLIC" => "Y",

		"MODERATE" => "N",

		"SHOW_CONTROLS_BUTTONS" => "Y",

		"USE_LIGHT_VIEW" => "N",

		"IBLOCK_TYPE" => "gallery",

		"IBLOCK_ID" => "11",

		"GALLERY_GROUPS" => array(),

		"ONLY_ONE_GALLERY" => "Y",

		"MODERATION" => "Y",

		"SECTION_SORT_BY" => "UF_DATE",

		"SECTION_SORT_ORD" => "DESC",

		"ELEMENT_SORT_FIELD" => "id",

		"ELEMENT_SORT_ORDER" => "desc",

		"PATH_TO_USER" => "",

		"SEF_MODE" => "Y",

		"SECTION_PAGE_ELEMENTS" => "15",

		"ELEMENTS_PAGE_ELEMENTS" => "50",

		"PAGE_NAVIGATION_TEMPLATE" => "",

		"DATE_TIME_FORMAT_SECTION" => "d.m.Y",

		"DATE_TIME_FORMAT_DETAIL" => "d.m.Y",

		"GALLERY_AVATAR_SIZE" => "50",

		"ALBUM_PHOTO_THUMBS_SIZE" => "120",

		"THUMBNAIL_SIZE" => "100",

		"ORIGINAL_SIZE" => "1280",

		"JPEG_QUALITY1" => "100",

		"JPEG_QUALITY" => "100",

		"ADDITIONAL_SIGHTS" => array(),

		"USE_RATING" => "Y",

		"SHOW_TAGS" => "Y",

		"SET_TITLE" => "Y",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"SHOW_NAVIGATION" => "Y",    

		"UPLOADER_TYPE" => "applet",

		"APPLET_LAYOUT" => "extended",

		"UPLOAD_MAX_FILE_SIZE" => "1024",

		"USE_WATERMARK" => "Y",

		"WATERMARK_RULES" => "ALL",

		"WATERMARK_TYPE" => "PICTURE",

		"WATERMARK_FILE" => "",

		"WATERMARK_FILE_ORDER" => "usual",

		"WATERMARK_POSITION" => "mc",

		"WATERMARK_TRANSPARENCY" => "20",

		"PATH_TO_FONT" => "",

		"WATERMARK_MIN_PICTURE_SIZE" => "800",

		"MAX_VOTE" => "5",

		"VOTE_NAMES" => array("1", "2", "3", "4", "5"),

		"DISPLAY_AS_RATING" => "rating",

		"USE_COMMENTS" => "Y",

		"COMMENTS_TYPE" => "forum",

		"FORUM_ID" => "7",

		"PATH_TO_SMILE" => "/bitrix/images/blog/smile/",

		"URL_TEMPLATES_READ" => "",

		"URL_TEMPLATES_PROFILE_VIEW" => "",

		"USE_CAPTCHA" => "Y",

		"SHOW_LINK_TO_FORUM" => "Y",

		"PREORDER" => "Y",

		"POST_FIRST_MESSAGE" => "Y",

		"TAGS_PAGE_ELEMENTS" => "150",

		"TAGS_PERIOD" => "",

		"TAGS_INHERIT" => "Y",

		"TAGS_FONT_MAX" => "30",

		"TAGS_FONT_MIN" => "14",

		"TAGS_COLOR_NEW" => "486DAA",

		"TAGS_COLOR_OLD" => "486DAA",

		"TAGS_SHOW_CHAIN" => "Y",

		"ANALIZE_SOCNET_PERMISSION" => "Y",

		"SEF_FOLDER" => "/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"galleries" => "galleries/#USER_ID#/",

			"gallery" => "#USER_ALIAS#/",

			"gallery_edit" => "#USER_ALIAS#/action/#ACTION#/",

			"section" => "#USER_ALIAS#/#SECTION_ID#/",

			"section_edit" => "#USER_ALIAS#/#SECTION_ID#/action/#ACTION#/",

			"section_edit_icon" => "#USER_ALIAS#/#SECTION_ID#/icon/action/#ACTION#/",

			"upload" => "#USER_ALIAS#/#SECTION_ID#/action/upload/",

			"detail" => "#USER_ALIAS#/#SECTION_ID#/#ELEMENT_ID#/",

			"detail_edit" => "#USER_ALIAS#/#SECTION_ID#/#ELEMENT_ID#/action/#ACTION#/",

			"detail_slide_show" => "#USER_ALIAS#/#SECTION_ID#/#ELEMENT_ID#/slide_show/",

			"detail_list" => "list/",

			"search" => "search/",

			"tags" => "tags/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"galleries" => Array(),

			"gallery" => Array(),

			"gallery_edit" => Array(),

			"section" => Array(),

			"section_edit" => Array(),

			"section_edit_icon" => Array(),

			"upload" => Array(),

			"detail" => Array(),

			"detail_edit" => Array(),

			"detail_slide_show" => Array(),

			"detail_list" => Array(),

			"search" => Array(),

			"tags" => Array(),

		)

	),

);?>


```