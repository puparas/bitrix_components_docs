# Создание счетчика

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

[Бизнес-процессы](/user_help/service/bizproc/index.php)

[Блоги](/user_help/service/blogs/index.php)

[Веб-мессенджер](/user_help/service/im/index.php)

[Веб-формы](/user_help/service/form/index.php)

[Видеоконференциии (КП)](/user_help/service/video/index.php)

[Внешние источники данных (КП)](/user_help/service/xdi/index.php)

[Интранет (КП)](/user_help/service/intranet/index.php)

[Календарь событий](/user_help/service/event_calendar/index.php)

[Конструктор отчетов (КП)](/user_help/service/report/index.php)

[Экстранет (КП)](/user_help/service/extranet/index.php)

[Контроллер](/user_help/service/controller/index.php)

[Контроллер. Настройки модуля](/user_help/service/controller/settings.php)
[Управление подчиненными сайтами](/user_help/service/controller/controller_member_admin.php)
[Создание и редактирование сайта (клиента)](/user_help/service/controller/controller_member_edit.php)
[Управление группами сайтов](/user_help/service/controller/controller_group_admin.php)
[Создание и редактирование группы сайтов](/user_help/service/controller/controller_group_edit.php)
[Задачи для выполнения на клиентах контроллера сайтов](/user_help/service/controller/controller_task.php)
[Журнал работы контроллера сайтов](/user_help/service/controller/controller_log_admin.php)
[Удаленное выполнение команд](/user_help/service/controller/controller_run_command.php)
[Передача файлов](/user_help/service/controller/controller_upload_file.php)
[Счетчики](/user_help/service/controller/controller_counter_admin.php)
[Создание счетчика](/user_help/service/controller/controller_counter_edit.php)
[Авторизация](/user_help/service/controller/controller_auth.php)
[История изменений на клиенте](/user_help/service/controller/controller_member_history.php)

[Менеджер идей](/user_help/service/idea/index.php)

[Опросы, голосования](/user_help/service/vote/index.php)

[Обучение](/user_help/service/learning/index.php)

[Подписка, рассылки](/user_help/service/subscribe/index.php)

[Почта](/user_help/service/mail/index.php)

[Рейтинги](/user_help/service/rating/index.php)

[Смайлы](/user_help/service/smile/index.php)

[Социальная сеть (КП)](/user_help/service/socialnetwork/index.php)

[Социальные сервисы](/user_help/service/socialservices/index.php)

[Стикеры](/user_help/service/stickers/index.php)

[Техподдержка](/user_help/service/support/index.php)

[Учет рабочего времени (КП)](/user_help/service/timeman/index.php)

[Форум](/user_help/service/forum/index.php)

[CRM (КП)](/user_help/service/crm/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Сервисы](/user_help/service/index.php)

[Контроллер](/user_help/service/controller/index.php)

Создание счетчика

**Недоступно в редакциях:**Бизнес, Малый бизнес, Стандарт, Старт

# Создание счетчика

### Закладка Счетчик

| Поле | Описание |
| --- | --- |
| \*Название | Название счетчика. |
| \*Тип | Тип счетчика. Влияет на форму вывода данных. Возможны типы:  * **Целое число**. Выводит данные в формате целых чисел. * **Число**. Выводит данные в виде числа с десятичной дробью. * **Строка**. Выводит данные в формате строки. * **Дата/время**. Выводит данные в формате даты, времени в формате сайта. |
| Формат | Позволяет выводить данные в формате размера файла (Например: Мб).     Поле работает только для типов **Целое число** и **Число**. |
| Группы | Установка флажка для групп сайтов для которых должен применяться данный счетчик.     Подключение счетчика возможно и на закладке **Счетчики** на странице редактирования группы. |
| \*Команда | Поле для ввода PHP-кода счетчика. |

### Закладка Группы

| Поле | Описание |
| --- | --- |
| Группы | Установка флажка для групп сайтов для которых должен применяться данный счетчик.    Подключение счетчика возможно и на закладке **Счетчики** на странице редактирования группы. |

### Закладка Команда

| Поле | Описание |
| --- | --- |
| \*Команда | Поле для ввода PHP-кода счетчика. |

**\*** - поля, обязательные для заполнения.

### Примеры счетчиков

**Подсчет пользователей экстранета**

```
$counter = 0;
$rsUsers = CUser::GetList($o="ID", $b="asc", array("ACTIVE"=>"Y","=UF_DEPARTMENT"=>false), array("SELECT"=>array("ID")));
while($arUser = $rsUsers->Fetch())
  if($arUser["EXTERNAL_AUTH_ID"] !== "__controller")
    $counter++;
return $counter;
```

**Выставление лимита в 5GB** (Тип - число, формат - как размер файла)

```
$max_size = 5*1024*1024*1024;
COption::SetOptionString("main_size", "~max_size", $max_size);
return $max_size;
```

**Объем файлов в облаке** (Тип - число, формат - как размер файла)

```
$file_size = 0.0;
if(CModule::IncludeModule('clouds'))
{
  $rsBuckets = CCloudStorageBucket::GetList();
  while($arBucket = $rsBuckets->Fetch())
    $file_size += $arBucket["FILE_SIZE"];
}

COption::SetOptionString("main_size", "~cloud", $file_size);
$params = array("status" => "d", "time" => time());
COption::SetOptionString("main_size", "~cloud_params", serialize($params));

return $file_size;
```

### Смотрите также

* [Счётчики (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=3526)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх