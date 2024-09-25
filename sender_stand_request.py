import configuration
import requests
import data


def get_docs():
  return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def post_new_user(body):
  return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                       json=body,
                       headers=data.headers)


def post_new_client_kit(products_ids):
  return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                       json=products_ids,
                       headers=data.headers)