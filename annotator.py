import requests
import os
import io
import traceback


try:
    TADA_HOST = os.environ['TADA_HOST']
except Exception as e:
    TADA_HOST = ''


def annotate_subject(source_dir, subject_col_id, top_k=3, logger=None):
    """
    :param source_dir: the directory of the source file
    :param subject_col_id: the index of the subject column
    :param top_k: the number of suggested classes to return
    :return: list of string (classes)
    """



    # # TEST
    # url = "https://api.tada.linkeddata.es/subject"
    #
    # payload = {'col_id': '1',
    #            'alpha': '0.9',
    #            'k': '1'}
    # files = [
    #     ('source', (
    #     'aaawrestlers.csv', open('/Users/aalobaid/workspaces/Pyworkspace/tada-gam/local_data/aaawrestlers.csv', 'rb'),
    #     'text/csv'))
    # ]
    # headers = {}
    #
    # response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #
    # print(response.text)
    # # END TEST


    #
    #
    #
    # url = "https://api.tada.linkeddata.es/subject"
    # #
    # payload = {'col_id': '1',
    #            'alpha': '0.9',
    #            'k': '1'}
    # data = payload
    # files = [
    #     ('source', (
    #     'aaawrestlers.csv', open('/Users/aalobaid/workspaces/Pyworkspace/tada-gam/local_data/aaawrestlers.csv', 'rb'),
    #     'text/csv'))
    # ]
    # headers = {}
    #
    # # response = requests.request("POST", url, headers=headers, data=payload, files=files)
    # #
    # # print(response.text)
    #
    #
    #
    #





    data = {
        'col_id': subject_col_id,
        'alpha': 0.9,
        'k': top_k
    }
    # print("data: ")
    # print(data)
    # data['source'] = (source_dir.split(os.sep)[-1], open(source_dir), 'text/plain')
    # f = open(source_dir)
    # file_content = f.read()
    # data['source'] = (io.BytesIO(file_content), source_dir.split(os.sep)[-1])
    # response = requests.post(TADA_HOST+'/subject', data=data)
    # headers = {'Content-type': 'multipart/form-data'}
    # response = requests.post(TADA_HOST+'/subject', data=data, headers=headers)
    # files = {
    #     'source': (source_dir.split(os.sep)[-1], open(source_dir), 'text/plain')
    # }

    # files = [
    #     ('source', (
    #     'aaawrestlers.csv',
    #     open('/Users/aalobaid/workspaces/Pyworkspace/tada-gam/local_data/aaawrestlers.csv', 'rb'),
    #     'text/csv'))
    # ]
    #
    #
    # print("source dir file: ")
    # print(source_dir.split(os.sep)[-1])
    # print("dir: "+source_dir)
    #
    # files = [
    #     ('source', (
    #         source_dir.split(os.sep)[-1],
    #         open(source_dir, 'rb'),
    #     'text/csv'))
    # ]
    #
    files = [
        ('source', (
            source_dir.split(os.sep)[-1],
            open(source_dir),
            'text/plain'))
    ]
    # # response = requests.post(TADA_HOST+'/subject', data=data, files=files)
    # print("url: "+TADA_HOST+'/subject')
    # response = requests.request("POST", TADA_HOST+'/subject', data=data, files=files)
    # print("url: <%s>" % url)
    # print("host: <%s>" % (TADA_HOST+'/subject'))
    response = requests.request("POST", TADA_HOST+'/subject', data=data, files=files)

    if response.status_code == 200:
        print("-- entities: ")
        print(response.json())
        logger.debug("annotate_subject> entities ")
        logger.debug(str(response.json()))
        entities = response.json()['entities']
    else:
        print("-- ERROR: status code: "+str(response.status_code))
        entities = []
        # print("response: ")
        # print(response.content)
        # print(response.status_code)
        try:
            print(response.json())
            logger.debug(str(response.json()))
        except:
            print("No JSON")
            logger.debug("annotate_subject> No JSON")
            traceback.print_exc()
    return entities


def annotate_property(source_dir, subject_col_id, top_k=3, logger=None):
    """
    :param source_dir: the directory of the source file
    :param subject_col_id: the index of the subject column
    :param top_k: the number of suggested classes to return
    :return: list of string (classes)
    """
    data = {
        'subject_col_id': subject_col_id,
        'k': top_k,
    }
    # data['source'] = (source_dir.split(os.sep)[-1], open(source_dir), 'text/plain')
    # f = open(source_dir)
    # file_content = f.read()
    # data['source'] = (io.BytesIO(file_content), source_dir.split(os.sep)[-1])
    # response = requests.post(TADA_HOST+'/subject', data=data)
    # headers = {'Content-type': 'multipart/form-data'}
    # response = requests.post(TADA_HOST+'/subject', data=data, headers=headers)
    files = {
        'source': (source_dir.split(os.sep)[-1], open(source_dir), 'text/plain')
    }
    response = requests.post(TADA_HOST+'/property', data=data, files=files)
    if response.status_code == 200:
        print("properties: ")
        print(response.json())
        logger.debug("annotate_property> properties ")
        logger.debug(str(response.json()))
        pairs = response.json()['cols_properties']
    else:
        pairs = []
        try:
            print(response.json())
            logger.debug(str(response.json()))
        except:
            print("No JSON")
            logger.debug("annotate_property> No JSON")
            traceback.print_exc()
    return pairs

