Description

API de Pet, com criação, consulta e remoção do pet(s).

Dev

Luiz Almeida - All

Tecnologias

Black, Django, and Django Rest Framework

Instalação

Use command python -m venv .venv to create a venv.

Use command source .venv/bin/activate to active de venv.

Use command pip install -r requirements.txt to install all tecnologies.

Use command python manage.py migrate to create de tables.

Use command python manage.py runserver to start the server localy.

Rotas

ROOT - "/animals".
"/" ["POST"] - To create pet registration.

```
Body request:
{
    "name": "PetName",
    "age": PetAge(Integer),
    "weight": PetWeight(Integer),
    "sex": "PetSex",
    "group": {
        "name": "Petnamegroup",
        "scientific_name": "PetScientificName"
    },
    "characteristic_set": [
        {
            "characteristic": "PetCharacteristic"
        },
        {
            "characteristic": "PetCharacteristic2"
        }
    ]
}

Response:
{
    "id": PetID,
    "name": "PetName",
    "age": PetAge (Integer),
    "weight": PetWeight (Integer),
    "sex": "PetSex",
    "group": {
        "id": groupID (Integer),
        "name": "PetNameGroup",
        "scientific_name": "PetScientificName"
    },
    "characteristic_set": [
        {
            "id": PetCharacteristic (Integer),
            "characteristic": "PetCharacteristic"
        },
        {
            "id": PetCharacteristic2 (Integer),
            "characteristic": "PetCharacteristic2"
        }
    ]
}

Status: 201_CREATED
```

"/" ["GET"] - To get a all registered Pets informations.

```
Response:
[
    {
        "id": 1,
        "name": "Pet1Name",
        "age": Pet1Age,
        "weight": Pet1Weight,
        "sex": "Pet1Sex",
        "group": {
            "id": 1,
            "name": "Pet1namegroup",
            "scientific_name": "Pet1ScientificName"
        },
        "characteristic_set": [
            {
                "id": Pet1CharacteristicID (Integer),
                "characteristic": "Pet1Characteristic"
            },
        ]
    },
    {
        "id": 2,
        "name": "Pet2Name",
        "age": Pet2Age,
        "weight": Pet2Weight,
        "sex": "Pet2Sex",
        "group": {
            "id": 1,
            "name": "Pet2namegroup",
            "scientific_name": "Pet2ScientificName"
        },
        "characteristic_set": [
            {
                "id": Pet2CharacteristicID (Integer),
                "characteristic": "Pet2Characteristic"
            },
        ]
    }, ...
]

Status: 200 OK
```

"/<int:<animal_id>" ["GET"] - To get a specific register Pet informations.

```
Response:
{
    "id": animal_id,
    "name": "PetName",
    "age": PetAge (Integer),
    "weight": PetWeight (Integer),
    "sex": "PetSex",
    "group": {
        "id": groupID (Integer),
        "name": "PetNameGroup",
        "scientific_name": "PetScientificName"
    },
    "characteristic_set": [
        {
            "id": PetCharacteristicID (Integer),
            "characteristic": "PetCharacteristic"
        },
    ]
}

Status: 200 OK

If Pet registration doesn't exist:

Status: 404 NOT FOUND
```

"/<int:<animal_id>" ["DELETE"] - Delete Pet registration.

```
Status: 204 NO CONTENT

If Pet registration doesn't exist:

Status: 404 NOT FOUND
```
