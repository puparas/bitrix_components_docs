| Поле | Описание |
| --- |

|
| Использовать для видеозвонков SFU сервер Voximplant | Если опция включена, то медиа-поток звонка пойдет через сервера VoxImplant и будет разрешено подключение до 48 участников. Если не стоит - медиа-поток идет напрямую между участниками, разрешено до 4-х участников. По умолчанию не стоит.   Доступно только в "Битрикс24 в коробке" |
| Использовать свой TURN сервер видеозвонков |

|
| Скрывать отсутствующих пользователей | При отмеченной опции отсутствующие пользователи по умолчанию будут скрыты в контакт-листе. Каждый пользователь может включать или выключать данную опцию в [настройках Бизнес-чата](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=71&LESSON_ID=7487) в публичной части. |
| Скрывать группы пользователей |

|
| Загружать последние сообщения | При отмеченной опции по умочланию будут загружены последние сообщения в диалогах. Каждый пользователь может включать или выключать данную опцию в [настройках Бизнес-чата](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=71&LESSON_ID=7487) в публичной части. |
| Загружать историю уведомлений |

|
| Сочетание клавиш для отправки сообщения | Указывается сочетание клавиш для отправки сообщений: **Enter** или **Ctrl + Enter** по умолчанию. |
| Расположение панели мессенджера |

|
| Принимать сообщения от | Указывается, от кого разрешено получать сообщения по умолчанию.    Доступно только в "1С-Битрикс: Управление сайтом" |
| Принимать звонки от |

|
| Приглашать в чат могут | Указывается, от кого разрешено получать приглашение в чат по умолчанию.   Доступно только в "1С-Битрикс: Управление сайтом" |
| Отображать контакт при поиске для |

|
| При приглашении пользователя в чат, ему доступна история сообщений | Указывается, как показывать историю сообщений группового чата при приглашении в него нового участника:  * **с момента входа** - ранние сообщения участников группового чата приглашенному участнику будут не видны; * **с первого сообщения** - будут видны все сообщения с момента создания чата. |
| Включить цветовую схему для чатов и пользователей |

|
| Включить открытые чаты | При отмеченной опции будут включены [Открытые чаты](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=71&LESSON_ID=7491#chats), в том числе и **Общий чат**. |
| Включить предварительную загрузку всех пользователей портала для быстрого поиска |

|
| Включить автоматическое сообщение о новом сотруднике в общий чат | При отмеченной опции в Общий чат будет приходить сообщение о принятии на работу нового сотрудника.   Доступно только в "Битрикс24 в коробке" |
| Включить автоматическое сообщение об увольнении сотрудника в общий чат |

|
| Настройки по сайтам или порталам | |
| Формат отображения имени в списке контактов |

```
  

  CREATE fulltext index IXF_IM_MESS_1 on b_im_message


  ```