#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Top level script. Calls other functions that generate datasets that this script then creates in HDX.

"""
import logging


from hdx.hdx_configuration import Configuration
from os.path import join
from hdx.data.dataset import Dataset
from unhabitat import getData, generate_dataset_and_showcase
from hdx.facades.simple import facade


logger = logging.getLogger(__name__)

def updateTag(iso2):
    #https://data.humdata.org/dataset/unhabitat-zw-indicators
    iso = iso2.lower()
    url = "unhabitat-%s-indicators" %iso
    print(url)

    dataset = Dataset.read_from_hdx("unhabitat-%s-indicators" %iso)
    # print(dataset)
    dataset.add_tag('INDICATORS')
    dataset.update_in_hdx()

def main():
    """Generate dataset and create it in HDX"""
    countries = {
                 #'Afghanistan': 'AF',
                 # 'Albania': 'AL',
                 # 'Algeria': 'DZ',
                 # 'Andorra': 'AD',
                 # 'Angola': 'AO',
                 # 'Argentina': 'AR',
                 # 'Armenia': 'AM',
                 # 'Aruba': 'AW',
                 # 'Australia': 'AU',
                 # 'Azerbaijan': 'AZ',
                 # 'Bahamas': 'BS',
                 # 'Bahrain': 'BH',
                 # 'Bangladesh': 'BD',
                 # 'Barbados': 'BB',
                 # 'Belarus': 'BY',
                 # 'Belgium': 'BE',
                 # 'Belize': 'BZ',
                 # 'Benin': 'BJ',
                 # 'Bermuda': 'BM',
                 # 'Bhutan': 'BT',
                 # 'Bolivia': 'BO',
                 # 'Botswana': 'BW',
                 # 'Brazil': 'BR',
                 # 'Bulgaria': 'BG',
                 # 'Burkina faso': 'BF',
                 # 'Burundi': 'BI',
                 # 'Cambodia': 'KH',
                 # 'Cameroon': 'CM',
                 # 'Canada': 'CA',
                 # 'Cape verde': 'CV',
                 # 'Central african republic': 'CF',
                 # 'Chad': 'TD',
                 # 'Chile': 'CL',
                 # 'China': 'CN',
                 # 'Colombia': 'CO',
                 # 'Comoros': 'KM',
                 # 'Congo': 'CD',
                 # 'Costa rica': 'CR',
                 # 'Ivory coast': 'CI',
                 # 'Croatia': 'HR',
                 # 'Cuba': 'CU',
                 # 'Cyprus': 'CY',
                 # 'Czech republic': 'CZ',
                 # 'Denmark': 'DK',
                 # 'Djibouti': 'DJ',
                 # 'Dominica': 'DM',
                 # 'Dominican republic': 'DO',
                 # 'Ecuador': 'EC',
                 # 'Egypt': 'EG',
                 # 'El salvador': 'SV',
                 # 'Equatorial guinea': 'GQ',
                 # 'Eritrea': 'ER',
                 # 'Estonia': 'EE',
                 # 'Ethiopia': 'ET',
                 # 'Faroe islands': 'FO',
                 # 'Fiji': 'FJ',
                 # 'Finland': 'FI',
                 # 'France': 'FR',
                 # 'French guiana': 'GF',
                 # 'French polynesia': 'PF',
                 # 'Gabon': 'GA',
                 # 'Gambia': 'GM',
                 # 'Georgia': 'GE',
                 # 'Germany': 'DE',
                 # 'Ghana': 'GH',
                 # 'Gibraltar': 'GI',
                 # 'Greece': 'GR',
                 # 'Guadeloupe': 'GP',
                 # 'Guatemala': 'GT',
                 # 'Guinea': 'GN',
                 # 'Guinea-bissau:': 'GW',
                 # 'Guyana': 'GY',
                 # 'Haiti': 'HT',
                 # 'Honduras': 'HN',
                 # 'Hungary': 'HU',
                 # 'India': 'IN',
                 # 'Indonesia': 'ID',
                 # 'Iran': 'IR',
                 # 'Iraq': 'IQ',
                 # 'Italy': 'IT',
                 # 'Jamaica': 'JM',
                 # 'Japan': 'JP',
                 # 'Jordan': 'JO',
                 # 'Kazakhstan': 'KZ',
                 # 'Kenya': 'KE',
                 # 'Kiribati': 'KI',
                 # 'Kuwait': 'KW',
                 # 'Kyrgyzstan': 'KG',
                 # 'Lebanon': 'LB',
                 # 'Lesotho': 'LS',
                 # 'Liberia': 'LR',
                 # 'Libya': 'LY',
                 # 'Madagascar': 'MG',
                 # 'Malawi': 'MW',
                 # 'Malaysia': 'MY',
                 # 'Maldives': 'MV',
                 # 'Mali': 'ML',
                 # 'Martinique': 'MQ',
                 # 'Mauritania': 'MR',
                 # 'Mauritius': 'MU',
                 # 'Mexico': 'MX',
                 # 'Mongolia': 'MN',
                 # 'Morocco': 'MA',
                 # 'Mozambique': 'MZ',
                 # 'Myanmar': 'MM',
                 # 'Namibia': 'NA',
                 # 'Nepal': 'NP',
                 # 'Netherlands': 'NL',
                 # 'New zealand': 'NZ',
                 # 'Nicaragua': 'NI',
                 # 'Niger': 'NE',
                 #'Nigeria': 'NG', pas bon
                 # 'Norway': 'NO',
                 # 'Oman': 'OM',
                 # 'Pakistan': 'PK',
                 # 'Palestine': 'PS',
                 # 'Panama': 'PA',
                 # 'Papua new guinea': 'PG',
                 # 'Paraguay': 'PY',
                 # 'Peru': 'PE',
                 # 'Philippines': 'PH',
                 # 'Poland': 'PL',
                 # 'Portugal': 'PT',
                 # 'Puerto rico': 'PR',
                 # 'Qatar': 'QA',
                 # 'Reunion': 'RE',
                 # 'Romania': 'RO',
                 # 'Russia': 'RU',
                 # 'Rwanda': 'RW',
                 # 'Samoa': 'WS',
                 # 'Sao tome and principe': 'ST',
                 # 'Saudi arabia': 'SA',
                 # 'Senegal': 'SN',
                 # 'Serbia': 'RS',
                 # 'Seychelles': 'SC',
                 # 'Sierra leone': 'SL',
                 # 'Singapore': 'SG',
                 # 'Slovakia': 'SK',
                 # 'Slovenia': 'SI',
                 # 'Solomon islands': 'SB',
                 # 'Somalia': 'SO',
                 # 'South africa': 'ZA',
                 # 'Spain': 'ES',
                 # 'Sri lanka': 'LK',
                 # 'Sudan': 'SD',
                 # 'Swaziland': 'SZ',
                 # 'Sweden': 'SE',
                 # 'Switzerland': 'CH',
                 # 'Syria': 'SY',
                 # 'Tajikistan': 'TJ',
                 # 'Tanzania': 'TZ',
                 # 'Thailand': 'TH',
                 # 'Togo': 'TG',
                 # 'Trinidad and tobago': 'TT',
                 # 'Tunisia': 'TN',
                 # 'Turkey': 'TR',
                 # 'Turkmenistan': 'TM',
                 # 'Uganda': 'UG',
                 # 'Ukraine': 'UA',
                 # 'United arab emirates': 'AE',
                 # 'United kingdom': 'GB', pas bon 
                 # 'United states': 'US', pas bon
                 'Uruguay': 'UY',
                 'Uzbekistan': 'UZ',
                 'Vanuatu': 'VU',
                 'Venezuela': 'VE',
                 'Viet nam': 'VN',
                 'Yemen': 'YE',
                 'Zambia': 'ZM',
                 'Zimbabwe': 'ZW'
                 }
    for pays in countries:
        # dataset, showcase = generate_dataset_and_showcase(pays, countries[pays])
        # dataset.update_from_yaml()

        # dataset.create_in_hdx(hxl_update=False)
        # # dataset.create_in_hdx()
        # dataset.add_tag('INDICATORS')
        # showcase.create_in_hdx()

        # showcase.add_dataset(dataset)
        updateTag(countries[pays])


if __name__ == '__main__':
    facade(main, hdx_site='prod', user_agent='HDXINTERNAL unhabitat scraper',
           project_config_yaml=join('config', 'project_configuration.yml'))
