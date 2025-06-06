| Параметр | Значение |
| --- |

|
| [Проактивный фильтр (Web Application Firewall)](/user_help/settings/security/security_filter.php) | Включен |
| [Исключения из проактивного фильтра](/user_help/settings/security/security_filter.php#exception) |

|
| [Журнал вторжений за последние 7 дней](/user_help/settings/security/settings.php#events) | 0 |
| [Контроль активности](/user_help/settings/security/security_stat_activity.php) |

|
| [Использовать CAPTCHA при регистрации](/user_help/settings/settings/settings.php#author) | Да |
| [Режим вывода ошибок (error\_reporting)](/user_help/settings/settings/settings.php#settings) |

|
| [Показ ошибочных запросов базы данных](https://dev.1c-bitrix.ru/api_help/main/general/magic_vars.php#dbdebug) | Выключен |

**Примечание**: если стандартный уровень не настроен полностью, то защита сайта будет осуществляться на начальном уровне, но с учетом настроенных параметров на стандартном, высоком и повышенном уровнях.

### Высокий

Чтобы защита осуществлялась на высоком уровне безопасности, сначала необходимо настроить стандартный уровень безопасности, а затем выполнить настройку параметров для высокого уровня.

| Параметр | Значение |
| --- |

|
| [Журналирование событий главного модуля](/user_help/settings/settings/settings.php#events) | Не все включены |
| [Ограничение отображения страниц во фрейме](/user_help/settings/security/security_frame.php) |

|
| [Защита административной части](/user_help/settings/security/security_iprule_admin.php) | Включена |
| [Хранение сессий в базе данных](/user_help/settings/security/security_session.php#security_session) |

|
| [Смена идентификатора сессий](/user_help/settings/security/security_session.php#session_id) | Включена |
| [Защита редиректов от фишинга](/user_help/settings/security/security_redirect.php) |

|

**Примечание**: если некоторые параметры высокого уровня безопасности принимают несоответствующие значения, то защита сайта будет осуществляться на стандартном или начальном (если настроены не все параметры стандартного уровня) уровне, но с учетом настроенных параметров на стандартном, высоком и повышенном уровнях.

### Повышенный

Чтобы защита осуществлялась на повышенном уровне безопасности, сначала необходимо настроить защиту на стандартном и высоком уровне, а затем выполнить настройку параметров повышенного уровня.

| Параметр | Значение |
| --- |

|
| [Одноразовые пароли](/user_help/settings/security/security_otp.php) | Включены |
| [Контроль целостности](/user_help/settings/security/security_file_verifier.php) |

|
| [Веб-антивирус](/user_help/settings/security/security_antivirus.php) | Включен |
| [Действия при обнаружении вируса](/user_help/settings/security/security_antivirus.php#option) |

|
| [Исключения веб-антивируса](/user_help/settings/security/security_antivirus.php#exception) | Нет |
| [Журнал заражений за последние 7 дней](/user_help/settings/security/event_log.php) |