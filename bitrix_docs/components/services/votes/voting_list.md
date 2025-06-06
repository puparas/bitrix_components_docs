| Пример вызова компонента **voting.list** |
| --- |
| ``` <?$APPLICATION->IncludeComponent("bitrix:voting.list","",Array(
 		"CHANNEL_SID" => "BOOKS_VOTE", 
 		"VOTE_FORM_TEMPLATE" => "vote_new.php?VOTE_ID=#VOTE_ID#", 
 		"VOTE_RESULT_TEMPLATE" => "vote_result.php?VOTE_ID=#VOTE_ID#" 
 	),
 );?>
  ``` |

|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Группа опросов |

| Указываются группы, опросы которых будут выведены на странице. |
| **Шаблоны ссылок** |

| |
| Страница для вывода пустой формы опроса |

| Указывается адрес страницы для вывода пустой формы опроса. |
| Страница для вывода диаграмм результатов опроса |

``` <?$APPLICATION->IncludeComponent("bitrix:voting.list","",Array(
 		"CHANNEL_SID" => "BOOKS_VOTE", 
 		"VOTE_FORM_TEMPLATE" => "vote_new.php?VOTE_ID=#VOTE_ID#", 
 		"VOTE_RESULT_TEMPLATE" => "vote_result.php?VOTE_ID=#VOTE_ID#" 
 	),
 );?>
  ```