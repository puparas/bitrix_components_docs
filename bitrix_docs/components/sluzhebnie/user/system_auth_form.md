|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Дополнительно** |

| |
| Страница регистрации |

| Указывается путь к странице регистрации пользователя. |
| Страница забытого пароля |

| Указывается путь к странице восстановления пароля. |
| Страница профиля |

| Указывается путь к странице с параметрами пользователя. |
| Показывать ошибки |

```
<?$APPLICATION->IncludeComponent("bitrix:system.auth.form","",Array(

     "REGISTER_URL" => "register.php",

     "FORGOT_PASSWORD_URL" => "",

     "PROFILE_URL" => "profile.php",

     "SHOW_ERRORS" => "Y" 

     )

);?>
```