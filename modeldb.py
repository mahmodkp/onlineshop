# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'accounts_customuser'


class AccountsCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AccountsCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Table1(models.Model):
    name = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    instance_code = models.BigIntegerField(blank=True, null=True)
    namad_code = models.TextField(blank=True, null=True)
    industry_code = models.BigIntegerField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    first_price = models.BigIntegerField(blank=True, null=True)
    yesterday_price = models.BigIntegerField(blank=True, null=True)
    close_price = models.BigIntegerField(blank=True, null=True)
    close_price_change = models.BigIntegerField(blank=True, null=True)
    close_price_change_percent = models.FloatField(blank=True, null=True)
    final_price = models.BigIntegerField(blank=True, null=True)
    final_price_change = models.BigIntegerField(blank=True, null=True)
    final_price_change_percent = models.FloatField(blank=True, null=True)
    eps = models.TextField(blank=True, null=True)
    free_float = models.BigIntegerField(blank=True, null=True)
    highest_price = models.BigIntegerField(blank=True, null=True)
    lowest_price = models.BigIntegerField(blank=True, null=True)
    daily_price_high = models.BigIntegerField(blank=True, null=True)
    daily_price_low = models.BigIntegerField(blank=True, null=True)
    p_e = models.FloatField(db_column='P:E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_number = models.BigIntegerField(blank=True, null=True)
    trade_volume = models.BigIntegerField(blank=True, null=True)
    trade_value = models.BigIntegerField(blank=True, null=True)
    all_stocks = models.BigIntegerField(blank=True, null=True)
    basis_volume = models.BigIntegerField(blank=True, null=True)
    real_buy_volume = models.BigIntegerField(blank=True, null=True)
    co_buy_volume = models.BigIntegerField(blank=True, null=True)
    real_sell_volume = models.BigIntegerField(blank=True, null=True)
    co_sell_volume = models.BigIntegerField(blank=True, null=True)
    real_buy_value = models.BigIntegerField(blank=True, null=True)
    co_buy_value = models.BigIntegerField(blank=True, null=True)
    real_sell_value = models.BigIntegerField(blank=True, null=True)
    co_sell_value = models.BigIntegerField(blank=True, null=True)
    real_buy_count = models.BigIntegerField(blank=True, null=True)
    co_buy_count = models.BigIntegerField(blank=True, null=True)
    real_sell_count = models.BigIntegerField(blank=True, null=True)
    co_sell_count = models.BigIntegerField(blank=True, null=True)
    market_value = models.BigIntegerField(blank=True, null=True)
    marketdate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class TableName(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    instance_code = models.BigIntegerField(blank=True, null=True)
    namad_code = models.TextField(blank=True, null=True)
    industry_code = models.BigIntegerField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    first_price = models.BigIntegerField(blank=True, null=True)
    yesterday_price = models.BigIntegerField(blank=True, null=True)
    close_price = models.BigIntegerField(blank=True, null=True)
    close_price_change = models.BigIntegerField(blank=True, null=True)
    close_price_change_percent = models.FloatField(blank=True, null=True)
    final_price = models.BigIntegerField(blank=True, null=True)
    final_price_change = models.BigIntegerField(blank=True, null=True)
    final_price_change_percent = models.FloatField(blank=True, null=True)
    eps = models.TextField(blank=True, null=True)
    free_float = models.BigIntegerField(blank=True, null=True)
    highest_price = models.BigIntegerField(blank=True, null=True)
    lowest_price = models.BigIntegerField(blank=True, null=True)
    daily_price_high = models.BigIntegerField(blank=True, null=True)
    daily_price_low = models.BigIntegerField(blank=True, null=True)
    p_e = models.FloatField(db_column='P:E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_number = models.BigIntegerField(blank=True, null=True)
    trade_volume = models.BigIntegerField(blank=True, null=True)
    trade_value = models.BigIntegerField(blank=True, null=True)
    all_stocks = models.BigIntegerField(blank=True, null=True)
    basis_volume = models.BigIntegerField(blank=True, null=True)
    real_buy_volume = models.BigIntegerField(blank=True, null=True)
    co_buy_volume = models.BigIntegerField(blank=True, null=True)
    real_sell_volume = models.BigIntegerField(blank=True, null=True)
    co_sell_volume = models.BigIntegerField(blank=True, null=True)
    real_buy_value = models.BigIntegerField(blank=True, null=True)
    co_buy_value = models.BigIntegerField(blank=True, null=True)
    real_sell_value = models.BigIntegerField(blank=True, null=True)
    co_sell_value = models.BigIntegerField(blank=True, null=True)
    real_buy_count = models.BigIntegerField(blank=True, null=True)
    co_buy_count = models.BigIntegerField(blank=True, null=True)
    real_sell_count = models.BigIntegerField(blank=True, null=True)
    co_sell_count = models.BigIntegerField(blank=True, null=True)
    market_value = models.BigIntegerField(blank=True, null=True)
    marketdate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_name'
