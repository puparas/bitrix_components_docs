| Поле | Описание |
| --- |

|
| \*Название | Название счетчика. |
| \*Тип |

|
| Формат | Позволяет выводить данные в формате размера файла (Например: Мб).     Поле работает только для типов **Целое число** и **Число**. |
| Группы |

|
| \*Команда | Поле для ввода PHP-кода счетчика. |

### Закладка Группы

| Поле | Описание |
| --- |

|
| Группы | Установка флажка для групп сайтов для которых должен применяться данный счетчик.    Подключение счетчика возможно и на закладке **Счетчики** на странице редактирования группы. |

### Закладка Команда

| Поле | Описание |
| --- |

```
$counter = 0;

$rsUsers = CUser::GetList($o="ID", $b="asc", array("ACTIVE"=>"Y","=UF_DEPARTMENT"=>false), array("SELECT"=>array("ID")));

while($arUser = $rsUsers->Fetch())

  if($arUser["EXTERNAL_AUTH_ID"] !== "__controller")

    $counter++;

return $counter;
```

```
$max_size = 5*1024*1024*1024;

COption::SetOptionString("main_size", "~max_size", $max_size);

return $max_size;
```

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