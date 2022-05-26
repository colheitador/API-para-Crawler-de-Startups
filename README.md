# API-para-Crawler-de-Startups
As informações desta aplicação são baseadas no website StartupBase.

(o webscraping foi possível nas páginas de 9633 startups /9725 links não-nulos = 99,05% )

Para executar a aplicação, abra o terminal e vá ao diretório onde está o arquivo "main.py". Execute "uvicorn main:app --reload", espere o carregamento e vá até o endereço IP mostrado pelo terminal. Acrescente "/docs" ao final do endereço. 

Ex: http://127.0.0.1:8000/docs

Para usar a função "Pesquisar Por Cidade Ou Sigla Do Estado", clique em "Try it out" e digite uma palavra ou sequencia de caracteres presentes no nome da cidade ou na sigla do estado da empresa. Ex: se quisessemos pesquisar por startups em Salvador, poderíamos escrever "Salvador", " - BA", "Salvador - BA", "Salv", "lvador", etc;
Para usar a função "Pesquisar Por Descrição", digite uma palavra ou sequência de caracteres presentes na descrição da empresa;
Para usar a função "Pesquisar Por Nome", digite uma palavra ou sequencia de caracteres presentes no nome empresa.

Caso queira atualizar a base de dados, instale as dependências necessárias, certifique-se de ter o postgresql já configurado, abra o arquivo "scraper_e_crawler_startups.ipynb", leia os comentários para entender o funcionamento do programa e execute apenas as células necessárias.

__________________________________________________________________________

Quanto ao chromedriver:

O chromedriver deste repositório é para a versão 101 do google chrome. Para baixar o chromedriver de outra versão: https://chromedriver.chromium.org/downloads

__________________________________________________________________________

Quanto ao postgresql:

Também certifique-se de ter o postgresql instalado e configurado. Website para download: https://www.postgresql.org/download/

Uma das coisas que costuma ser necessária é abrir o arquivo pg_hba.conf e escrever 0.0.0.0/0 no lugar do endereço de ipv4

Troque isto:

IPv4 local connections:
host all all 127.0.0.1/32 scram-sha-256

Por isto:

IPv4 local connections:
host all all 0.0.0.0/0 scram-sha-256
