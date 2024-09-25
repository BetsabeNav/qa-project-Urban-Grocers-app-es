headers = {
   "Content-Type": "application/json"
}


#Diccionario con datos para crear un nuevo usuario
user_body = {
   "firstName": "Andrea",
   "phone": "+11234567890",
   "address": "123 Elm Street, Hilltop"
}


#Diccionario con datos para crear un nuevo kit
kit_body = {
      "name": "Mi conjunto",
      "card": {
          "id": 1,
          "name": "Para la situación"
      },
      "productsList": None,
      "id": 7,
      "productsCount": 0
  }