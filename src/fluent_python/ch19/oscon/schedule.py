# -*- coding: UTF-8 -*-

import warnings

import osconfeed
import shelve

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)


def main():
    with shelve.open(DB_NAME) as the_db:
        if CONFERENCE not in the_db:
            load_db(the_db)
        speaker = the_db['speaker.3471']
        print(speaker.name)


if __name__ == '__main__':
    main()
