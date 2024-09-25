import data
import sender_stand_request
from data import kit_body

# Función para cambiar los valores en el parámetro "firstName"
def get_kit_body(kit_name):
  current_body = data.kit_body.copy()
  current_body["name"] = kit_name
  return current_body


## Función de prueba positiva
def positive_assert(kit_name):
  kit_body = get_kit_body(kit_name)
  user_response = sender_stand_request.post_new_client_kit(kit_body)


  assert user_response.status_code == 201
  assert user_response.json()["authToken"] != ""



# Función de prueba negativa
def negative_assert_symbol(kit_name):
  kit_body = get_kit_body(kit_name)
  response = sender_stand_request.post_new_client_kit(kit_body)


  assert response.status_code == 400
  assert response.json()["code"] == 400




# Función de prueba negativa- no pasan parametros
def negative_assert_no_name(kit_body):
  response = sender_stand_request.post_new_client_kit(kit_body)
  assert response.status_code == 400
  assert response.json()["code"] == 400


# Prueba 1: Creación de un nuevo kit:  El parámetro "name" contiene 1 caracter
def test_create_kit_1_letter_in_name():
  positive_assert("A")


# Prueba 2: Creación de un nuevo kit:  El parámetro "name" contiene 511 caracteres
def test_create_kit_511_letter_in_name():
  positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#Prueba 3: Eror- Creación de un nuevo kit:  El parámetro "name" contiene 0 caracteres
def test_create_kit_0_letter_in_name():
  negative_assert_symbol("")


# Prueba 4: Error- Creación de un nuevo kit:  El parámetro "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name():
  negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5: Creación de un nuevo kit:  El parámetro "name" contiene caracteres especiales
def test_create_kit_special_characters_in_name():
  positive_assert("№%@",)


# Prueba 6: Creación de un nuevo kit:  El parámetro "name" contiene espacios
def test_create_kit_space_in_name():
  positive_assert(" A Aaa ")


# Prueba 7: Creación de un nuevo kit:  El parámetro "name" contiene números
def test_create_kit_numers_in_name():
  positive_assert("123")


# Prueba 8: Error- La solicitud no contiene el parámetro "Name"
def test_create_kit_no_name_get_error_response():
  kit_body = data.kit_body.copy()
  kit_body.pop("name")
  negative_assert_no_name(kit_body)


# Prueba 9: Error- El tipo del parámetro "name" es un número
def test_create_kit_number_type_name_get_error_response():
  ki_body = get_kit_body(12)
  response = sender_stand_request.post_new_client_kit(kit_body)
  assert response.status_code == 400
