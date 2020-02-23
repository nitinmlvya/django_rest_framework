# django_rest_framework

## Run project

`
python manage.py runserver
`

## Make Migrations

`
python manage.py makemigrations <app_name>
`
## Migrate after make migrations

`
python manage.py migrate <app_name>
`

### Steps:
- get_started


### Reset migrations
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html


### SQL Setups query:
`INSERT INTO `db_django_rf`.`auth_user`
(`id`,
`password`,
`last_login`,
`is_superuser`,
`email`,
`username`,
`first_name`,
`last_name`,
`date_joined`,
`role_id`)
VALUES
(1,
'admin',
null,
1,
'admin@test.com',
'admin',
'admin',
'admin',
'2020-02-23 05:31:47',
1);

INSERT INTO `db_django_rf`.`auth_role`
(`id`,
`name`)
VALUES
(1,
'admin');
`