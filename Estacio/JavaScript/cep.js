function consultarCEP() {
              
    var cep = document.getElementById("cep").value;

    var conexao = new XMLHttpRequest();

    var url = "http://cep.la/"+cep;

    conexao.open("GET", url, true);
    conexao.setRequestHeader("Accept", "application/json");

    conexao.onreadystatechange = function () {
        if (conexao.readyState == 3) {
            //console.log('Carregando o Conteúdo');
        }
        
        if (conexao.readyState == 4) {
           //console.log('CEP: ' + conexao.responseText);

           var jsonResponse = JSON.parse(conexao.responseText);

           document.getElementById("Resultado").innerHTML = 'CEP: ' + jsonResponse.cep + '<br>UF: ' + jsonResponse.uf + '<br>Cidade: ' 
           + jsonResponse.cidade + '<br>Bairro: ' + jsonResponse.bairro + '<br>Logradouro: ' + jsonResponse.logradouro;                

           //console.log(jsonResponse);  
        }
    }
    conexao.send(null);
} ;