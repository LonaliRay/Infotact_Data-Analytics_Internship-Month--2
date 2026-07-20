{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaoOEcyM481IUqXKj8wEAN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LonaliRay/Infotact_Data-Analytics_Internship-Month-2/blob/main/datacleaning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "oQoptYtw2Njy"
      },
      "outputs": [],
      "source": [
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "customers = pd.read_csv('olist_customers_dataset.csv')\n",
        "orders = pd.read_csv('olist_orders_dataset.csv')\n",
        "order_items = pd.read_csv('olist_order_items_dataset.csv')\n",
        "payments = pd.read_csv('olist_order_payments_dataset.csv')\n",
        "products = pd.read_csv('olist_products_dataset.csv')\n",
        "reviews = pd.read_csv('olist_order_reviews_dataset.csv')\n",
        "sellers = pd.read_csv('olist_sellers_dataset.csv')\n",
        "geolocation = pd.read_csv('olist_geolocation_dataset.csv')"
      ],
      "metadata": {
        "id": "1DnJlNzJ2fKh"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "list1=[customers,order_items,orders,payments,sellers,reviews,products,geolocation]"
      ],
      "metadata": {
        "id": "6Zxd6MwS5kpJ"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "print(os.getcwd())\n",
        "print(os.listdir())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-CqRl-7N32Sh",
        "outputId": "13180f49-62a7-4401-ad05-eac0293f7f0a"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content\n",
            "['.config', 'olist_sellers_dataset.csv', 'olist_order_items_dataset.csv', 'olist_order_reviews_dataset.csv', 'olist_customers_dataset.csv', 'olist_orders_dataset.csv', 'olist_products_dataset.csv', 'olist_order_payments_dataset.csv', 'olist_geolocation_dataset.csv', 'sample_data']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in list1:\n",
        "  print(i.head())\n",
        "  print(i.shape)\n",
        "  print(i.duplicated())\n",
        "  i.info()\n",
        "  print(i.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TW6JNzjT5rEJ",
        "outputId": "238671d6-3852-4972-a3a3-587bb5c45f9d"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                        customer_id                customer_unique_id  \\\n",
            "0  06b8999e2fba1a1fbc88172c00ba8bc7  861eff4711a542e4b93843c6dd7febb0   \n",
            "1  18955e83d337fd6b2def6b18a428ac77  290c77bc529b7ac935b93aa66c333dc3   \n",
            "2  4e7b3e00288586ebd08712fdd0374a03  060e732b5b29e8181a18229c7b0b2b5e   \n",
            "3  b2b6027bc5c5109e529d4dc6358b12c3  259dac757896d24d7702b9acbbff3f3c   \n",
            "4  4f2d8ab171c80ec8364f7c12e35b23ad  345ecd01c38d18a9036ed96c73b8d066   \n",
            "\n",
            "   customer_zip_code_prefix          customer_city customer_state  \n",
            "0                     14409                 franca             SP  \n",
            "1                      9790  sao bernardo do campo             SP  \n",
            "2                      1151              sao paulo             SP  \n",
            "3                      8775        mogi das cruzes             SP  \n",
            "4                     13056               campinas             SP  \n",
            "(99441, 5)\n",
            "0        False\n",
            "1        False\n",
            "2        False\n",
            "3        False\n",
            "4        False\n",
            "         ...  \n",
            "99436    False\n",
            "99437    False\n",
            "99438    False\n",
            "99439    False\n",
            "99440    False\n",
            "Length: 99441, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 99441 entries, 0 to 99440\n",
            "Data columns (total 5 columns):\n",
            " #   Column                    Non-Null Count  Dtype \n",
            "---  ------                    --------------  ----- \n",
            " 0   customer_id               99441 non-null  object\n",
            " 1   customer_unique_id        99441 non-null  object\n",
            " 2   customer_zip_code_prefix  99441 non-null  int64 \n",
            " 3   customer_city             99441 non-null  object\n",
            " 4   customer_state            99441 non-null  object\n",
            "dtypes: int64(1), object(4)\n",
            "memory usage: 3.8+ MB\n",
            "customer_id                 0\n",
            "customer_unique_id          0\n",
            "customer_zip_code_prefix    0\n",
            "customer_city               0\n",
            "customer_state              0\n",
            "dtype: int64\n",
            "                           order_id  order_item_id  \\\n",
            "0  00010242fe8c5a6d1ba2dd792cb16214              1   \n",
            "1  00018f77f2f0320c557190d7a144bdd3              1   \n",
            "2  000229ec398224ef6ca0657da4fc703e              1   \n",
            "3  00024acbcdf0a6daa1e931b038114c75              1   \n",
            "4  00042b26cf59d7ce69dfabb4e55b4fd9              1   \n",
            "\n",
            "                         product_id                         seller_id  \\\n",
            "0  4244733e06e7ecb4970a6e2683c13e61  48436dade18ac8b2bce089ec2a041202   \n",
            "1  e5f2d52b802189ee658865ca93d83a8f  dd7ddc04e1b6c2c614352b383efe2d36   \n",
            "2  c777355d18b72b67abbeef9df44fd0fd  5b51032eddd242adc84c38acab88f23d   \n",
            "3  7634da152a4610f1595efa32f14722fc  9d7a1d34a5052409006425275ba1c2b4   \n",
            "4  ac6c3623068f30de03045865e4e10089  df560393f3a51e74553ab94004ba5c87   \n",
            "\n",
            "   shipping_limit_date   price  freight_value  \n",
            "0  2017-09-19 09:45:35   58.90          13.29  \n",
            "1  2017-05-03 11:05:13  239.90          19.93  \n",
            "2  2018-01-18 14:48:30  199.00          17.87  \n",
            "3  2018-08-15 10:10:18   12.99          12.79  \n",
            "4  2017-02-13 13:57:51  199.90          18.14  \n",
            "(112650, 7)\n",
            "0         False\n",
            "1         False\n",
            "2         False\n",
            "3         False\n",
            "4         False\n",
            "          ...  \n",
            "112645    False\n",
            "112646    False\n",
            "112647    False\n",
            "112648    False\n",
            "112649    False\n",
            "Length: 112650, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 112650 entries, 0 to 112649\n",
            "Data columns (total 7 columns):\n",
            " #   Column               Non-Null Count   Dtype  \n",
            "---  ------               --------------   -----  \n",
            " 0   order_id             112650 non-null  object \n",
            " 1   order_item_id        112650 non-null  int64  \n",
            " 2   product_id           112650 non-null  object \n",
            " 3   seller_id            112650 non-null  object \n",
            " 4   shipping_limit_date  112650 non-null  object \n",
            " 5   price                112650 non-null  float64\n",
            " 6   freight_value        112650 non-null  float64\n",
            "dtypes: float64(2), int64(1), object(4)\n",
            "memory usage: 6.0+ MB\n",
            "order_id               0\n",
            "order_item_id          0\n",
            "product_id             0\n",
            "seller_id              0\n",
            "shipping_limit_date    0\n",
            "price                  0\n",
            "freight_value          0\n",
            "dtype: int64\n",
            "                           order_id                       customer_id  \\\n",
            "0  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   \n",
            "1  53cdb2fc8bc7dce0b6741e2150273451  b0830fb4747a6c6d20dea0b8c802d7ef   \n",
            "2  47770eb9100c2d0c44946d9cf07ec65d  41ce2a54c0b03bf3443c3d931a367089   \n",
            "3  949d5b44dbf5de918fe9c16f97b45f8a  f88197465ea7920adcdbec7375364d82   \n",
            "4  ad21c59c0840e6cb83a9ceb5573f8159  8ab97904e6daea8866dbdbc4fb7aad2c   \n",
            "\n",
            "  order_status order_purchase_timestamp    order_approved_at  \\\n",
            "0    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   \n",
            "1    delivered      2018-07-24 20:41:37  2018-07-26 03:24:27   \n",
            "2    delivered      2018-08-08 08:38:49  2018-08-08 08:55:23   \n",
            "3    delivered      2017-11-18 19:28:06  2017-11-18 19:45:59   \n",
            "4    delivered      2018-02-13 21:18:39  2018-02-13 22:20:29   \n",
            "\n",
            "  order_delivered_carrier_date order_delivered_customer_date  \\\n",
            "0          2017-10-04 19:55:00           2017-10-10 21:25:13   \n",
            "1          2018-07-26 14:31:00           2018-08-07 15:27:45   \n",
            "2          2018-08-08 13:50:00           2018-08-17 18:06:29   \n",
            "3          2017-11-22 13:39:59           2017-12-02 00:28:42   \n",
            "4          2018-02-14 19:46:34           2018-02-16 18:17:02   \n",
            "\n",
            "  order_estimated_delivery_date  \n",
            "0           2017-10-18 00:00:00  \n",
            "1           2018-08-13 00:00:00  \n",
            "2           2018-09-04 00:00:00  \n",
            "3           2017-12-15 00:00:00  \n",
            "4           2018-02-26 00:00:00  \n",
            "(99441, 8)\n",
            "0        False\n",
            "1        False\n",
            "2        False\n",
            "3        False\n",
            "4        False\n",
            "         ...  \n",
            "99436    False\n",
            "99437    False\n",
            "99438    False\n",
            "99439    False\n",
            "99440    False\n",
            "Length: 99441, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 99441 entries, 0 to 99440\n",
            "Data columns (total 8 columns):\n",
            " #   Column                         Non-Null Count  Dtype \n",
            "---  ------                         --------------  ----- \n",
            " 0   order_id                       99441 non-null  object\n",
            " 1   customer_id                    99441 non-null  object\n",
            " 2   order_status                   99441 non-null  object\n",
            " 3   order_purchase_timestamp       99441 non-null  object\n",
            " 4   order_approved_at              99281 non-null  object\n",
            " 5   order_delivered_carrier_date   97658 non-null  object\n",
            " 6   order_delivered_customer_date  96476 non-null  object\n",
            " 7   order_estimated_delivery_date  99441 non-null  object\n",
            "dtypes: object(8)\n",
            "memory usage: 6.1+ MB\n",
            "order_id                            0\n",
            "customer_id                         0\n",
            "order_status                        0\n",
            "order_purchase_timestamp            0\n",
            "order_approved_at                 160\n",
            "order_delivered_carrier_date     1783\n",
            "order_delivered_customer_date    2965\n",
            "order_estimated_delivery_date       0\n",
            "dtype: int64\n",
            "                           order_id  payment_sequential payment_type  \\\n",
            "0  b81ef226f3fe1789b1e8b2acac839d17                   1  credit_card   \n",
            "1  a9810da82917af2d9aefd1278f1dcfa0                   1  credit_card   \n",
            "2  25e8ea4e93396b6fa0d3dd708e76c1bd                   1  credit_card   \n",
            "3  ba78997921bbcdc1373bb41e913ab953                   1  credit_card   \n",
            "4  42fdf880ba16b47b59251dd489d4441a                   1  credit_card   \n",
            "\n",
            "   payment_installments  payment_value  \n",
            "0                     8          99.33  \n",
            "1                     1          24.39  \n",
            "2                     1          65.71  \n",
            "3                     8         107.78  \n",
            "4                     2         128.45  \n",
            "(103886, 5)\n",
            "0         False\n",
            "1         False\n",
            "2         False\n",
            "3         False\n",
            "4         False\n",
            "          ...  \n",
            "103881    False\n",
            "103882    False\n",
            "103883    False\n",
            "103884    False\n",
            "103885    False\n",
            "Length: 103886, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 103886 entries, 0 to 103885\n",
            "Data columns (total 5 columns):\n",
            " #   Column                Non-Null Count   Dtype  \n",
            "---  ------                --------------   -----  \n",
            " 0   order_id              103886 non-null  object \n",
            " 1   payment_sequential    103886 non-null  int64  \n",
            " 2   payment_type          103886 non-null  object \n",
            " 3   payment_installments  103886 non-null  int64  \n",
            " 4   payment_value         103886 non-null  float64\n",
            "dtypes: float64(1), int64(2), object(2)\n",
            "memory usage: 4.0+ MB\n",
            "order_id                0\n",
            "payment_sequential      0\n",
            "payment_type            0\n",
            "payment_installments    0\n",
            "payment_value           0\n",
            "dtype: int64\n",
            "                          seller_id  seller_zip_code_prefix  \\\n",
            "0  3442f8959a84dea7ee197c632cb2df15                   13023   \n",
            "1  d1b65fc7debc3361ea86b5f14c68d2e2                   13844   \n",
            "2  ce3ad9de960102d0677a81f5d0bb7b2d                   20031   \n",
            "3  c0f3eea2e14555b6faeea3dd58c1b1c3                    4195   \n",
            "4  51a04a8a6bdcb23deccc82b0b80742cf                   12914   \n",
            "\n",
            "         seller_city seller_state  \n",
            "0           campinas           SP  \n",
            "1         mogi guacu           SP  \n",
            "2     rio de janeiro           RJ  \n",
            "3          sao paulo           SP  \n",
            "4  braganca paulista           SP  \n",
            "(3095, 4)\n",
            "0       False\n",
            "1       False\n",
            "2       False\n",
            "3       False\n",
            "4       False\n",
            "        ...  \n",
            "3090    False\n",
            "3091    False\n",
            "3092    False\n",
            "3093    False\n",
            "3094    False\n",
            "Length: 3095, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 3095 entries, 0 to 3094\n",
            "Data columns (total 4 columns):\n",
            " #   Column                  Non-Null Count  Dtype \n",
            "---  ------                  --------------  ----- \n",
            " 0   seller_id               3095 non-null   object\n",
            " 1   seller_zip_code_prefix  3095 non-null   int64 \n",
            " 2   seller_city             3095 non-null   object\n",
            " 3   seller_state            3095 non-null   object\n",
            "dtypes: int64(1), object(3)\n",
            "memory usage: 96.8+ KB\n",
            "seller_id                 0\n",
            "seller_zip_code_prefix    0\n",
            "seller_city               0\n",
            "seller_state              0\n",
            "dtype: int64\n",
            "                          review_id                          order_id  \\\n",
            "0  7bc2406110b926393aa56f80a40eba40  73fc7af87114b39712e6da79b0a377eb   \n",
            "1  80e641a11e56f04c1ad469d5645fdfde  a548910a1c6147796b98fdf73dbeba33   \n",
            "2  228ce5500dc1d8e020d8d1322874b6f0  f9e4b658b201a9f2ecdecbb34bed034b   \n",
            "3  e64fb393e7b32834bb789ff8bb30750e  658677c97b385a9be170737859d3511b   \n",
            "4  f7c4243c7fe1938f181bec41a392bdeb  8e6bfb81e283fa7e4f11123a3fb894f1   \n",
            "\n",
            "   review_score review_comment_title  \\\n",
            "0             4                  NaN   \n",
            "1             5                  NaN   \n",
            "2             5                  NaN   \n",
            "3             5                  NaN   \n",
            "4             5                  NaN   \n",
            "\n",
            "                              review_comment_message review_creation_date  \\\n",
            "0                                                NaN  2018-01-18 00:00:00   \n",
            "1                                                NaN  2018-03-10 00:00:00   \n",
            "2                                                NaN  2018-02-17 00:00:00   \n",
            "3              Recebi bem antes do prazo estipulado.  2017-04-21 00:00:00   \n",
            "4  Parabéns lojas lannister adorei comprar pela I...  2018-03-01 00:00:00   \n",
            "\n",
            "  review_answer_timestamp  \n",
            "0     2018-01-18 21:46:59  \n",
            "1     2018-03-11 03:05:13  \n",
            "2     2018-02-18 14:36:24  \n",
            "3     2017-04-21 22:02:06  \n",
            "4     2018-03-02 10:26:53  \n",
            "(99224, 7)\n",
            "0        False\n",
            "1        False\n",
            "2        False\n",
            "3        False\n",
            "4        False\n",
            "         ...  \n",
            "99219    False\n",
            "99220    False\n",
            "99221    False\n",
            "99222    False\n",
            "99223    False\n",
            "Length: 99224, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 99224 entries, 0 to 99223\n",
            "Data columns (total 7 columns):\n",
            " #   Column                   Non-Null Count  Dtype \n",
            "---  ------                   --------------  ----- \n",
            " 0   review_id                99224 non-null  object\n",
            " 1   order_id                 99224 non-null  object\n",
            " 2   review_score             99224 non-null  int64 \n",
            " 3   review_comment_title     11568 non-null  object\n",
            " 4   review_comment_message   40977 non-null  object\n",
            " 5   review_creation_date     99224 non-null  object\n",
            " 6   review_answer_timestamp  99224 non-null  object\n",
            "dtypes: int64(1), object(6)\n",
            "memory usage: 5.3+ MB\n",
            "review_id                      0\n",
            "order_id                       0\n",
            "review_score                   0\n",
            "review_comment_title       87656\n",
            "review_comment_message     58247\n",
            "review_creation_date           0\n",
            "review_answer_timestamp        0\n",
            "dtype: int64\n",
            "                         product_id  product_category_name  \\\n",
            "0  1e9e8ef04dbcff4541ed26657ea517e5             perfumaria   \n",
            "1  3aa071139cb16b67ca9e5dea641aaa2f                  artes   \n",
            "2  96bd76ec8810374ed1b65e291975717f          esporte_lazer   \n",
            "3  cef67bcfe19066a932b7673e239eb23d                  bebes   \n",
            "4  9dc1a7de274444849c219cff195d0b71  utilidades_domesticas   \n",
            "\n",
            "   product_name_lenght  product_description_lenght  product_photos_qty  \\\n",
            "0                 40.0                       287.0                 1.0   \n",
            "1                 44.0                       276.0                 1.0   \n",
            "2                 46.0                       250.0                 1.0   \n",
            "3                 27.0                       261.0                 1.0   \n",
            "4                 37.0                       402.0                 4.0   \n",
            "\n",
            "   product_weight_g  product_length_cm  product_height_cm  product_width_cm  \n",
            "0             225.0               16.0               10.0              14.0  \n",
            "1            1000.0               30.0               18.0              20.0  \n",
            "2             154.0               18.0                9.0              15.0  \n",
            "3             371.0               26.0                4.0              26.0  \n",
            "4             625.0               20.0               17.0              13.0  \n",
            "(32951, 9)\n",
            "0        False\n",
            "1        False\n",
            "2        False\n",
            "3        False\n",
            "4        False\n",
            "         ...  \n",
            "32946    False\n",
            "32947    False\n",
            "32948    False\n",
            "32949    False\n",
            "32950    False\n",
            "Length: 32951, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 32951 entries, 0 to 32950\n",
            "Data columns (total 9 columns):\n",
            " #   Column                      Non-Null Count  Dtype  \n",
            "---  ------                      --------------  -----  \n",
            " 0   product_id                  32951 non-null  object \n",
            " 1   product_category_name       32341 non-null  object \n",
            " 2   product_name_lenght         32341 non-null  float64\n",
            " 3   product_description_lenght  32341 non-null  float64\n",
            " 4   product_photos_qty          32341 non-null  float64\n",
            " 5   product_weight_g            32949 non-null  float64\n",
            " 6   product_length_cm           32949 non-null  float64\n",
            " 7   product_height_cm           32949 non-null  float64\n",
            " 8   product_width_cm            32949 non-null  float64\n",
            "dtypes: float64(7), object(2)\n",
            "memory usage: 2.3+ MB\n",
            "product_id                      0\n",
            "product_category_name         610\n",
            "product_name_lenght           610\n",
            "product_description_lenght    610\n",
            "product_photos_qty            610\n",
            "product_weight_g                2\n",
            "product_length_cm               2\n",
            "product_height_cm               2\n",
            "product_width_cm                2\n",
            "dtype: int64\n",
            "   geolocation_zip_code_prefix  geolocation_lat  geolocation_lng  \\\n",
            "0                         1037       -23.545621       -46.639292   \n",
            "1                         1046       -23.546081       -46.644820   \n",
            "2                         1046       -23.546129       -46.642951   \n",
            "3                         1041       -23.544392       -46.639499   \n",
            "4                         1035       -23.541578       -46.641607   \n",
            "\n",
            "  geolocation_city geolocation_state  \n",
            "0        sao paulo                SP  \n",
            "1        sao paulo                SP  \n",
            "2        sao paulo                SP  \n",
            "3        sao paulo                SP  \n",
            "4        sao paulo                SP  \n",
            "(1000163, 5)\n",
            "0          False\n",
            "1          False\n",
            "2          False\n",
            "3          False\n",
            "4          False\n",
            "           ...  \n",
            "1000158    False\n",
            "1000159     True\n",
            "1000160     True\n",
            "1000161    False\n",
            "1000162     True\n",
            "Length: 1000163, dtype: bool\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1000163 entries, 0 to 1000162\n",
            "Data columns (total 5 columns):\n",
            " #   Column                       Non-Null Count    Dtype  \n",
            "---  ------                       --------------    -----  \n",
            " 0   geolocation_zip_code_prefix  1000163 non-null  int64  \n",
            " 1   geolocation_lat              1000163 non-null  float64\n",
            " 2   geolocation_lng              1000163 non-null  float64\n",
            " 3   geolocation_city             1000163 non-null  object \n",
            " 4   geolocation_state            1000163 non-null  object \n",
            "dtypes: float64(2), int64(1), object(2)\n",
            "memory usage: 38.2+ MB\n",
            "geolocation_zip_code_prefix    0\n",
            "geolocation_lat                0\n",
            "geolocation_lng                0\n",
            "geolocation_city               0\n",
            "geolocation_state              0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Order Status Distribution:\")\n",
        "print(orders['order_status'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bLA578DE6EXx",
        "outputId": "2734ee1e-ebb0-4a0e-98b4-1041b3feac9b"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Order Status Distribution:\n",
            "order_status\n",
            "delivered      96478\n",
            "shipped         1107\n",
            "canceled         625\n",
            "unavailable      609\n",
            "invoiced         314\n",
            "processing       301\n",
            "created            5\n",
            "approved           2\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Keep only delivered orders day 2\n",
        "orders = orders[orders['order_status'] == 'delivered']\n",
        "# Handle missing values in Orders\n",
        "orders = orders.dropna(subset=[\n",
        "    'order_approved_at',\n",
        "    'order_delivered_customer_date'\n",
        "])"
      ],
      "metadata": {
        "id": "ePqHqIWl6WOF"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Handle missing values in Order Items\n",
        "order_items = order_items.dropna()\n",
        "# Handle missing values in Products day 3\n",
        "products['product_category_name'] = products['product_category_name'].fillna('Unknown')\n",
        "products['product_name_lenght'] = products['product_name_lenght'].fillna(0)\n",
        "products['product_description_lenght'] = products['product_description_lenght'].fillna(0)\n",
        "products['product_photos_qty'] = products['product_photos_qty'].fillna(0)\n",
        "products = products.dropna(subset=[\n",
        "    'product_weight_g',\n",
        "    'product_length_cm',\n",
        "    'product_height_cm',\n",
        "    'product_width_cm'\n",
        "])"
      ],
      "metadata": {
        "id": "Ia9V4yPs6sO2"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Verify missing values after cleaning day 4\n",
        "print(\"\\nOrders Missing Values:\")\n",
        "print(orders.isnull().sum())\n",
        "print(\"\\nOrder Items Missing Values:\")\n",
        "print(order_items.isnull().sum())\n",
        "print(\"\\nProducts Missing Values:\")\n",
        "print(products.isnull().sum())\n",
        "# Check final dataset shapes\n",
        "print(\"\\nFinal Dataset Shapes:\")\n",
        "print(\"Orders:\", orders.shape)\n",
        "print(\"Order Items:\", order_items.shape)\n",
        "print(\"Products:\", products.shape)\n",
        "\n",
        "# Convert purchase timestamp into datetime\n",
        "orders['order_purchase_timestamp'] = pd.to_datetime(\n",
        "    orders['order_purchase_timestamp'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eQYI0cQT63s-",
        "outputId": "10dd4625-0a97-4a40-a6d0-f4d17e5875f5"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Orders Missing Values:\n",
            "order_id                         0\n",
            "customer_id                      0\n",
            "order_status                     0\n",
            "order_purchase_timestamp         0\n",
            "order_approved_at                0\n",
            "order_delivered_carrier_date     1\n",
            "order_delivered_customer_date    0\n",
            "order_estimated_delivery_date    0\n",
            "dtype: int64\n",
            "\n",
            "Order Items Missing Values:\n",
            "order_id               0\n",
            "order_item_id          0\n",
            "product_id             0\n",
            "seller_id              0\n",
            "shipping_limit_date    0\n",
            "price                  0\n",
            "freight_value          0\n",
            "dtype: int64\n",
            "\n",
            "Products Missing Values:\n",
            "product_id                    0\n",
            "product_category_name         0\n",
            "product_name_lenght           0\n",
            "product_description_lenght    0\n",
            "product_photos_qty            0\n",
            "product_weight_g              0\n",
            "product_length_cm             0\n",
            "product_height_cm             0\n",
            "product_width_cm              0\n",
            "dtype: int64\n",
            "\n",
            "Final Dataset Shapes:\n",
            "Orders: (96456, 8)\n",
            "Order Items: (112650, 7)\n",
            "Products: (32949, 9)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Extract Purchase Month day 5\n",
        "orders['OrderMonth'] = orders['order_purchase_timestamp'].dt.to_period('M')"
      ],
      "metadata": {
        "id": "lxsn0VVh6_xp"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(orders[['order_purchase_timestamp', 'OrderMonth']].head())\n",
        "print(orders.dtypes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hh_-aGSs7KQT",
        "outputId": "d308bad9-744e-4356-ec74-a19d376fcefa"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  order_purchase_timestamp OrderMonth\n",
            "0      2017-10-02 10:56:33    2017-10\n",
            "1      2018-07-24 20:41:37    2018-07\n",
            "2      2018-08-08 08:38:49    2018-08\n",
            "3      2017-11-18 19:28:06    2017-11\n",
            "4      2018-02-13 21:18:39    2018-02\n",
            "order_id                                 object\n",
            "customer_id                              object\n",
            "order_status                             object\n",
            "order_purchase_timestamp         datetime64[ns]\n",
            "order_approved_at                        object\n",
            "order_delivered_carrier_date             object\n",
            "order_delivered_customer_date            object\n",
            "order_estimated_delivery_date            object\n",
            "OrderMonth                            period[M]\n",
            "dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save cleaned datasets\n",
        "orders.to_csv(\"orders_cleaned.csv\", index=False)\n",
        "order_items.to_csv(\"order_items_cleaned.csv\", index=False)\n",
        "products.to_csv(\"products_cleaned.csv\", index=False)\n",
        "print(\"Cleaned datasets saved successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0p47BIpE7avv",
        "outputId": "e2e3dc31-c84d-43c2-c545-0e22819e11f8"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cleaned datasets saved successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Week2\n",
        "# Find first purchase month for each customer day 8\n",
        "cohort = orders.groupby('customer_id')['OrderMonth'].min().reset_index()\n"
      ],
      "metadata": {
        "id": "3HtnM4bP8DME"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Rename column\n",
        "cohort.rename(columns={'OrderMonth': 'CohortMonth'}, inplace=True)"
      ],
      "metadata": {
        "id": "3fLLORyL8IO9"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Merge with orders dataset\n",
        "orders = orders.merge(cohort, on='customer_id')\n"
      ],
      "metadata": {
        "id": "rhvteQHo8P6x"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Verify\n",
        "print(orders[['customer_id', 'OrderMonth', 'CohortMonth']].head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OuZhHGRy8T9t",
        "outputId": "bc63d318-d061-471a-a556-9c10f369cf25"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                        customer_id OrderMonth CohortMonth\n",
            "0  9ef432eb6251297304e76186b10a928d    2017-10     2017-10\n",
            "1  b0830fb4747a6c6d20dea0b8c802d7ef    2018-07     2018-07\n",
            "2  41ce2a54c0b03bf3443c3d931a367089    2018-08     2018-08\n",
            "3  f88197465ea7920adcdbec7375364d82    2017-11     2017-11\n",
            "4  8ab97904e6daea8866dbdbc4fb7aad2c    2018-02     2018-02\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Calculate year and month difference day 9\n",
        "year_diff = orders['OrderMonth'].dt.year - orders['CohortMonth'].dt.year\n",
        "month_diff = orders['OrderMonth'].dt.month - orders['CohortMonth'].dt.month\n"
      ],
      "metadata": {
        "id": "DU1LcUNA8XQK"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create Cohort Index\n",
        "orders['CohortIndex'] = year_diff * 12 + month_diff + 1\n",
        "# Verify\n",
        "print(orders[['customer_id','OrderMonth','CohortMonth','CohortIndex']].head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QSOKrmav8b7q",
        "outputId": "08644821-2cab-4895-d929-1b9f1f2fb5a6"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                        customer_id OrderMonth CohortMonth  CohortIndex\n",
            "0  9ef432eb6251297304e76186b10a928d    2017-10     2017-10            1\n",
            "1  b0830fb4747a6c6d20dea0b8c802d7ef    2018-07     2018-07            1\n",
            "2  41ce2a54c0b03bf3443c3d931a367089    2018-08     2018-08            1\n",
            "3  f88197465ea7920adcdbec7375364d82    2017-11     2017-11            1\n",
            "4  8ab97904e6daea8866dbdbc4fb7aad2c    2018-02     2018-02            1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Count unique customers day 10\n",
        "cohort_data = orders.groupby(\n",
        "    ['CohortMonth', 'CohortIndex']\n",
        ")['customer_id'].nunique().reset_index()\n"
      ],
      "metadata": {
        "id": "BbnnPc6i8k4q"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create retention matrix\n",
        "retention_matrix = cohort_data.pivot_table(\n",
        "    index='CohortMonth',\n",
        "    columns='CohortIndex',\n",
        "    values='customer_id'\n",
        ")"
      ],
      "metadata": {
        "id": "1LS3M8tf8p9K"
      },
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Verify\n",
        "print(retention_matrix)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gj-DJiQb8usN",
        "outputId": "43ec83a2-c251-4f75-c7d9-a3b855be8c7a"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CohortIndex       1\n",
            "CohortMonth        \n",
            "2016-09         1.0\n",
            "2016-10       265.0\n",
            "2016-12         1.0\n",
            "2017-01       748.0\n",
            "2017-02      1641.0\n",
            "2017-03      2546.0\n",
            "2017-04      2303.0\n",
            "2017-05      3545.0\n",
            "2017-06      3135.0\n",
            "2017-07      3872.0\n",
            "2017-08      4193.0\n",
            "2017-09      4150.0\n",
            "2017-10      4478.0\n",
            "2017-11      7288.0\n",
            "2017-12      5513.0\n",
            "2018-01      7069.0\n",
            "2018-02      6555.0\n",
            "2018-03      7003.0\n",
            "2018-04      6798.0\n",
            "2018-05      6749.0\n",
            "2018-06      6096.0\n",
            "2018-07      6156.0\n",
            "2018-08      6351.0\n"
          ]
        }
      ]
    }
  ]
}