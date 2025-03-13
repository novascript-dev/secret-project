Nova Fernandes - Kaya Doc


## Responsividade:

Todo o site está responsivo para funcionar nos **principais tamanhos de tela** (sm, md, lg, xl), salvo exceções de canto (telas muito pequenas ou telas muito grandes) que podem conter bugs visuais.


## Tecnologias Utilizadas
- `django` com `tailwind` e `sqlite` para construção geral das funcionalidades.
- `django-tailwind` para melhor configuração do ambiente de desenvolvimento e build com watch de alterações e +
- `docker` com `supervisord` para containerizar o projeto e executar o ambiente de desenvolvimento com o `django-tailwind start` no fundo, além de realizar `migrate` automático e o `import_mock_data` (script criado para popular o banco com dados falsos antes de rodar)

## Como rodar o projeto:

**Clone este projeto**, **acesse a pasta onde se encontra este README** e **execute**:

```
$ sudo docker build -t nova-assessment .
```

Para poder buildar o projeto completo.

Agora, vamos simplesmente executá-lo:

```
$ sudo docker run -p 8000:8000 -v $(pwd):/app nova-assessment
```


_**Aguarde alguns segundos**, pois o terminal exibirá logs do tailwind, do runserver, do migrate e do import mock data_


Pronto! **Agora basta acessar no navegador a seguinte URL**:

http://0.0.0.0:8000/doctors/

---
