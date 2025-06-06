|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| Путь к скриптам |

| Указывается путь, где расположены административные скрипты |
| Путь к файлу меню |

| Указывается путь |
| Имя события |

| Наименование события формирования пунктов меню |
| Заголовок меню |

```
<?$APPLICATION->IncludeComponent(

'bitrix:mobileapp.menu',

'.default',

[

'SYNC_REQUEST_PATH' => '/bitrix/admin/mobile',

'MENU_FILE_PATH' => '/bitrix/admin/mobile/.mobile_menu.php',

'BUILD_MENU_EVENT_NAME' => 'OnBeforeAdminMobileMenuBuild',

'MENU_TITLE' => 'Администратор'

],

false,

Array('HIDE_ICONS' => 'Y'));

?>


```