API de Pet, com criação, consulta e remoção do pet(s).

Desenvolvedor

Luiz Almeida - All

Tecnologias

Django and Rest

Instalação

Use comand: pip install -r requirements.txt to install all tecnologies

Use comand: to

Rotas
ROOT usuários - "/usuario".
"/register" ["POST"] - Para cadastro de novos usuários.
"nome": "yourname",
"email": "yoruemail@domain.com",
"senha": "yourpassword"
"/login" ["POST"] - Para logar o usuário.
"email": "yoruemail@domain.com",
"senha": "yourpassword"
"/<int:<usuario_id>" ["GET"] - Para buscar as perguntas especificas de um usuário.
"/" ["DELETE"] - Deleção de usuários via Token.
"/" ["PATCH, PUT"] - Para atualização de usuários, autorização via Token.
ROOT temas - "/tema"
"/string:tema" ["GET"] - Retorna perguntas do tema escolhido.
"/" ["POST"] - Para criação de novas perguntas. Token requerido.
"/int:tema_id " ["PATCH, PUT"] - Para atualizar ou modificar as perguntas. Token Requerido.
"tema": "tema"\_update"
"/int:tema_id" ["DELETE"] - Para deletar as perguntas via id. Token requerido.
ROOT perguntas - "/pergunta"
"/" ["GET"] - Retorna todas as perguntas.
"/aleatoria?tema=tema" ["GET"] - Retorna pergunta aleatória do tema.
"/int:pergunta_id" ["GET"] - Retorna perguntas específicas pelo id.
"/" ["POST"] - Para criação de novas perguntas. Token requerido.
"pergunta": "question",
"resposta": "answer",
"tema": "theme",
"alternativa1": "alternative1",
"alternativa2": "alternative2",
"alternativa3": "alternative3"
"/int:pergunta_id" ["DELETE"] - Para deleção de perguntas pelo id. Token requerido.
"/int:pergunta_id" ["PATCH, PUT"] - Para modificação da pergunta pelo id. Token requerido.
