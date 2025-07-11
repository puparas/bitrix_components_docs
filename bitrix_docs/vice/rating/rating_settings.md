| Поле | Описание |
| --- |

|
| Система расчета веса голоса | Устанавливается система расчета веса голоса:  * автоматическая - вес голоса будет рассчитываться [автоматически по формулам](https://dev.1c-bitrix.ru/community/blogs/rsv-dev/2386.php). * настраиваемая - вес голоса будет рассчитываться по заданным параметрам. |
| Для расчета авторитета используется рейтинг |

|
| Текущий размер сообщества (пользователей) | Числовой показатель, высчитывается при пересчете авторитета. В размер сообщества включаются пользователи, которые заходили на сайт не позднее 90 дней с момента расчета и имеют право голосовать (за рейтинг или авторитет). |
| Рассчитывать нормировочный коэффициент |

|
| Кол-во пользователей, за авторитет которых может голосовать пользователь в течение суток | Указывается количество пользователей. |
| Вес голоса за авторитет пользователя рассчитывается |

|
| Кнопки голосования | |
| Использовать оценку контента |

|
| Тип оценки контента | Выбор вариантов оценки:  * Мне нравится. Оценка будет производится только в положительном плане. Данную оценку можно будет "забрать" обратно. При выборе этого чекбокса становятся доступными   поля настройки текста кнопки.      Поля настройки текста кнопки:+ **Текст кнопки "Мне нравится" до голосования**   + **Текст кнопки "Мне нравится" после голосования**   + **Текст кнопки "Мне нравится" для гостей** * Нравится / Не нравится. Оценка производится как в положительную сторону, так и в отрицательную. Данную оценку можно будет "забрать" обратно. |
| Вид кнопоки |

|
| Поля настроек текстов кнопки | Доступны при выборе Типа оценки **Мне нравится**. Можно задать нужный текст для кнопок голосования. |

### Право на голосование

| Поле | Описание |
| --- |

|
| Пользователь может голосовать за свой контент | Указать может ли автор контента голосовать за собственный контент. |
| Кол-во дней отсутствия пользователя на сайте для учета в размере сообщества |

|
| Автоматически включать пользователей в группу | [Y\N] Разрешает автоматическое включение новых пользователей в группу при регистрации. |
| **Рейтинг** |

|
| Группа, имеющая право голосовать за рейтинг | В данном поле указываются группы пользователей, которые могут голосовать за рейтинг контента. С помощью [правил обработки](/user_help/service/rating/rating_rule_list.php) вы можете настроить автоматическое включение пользователей в нужную группу по достижении определенного уровня авторитета. |
| Автоматически включать пользователей в группу |

|
| **Авторитет** | |
| Группа, имеющая право голосовать за авторитет |

|
| Автоматически включать пользователей в группу | Указывается группа пользователей, в которую будут включаться/исключаться пользователи при достижения ими определенного уровня нормированных голосов. Значения диапазона голосов задаются в полях **если кол-во нормированных голосов больше или равно** и **исключать если меньше**. |

### Начальные значения

| Поле | Описание |
| --- |

|
| Начальный авторитет для нового пользователя | В данном поле укажите, какой начальный авторитет будет иметь пользователь после регистрации. По умолчанию, он будет получать 3 нормированных голоса, при стандартных настройках, это позволит ему сразу голосовать за рейтинг контента и за авторитет пользователя. |
| Установить всем пользователям начальный авторитет |

|
| **Данные рейтингов** | |
| Удалить все данные системы рейтингования |