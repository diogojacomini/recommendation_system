# Changelog

Todas as alterações notáveis deste projeto serão documentadas neste arquivo.

## [0.0.2] - 2025-02-23

### adding
- **Nova Rota para Usuários**:
  - **Rota POST `/usuarios/`**: Agora é possível cadastrar novos usuários enviando um objeto `Usuario` no corpo da requisição. O novo usuário será salvo com um ID único gerado automaticamente.
  - **Rota GET `/usuarios/`**: Esta rota retorna a lista de todos os usuários cadastrados.


## [0.0.1] - 2025-02-22

### adding
- Primeira versão da API de Recomendação de Produtos com FastAPI.
