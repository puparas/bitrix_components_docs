|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Имена переменных** |

| |
| Имя переменной для страницы |

| Указывается имя переменной, которой передается страница социальной сети. |
| Имя переменной для задания |

| Указывается имя переменной, которой передается идентификатор задания некоторого бизнес-процесса. |
| **Шаблоны ссылок** |

| |
| Шаблон пути к обработке задания |

| Задается путь к странице обработки задания бизнес-процесса. |
| **Дополнительные настройки** |

| |
| Устанавливать цепочку навигации |

| [Y|N] При отмеченной опции в цепочке навигации будет отображаться пункт **Бизнес-процессы**. |
| Устанавливать заголовок страницы |

```


<?$APPLICATION->IncludeComponent("bitrix:socialnetwork.bizproc","",Array(

        "PAGE_VAR" => "page", 

        "TASK_VAR" => "task_id", 

        "PATH_TO_BIZPROC_EDIT" => "bizproc_task.php?task_id=#task_id#", 

        "SET_NAV_CHAIN" => "Y", 

        "SET_TITLE" => "Y" 

    )

);?>


```