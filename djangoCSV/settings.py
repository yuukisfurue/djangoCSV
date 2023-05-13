"""
Django settings for djangoCSV project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'guest', #☆
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoCSV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoCSV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admindjango',
        'USER': 'furueyuuki',
        'PASSWORD': '769Yuvua@_ho9088Ok58765',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PREFECTURES = [ 
    ("北海道"  ,"北海道"  ),  
    ("青森県"  ,"青森県"  ),  
    ("岩手県"  ,"岩手県"  ),  
    ("宮城県"  ,"宮城県"  ),  
    ("秋田県"  ,"秋田県"  ),  
    ("山形県"  ,"山形県"  ),  
    ("福島県"  ,"福島県"  ),  
    ("茨城県"  ,"茨城県"  ),  
    ("栃木県"  ,"栃木県"  ),  
    ("群馬県"  ,"群馬県"  ),  
    ("埼玉県"  ,"埼玉県"  ),  
    ("千葉県"  ,"千葉県"  ),  
    ("東京都"  ,"東京都"  ),  
    ("神奈川県" ,"神奈川県"),
    ("新潟県"  ,"新潟県"  ),  
    ("富山県"  ,"富山県"  ),  
    ("石川県"  ,"石川県"  ),  
    ("福井県"  ,"福井県"  ),  
    ("山梨県"  ,"山梨県"  ),  
    ("長野県"  ,"長野県"  ),  
    ("岐阜県"  ,"岐阜県"  ),  
    ("静岡県"  ,"静岡県"  ),  
    ("愛知県"  ,"愛知県"  ),  
    ("三重県"  ,"三重県"  ),  
    ("滋賀県"  ,"滋賀県"  ),  
    ("京都府"  ,"京都府"  ),  
    ("大阪府"  ,"大阪府"  ),  
    ("兵庫県"  ,"兵庫県"  ),  
    ("奈良県"  ,"奈良県"  ),  
    ("和歌山県" ,"和歌山県"),
    ("鳥取県"  ,"鳥取県"  ),  
    ("島根県"  ,"島根県"  ),  
    ("岡山県"  ,"岡山県"  ),  
    ("広島県"  ,"広島県"  ),  
    ("山口県"  ,"山口県"  ),  
    ("徳島県"  ,"徳島県"  ),  
    ("香川県"  ,"香川県"  ),  
    ("愛媛県"  ,"愛媛県"  ),  
    ("高知県"  ,"高知県"  ),  
    ("福岡県"  ,"福岡県"  ),  
    ("佐賀県"  ,"佐賀県"  ),  
    ("長崎県"  ,"長崎県"  ),  
    ("熊本県"  ,"熊本県"  ),  
    ("大分県"  ,"大分県"  ),  
    ("宮崎県"  ,"宮崎県"  ),  
    ("鹿児島県" ,"鹿児島県"),
    ("沖縄県"  ,"沖縄県"  ),  
]


GENDERS = [ 
    ("男性"  ,"男性"  ),  
    ("女性"  ,"女性"  ),  
]


EMPLOYMENTSTATUSS = [
     ( "正社員" ,"正社員" ), 
     ( "派遣社員" ,"派遣社員" ), 
     ( "契約社員" ,"契約社員" ), 
     ( "業務委託" ,"業務委託" ), 
     ( "アルバイト" ,"アルバイト" ), 
     ( "正職員" ,"正職員" ),
     ( "非常勤" ,"非常勤" ),
] 

COMPANYS = [
     ( "管理部" ,"管理部" ), 
     ( "営業部" ,"営業部" ), 
     ( "システム部" ,"システム部" ), 
     ( "財務経理部" ,"財務経理部" ), 
     ( "法務部" ,"法務部" ), 
     ( "総務人事部" ,"総務人事部" ),

] 

JYOBS = [
     ( "経営管理部" ,"経営管理部" ), 
     ( "事業企画部" ,"事業企画部" ), 
     ( "品質管理部" ,"品質管理部" ),      
     ( "第一営業部" ,"第一営業部" ), 
     ( "第二営業部" ,"第二営業部" ),
     ( "財務部" ,"財務部" ), 
     ( "経理部" ,"経理部" ), 
     ( "インフラ設計G" ,"インフラ設計G" ), 
     ( "開発設計G" ,"開発設計G" ),    
     ( "法務課" ,"法務課" ), 
     ( "総務課" ,"総務課" ), 
     ( "人事課" ,"人事課" ), 
     ( "広報企画部" ,"広報企画部" ), 
     ( "人材管理T" ,"人材管理T" ),
     ( "採用T" ,"採用T" ),       
] 

STAYS = [

    ("千代田区"  ,"千代田区"  ),  
    ("中央区"  ,"中央区"  ),  
    ("港区"  ,"港区"  ),  
    ("渋谷区"  ,"渋谷区"  ),  
    ("新宿区"  ,"新宿区"  ),  
    ("豊島区"  ,"豊島区"  ),  
    ("文京区"  ,"文京区"  ),  
    ("品川区"  ,"品川区"  ),  
    ("目黒区"  ,"目黒区"  ),  
    ("大田区"  ,"大田区"  ),  
    ("世田谷区"  ,"世田谷区"  ),  
    ("中野区"  ,"中野区"  ),  
    ("杉並区"  ,"杉並区"  ),  
    ("練馬区" ,"練馬区"),
    ("板橋区"  ,"板橋区"  ),  
    ("北区"  ,"北区"  ),  
    ("足立区"  ,"足立区"  ),  
    ("葛飾区"  ,"葛飾区"  ),  
    ("荒川区"  ,"荒川区"  ),  
    ("台東区"  ,"台東区"  ),  
    ("墨田区"  ,"墨田区"  ),  
    ("江東区"  ,"江東区"  ),  
    ("江戸川区"  ,"江戸川区"  ),  
    
]

AFFILIATONS = [
     ( "フロントラインT" ,"フロントラインT" ), 
     ( "プロモーションT" ,"プロモーションT" ), 
     ( "IセールスT" ,"IセールスT" ), 
     ( "CサクセスT" ,"CサクセスT" ),
     ( "事業管理T" ,"事業管理T" ), 
     ( "構成管理T" ,"構成管理T" ), 
     ( "品質管理T" ,"品質管理T" ), 
     ( "会計1課" ,"会計1課" ),
     ( "会計2課" ,"会計2課" ),  
     ( "設計構築T" ,"設計構築T" ), 
     ( "運用保守T" ,"運用保守T" ), 
     ( "設計開発T" ,"設計開発T" ), 
     ( "広報T" ,"広報T" ), 
     ( "企画T" ,"企画T" ), 
     ( "第一法務部" ,"第一法務部" ), 
     ( "第二法務部" ,"第二法務部" ), 
     ( "人材管理T" ,"人材管理T" ),
     ( "採用T" ,"採用T" ),    

] 

POSITIONS = [
     ( "メンバー" ,"メンバー" ),
     ( "リーダー" ,"リーダー" ), 
     ( "PL" ,"PL" ), 
     ( "PMO" ,"PMO" ), 
     ( "PM" ,"PM" ), 
     ( "係長" ,"係長" ), 
     ( "部長" ,"部長" ), 
     ( "課長" ,"課長" ), 
     ("会社役員"  ,"会社役員" ),  
     ("取締役"  ,"取締役" ), 
] 

ANNUALS= [
     ( "200" ,"200" ),
     ( "250" ,"250" ), 
     ( "300" ,"300" ), 
     ( "350" ,"350" ), 
     ( "400" ,"400" ), 
     ( "450" ,"450" ), 
     ( "500" ,"500" ), 
     ( "550" ,"550" ), 
     ( "600" ,"600" ), 
     ( "650" ,"650" ), 
     ( "700" ,"700" ), 
     ( "750" ,"750" ), 
     ( "800~" ,"800~" ), 
]

LASTYEARS = [
     ( "200" ,"200" ),
     ( "250" ,"250" ), 
     ( "300" ,"300" ), 
     ( "350" ,"350" ), 
     ( "400" ,"400" ), 
     ( "450" ,"450" ), 
     ( "500" ,"500" ), 
     ( "550" ,"550" ), 
     ( "600" ,"600" ), 
     ( "650" ,"650" ), 
     ( "700" ,"700" ), 
     ( "750" ,"750" ), 
     ( "800~" ,"800~" ), 
]