#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
SCRAPERNAME:
------------

Reads ScraperName JSON and creates datasets.

"""

import logging
import requests
import os
import csv
import json
from hdx.data.dataset import Dataset
from hdx.data.resource import Resource
from hdx.data.hdxobject import HDXError
from hdx.data.showcase import Showcase
# from hdx.utilities.location import Location
from slugify import slugify
from hdx.hdx_configuration import Configuration

logger = logging.getLogger(__name__)

"""
This function download the csv file corresponding to the given country iso 2
code in parameters
"""


# def test(iso2):
#     url = Configuration.read()['base_url'] + "&code=" + iso2

#     with requests.Session() as s:
#         download = s.get(url)

#         decoded_content = download.content.decode('utf-8')
#         with open('data/testDownload-%s' % iso2 + '.csv', 'w') as f:
#             f.write(decoded_content)
        # cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        # my_list = list(cr)s
        # for row in my_list:
        #     print(row)


def getData(countryISO2):
    url = Configuration.read()['base_url'] + "&code=" + countryISO2
    response = requests.get(url)
    headers = ['category', 'indicator', 'indicator_friendly', 'type_data',
               'latitude', 'longitude', 'region_id', 'country_id', 'name',
               'year', 'value']
    hxl = ['#meta+category', '#indicator+name', '#indicator+description',
           '#indicator+type', '#geo+lat', '#geo+lon', '#region+code',
           '#country+code+v_iso2', '#country+name', '#date+year', '#indicator+value']

    if response.status_code != 200:
        print(":(")
    else:
        try:
            with open('data/%s' % countryISO2 + '.csv', 'w') as f:
                f.write(response.text)
        except Exception as e:
            raise e

    with open('data/indicator_data_%s' % countryISO2 + '.csv', 'w') as hxl_tags:
        writer = csv.writer(hxl_tags, delimiter=',')
        writer.writerow(headers)
        writer.writerow(hxl)
        data = open('data/%s' % countryISO2 + '.csv', 'r')
        with data:
            reader = csv.reader(data)
            next(reader)
            for r in reader:
                writer.writerow(r)


def getCountryISO3Code(iso2):
    iso3 = 0
    with open('data/countries.json', 'r') as countries:
        data = json.load(countries)
        for d in data:
            if d['iso2'] == iso2.upper():
                iso3 = d['iso3']
    return iso3


def generate_dataset_and_showcase(countryName, countryISO2):
    title = '%s - Demographic, Health, Education and Transport indicators' % countryName
    logger.info('Creating dataset: %s' % title)
    name = 'unhabitat-%s-indicators' % countryISO2
    slugified_name = slugify(name).lower()
    dataset = Dataset({
        'name': slugified_name,
        'title': title,
    })
    # dataset.set_dataset_date(date, dataset_end_date=)
    dataset.set_dataset_year_range(1950, 2050)
    dataset.set_expected_update_frequency('Every year')
    dataset.set_subnational(1)
    dataset.add_country_location(getCountryISO3Code(countryISO2))
    dataset.add_tags(['EDUCATION', 'POPULATION', 'HEALTH', 'TRANSPORT', 'HXL'])

    if os.path.isfile('data/indicator_data_' + countryISO2 + '.csv'):
        resource = Resource()
        resource['name'] = 'Indicators_data_%s' % countryISO2
        resource['description'] = '%s - Demographic, Health, Education and Transport indicators' % countryName
        resource['format'] = 'csv'
        resource.set_file_to_upload('data/indicator_data_' +
                                    countryISO2 + '.csv')
    resource.check_required_fields(['group', 'package_id'])
    dataset.add_update_resource(resource)

    showcase_name = slugify('unhabitat-%s' % countryName + ' indacators-data').lower()
    showcase = Showcase({
        'name': showcase_name,
        'title': 'Explore %s' % countryName + ' indicators',
        'notes': 'Explore %s' % countryName + ' indicators',
        'url': 'http://urbandata.unhabitat.org/data-country/?countries=%s' % countryISO2 +'&indicators=total_length_road,rural_population,urban_population_countries,urban_slum_population_countries,population,income_gini_coefficient_countries',
        'image_url': 'https://centre.humdata.org/wp-content/uploads/2018/09/unhabitat-showcase.png'})
    showcase.add_tags(['EDUCATION', 'POPULATION', 'HEALTH', 'TRANSPORT'])

    return dataset, showcase
