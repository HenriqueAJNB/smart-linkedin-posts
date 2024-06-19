# Smart LinkedIn Posts

## Documentação funcional

Este projeto é um gerador de posts para LinkedIn utilizando IA generativa. A aplicação usa o modelo
OpenAI GPT-3.5-turbo para capturar a forma e tom de escrita baseado no histórido de posts e gerar, 
a partir de um dado tema, um novo posts utilizando o mesmo tom e linguajar dos posts anteriores.

O objetivo maior é escalar o número de seguidores usando postagens geradas com inteligência
artificial, porém com tom o mais próximo possível do autor. 

## Estrutura do projeto

- `data/shares.csv`: arquivo CSV com o histórico de posts do LinkedIn.
O arquivo deve ser baixado seguindo as [instruções da documentação oficial do LinkedIn](https://www.linkedin.com/help/linkedin/answer/a1339364/downloading-your-account-data)
- `smart_linkedin_posts/app.py`: script único do projeto
- `.env`: armazena a chave da API OpenAI no formato `OPENAI_API_KEY=...` não exposto por questões de segurança
- `pyproject.toml` e `poetry.lock`: arquivos de metadados do projeto e dependências.

## Requisitos técnicos obrigatórios
- Python 3.12

## Configuração inicial

1. Instalar `poetry`: `pip install poetry==1.7.0`
2. Instalar dependências: `poetry install`
3. Ativar ambiente virtual: `poetry shell`

## Disparo
- Execute a aplicação com `python smart_linkedin_posts/app.py` após ter feito a configuração inicial.
- A aplicação perguntara o tema para gerar o post
- O post será gerado na tela do terminal

## Custo associados ao projeto

Para maiores informações, consulte a [página de preços da OpenAI](https://openai.com/api/pricing/)
### GPT-3.5-turbo
- $0.50/1M tokens na entrada
- $1.50/1M tokens na saída
### Emmbeddings
- $0.10/1M tokens processados