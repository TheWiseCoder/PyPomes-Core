from typing import Final

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status

# TODO: complete the descriptions
_HTTP_STATUSES: Final[dict] = {
    # Informational responses
    100: {
        "name": "CONTINUE",
        "en": ("Interim response, indicating that the client should "
               "continue the request or ignore the response if the request is already finished."),
        "pt": ("Resposta provisória, indicando que o cliente deve continuar "
               "a solicitação ou ignorar a resposta se a solicitação já estiver concluída.")
    },
    101: {
        "name": "SWITCHING PROTOCOLS",
        "en": ("Sent in response to an upgrade request header from the client, "
               "indicating the protocol the server is switching to."),
        "pt": ("Enviado em resposta a um cabeçalho de solicitação Upgrade do cliente, "
               "indicando o protocolo para o qual o servidor está mudando.")
    },
    102: {
        "name": "PROCESSING",
        "en": ("Indicates that the server has received and is processing the request, "
               "but no response is available yet."),
        "pt": ("Indica que o servidor recebeu e está processando a requisição, "
               "mas nenhuma resposta está disponível ainda.")
    },
    103: {
        "name": "EARLY HINTS",
        "en": ("Used with the 'Link' header, letting the user agent start "
               "preloading resources while the server prepares a response."),
        "pt": ("Usado com o cabeçalho 'Link', permitindo que o agente do usuário "
               "inicie o pré-carregamento de recursos enquanto o servidor prepara uma resposta.")
    },
    # Successful responses
    200: {
        "name": "OK",
        "en": "The request succeeded.",
        "pt": "A solicitação foi bem-sucedida."
    },
    201: {
        "name": "CREATED",
        "en": "The request succeeded, and a new resource was created as a result.",
        "pt": "A requisição foi bem sucedida e um novo recurso foi criado como resultado."
    },
    202: {
        "name": "ACCEPTED",
        "en": "The request has been received but not yet acted upon.",
        "pt": "A solicitação foi recebida, mas ainda não foi atendida."
    },
    203: {
        "name": "NON AUTHORITATIVE INFORMATION",
        "en": ("The returned metadata is not exactly the same as is available from the origin server, "
               "but is collected from a local or a third-party copy."),
        "pt": ("Os metadados retornados não são exatamente os mesmos que estão disponíveis "
               "no servidor de origem, mas são coletados de uma cópia local ou de terceiros.")
    },
    204: {
        "name": "NO CONTENT",
        "en": "There is no content to send for this request, but the headers may be useful.",
        "pt": "Não há conteúdo para enviar para esta solicitação, mas os cabeçalhos podem ser úteis."
    },
    205: {
        "name": "RESET CONTENT",
        "en": "Tells the user agent to reset the document which sent this request.",
        "pt": "Diz ao agente do usuário para redefinir o documento que enviou esta solicitação."
    },
    206: {
        "name": "PARTIAL CONTENT",
        "en": "used when the 'Range' header is sent from the client to request only part of a resource.",
        "pt": "Usado quando o cabeçalho 'Range' é enviado do cliente para solicitar apenas parte de um recurso."
    },
    207: {
        "name": "MULTI-STATUS",
        "en": ("Conveys information about multiple resources, "
               "for situations where multiple status codes might be appropriate."),
        "pt": ("Transmite informações sobre vários recursos, "
               "para situações em que vários códigos de status podem ser apropriados.")
    },
    208: {
        "name": "ALREADY REPORTED",
        "en": "Used inside a '<dav:propstat>' response element to avoid "
              "repeatedly enumerating the internal members of multiple bindings to the same collection.",
        "pt": ("Usado dentro de um elemento de resposta '<dav:propstat>' para evitar "
               "enumerar repetidamente os membros internos de várias ligações para a mesma coleção.")
    },
    226: {
        "name": "IM USED",
        "en": ("The server has fulfilled a 'GET' request for the resource, and the response is a "
               "representation of the result of one or more instance-manipulations applied to the current instance."),
        "pt": ("O servidor atendeu a uma solicitação 'GET' para o recurso e a resposta é uma representação "
               "do resultado de uma ou mais manipulações de instância aplicadas à instância atual.")
    },
    # Redirection messages
    300: {
        "name": "MULTIPLE CHOICES",
        "en": ("The request has more than one possible response. "
               "The user agent or user should choose one of them."),
        "pt": ("A solicitação tem mais de uma resposta possível. "
               "O agente do usuário ou usuário deve escolher uma delas.")
    },
    301: {
        "name": "MOVED PERMANENTLY",
        "en": "The URL of the requested resource has been changed permanently. The new URL is given in the response.",
        "pt": "A URL do recurso solicitado foi permanentemente alterada. A nova URL é fornecida na resposta."
    },
    302: {
        "name": "FOUND",
        "en": ("The URI of requested resource has been changed temporarily. "
               "Further changes in the URI might be made in the future. "),
        "pt": ("A URI do recurso solicitado foi alterado temporariamente. "
               "Outras alterações na URI podem ser feitas no futuro.")
    },
    303: {
        "name": "SEE OTHER",
        "en": ("The server sent this response to direct the client to get "
                "the requested resource at another URI with a 'GET' request."),
        "pt": ("O servidor enviou esta resposta para direcionar o cliente "
               "a obter o recurso solicitado em outro URI com uma solicitação 'GET'.")
    },
    304: {
        "name": "NOT MODIFIED",
        "en": ("Tells the client that the response has not been modified, "
               "so the client can continue to use the same cached version of the response."),
        "pt": ("Informa ao cliente que a resposta não foi modificada; "
               "portanto, o cliente pode continuar a usar a mesma versão em cache da resposta.")
    },
    305: {
        "name": "USE PROXY",
        "en": ("Indicates that a requested response must be accessed by a proxy. "
               "It has been deprecated due to security concerns regarding in-band configuration of a proxy."),
        "pt": ("Indica que uma resposta solicitada deve ser acessada por um proxy. "
               "Foi descontinuado devido a questões de segurança em relação à configuração em banda de um proxy.")
    },
    307: {
        "name": "TEMPORARY REDIRECT",
        "en": ("The server sends this response to direct the client to get the "
               "requested resource at another URI, with the same method that was used in the prior request."),
        "pt": ("O servidor envia esta resposta para direcionar o cliente a obter "
               "o recurso solicitado em outra URI, com o mesmo método usado na solicitação anterior.")
    },
    308: {
        "name": "PERMANENT REDIRECT",
        "en": ("Indicates that the resource is now permanently located at another URI, "
               "specified by the 'Location:' HTTP Response header."),
        "pt": ("Indica que o recurso agora está permanentemente localizado em outra URI, "
               "especificada pelo cabeçalho de resposta HTTP 'Location:'.")
    },
    # Client error responses
    400: {
        "name": "BAD REQUEST",
        "en": ("The server cannot process the request due to something that is perceived to be a client error "
               "(e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."),
        "pt": ("O servidor não pode processar a solicitação devido a algo que é percebido como um erro do cliente "
               "(e.g., solicitação malformada, roteamento ou enquadramento de mensagem de solicitação inválida).")
    },
    401: {
        "name": "UNAUTHORIZED",
        "en": ("Semantically, this response means 'unauthenticated'. "
               "The client must authenticate itself to get the requested response."),
        "pt": ("Semanticamente, essa resposta significa 'unauthenticated'. "
               "O cliente deve se autenticar para obter a resposta solicitada.")
    },
    402: {
        "name": "PAYMENT REQUIRED",
        "en": "This response code is reserved for future use; no standard exists.",
        "pt": "Este código de resposta está reservado para uso futuro; não existe convenção padrão."
    },
    403: {
        "name": "FORBIDDEN",
        "en": ("The client does not have access rights to the content. "
               "Unlike '401 Unauthorized', the client's identity is known to the server."),
        "pt": ("O cliente não tem direitos de acesso ao conteúdo. "
               "Ao contrário do '401 Unauthorized', a identidade do cliente é conhecida pelo servidor.")
    },
    404: {
        "name": "NOT FOUND",
        "en": ("The server cannot find the requested resource. Either the URL is not recognized, the resource "
               "does not exist, or the server is hiding the existence of a resource from an unauthorized client."),
        "pt": ("O servidor não pode encontrar o recurso solicitado. A URL não é reconhecida, o recurso não existe, "
               "ou o servidor está ocultando a existência de um recurso de um cliente não autorizado.")
    },
    405: {
        "name": "METHOD NOT ALLOWED",
        "en": "The request method is known by the server but is not supported by the target resource. "
              "For example, an API may not allow calling 'DELETE' to remove a resource.",
        "pt": "O método de solicitação é conhecido pelo servidor, mas não é suportado pelo recurso de destino. "
              "Por exemplo, uma API pode não permitir chamar 'DELETE' para remover um recurso."
    },
    406: {
        "name": "NOT ACCEPTABLE",
        "en": ("After performing server-driven content negotiation, the server "
               "does not find any content that conforms to the criteria given by the user agent."),
        "pt": ("Após realizar negociação de conteúdo, o servidor não encontra conteúdo "
               "que esteja em conformidade com os critérios fornecidos pelo o agente do usuário.")
    },
    407: {
        "name": "PROXY AUTHENTICATION REQUIRED",
        "en": "Semelhante a '401 Unauthorized', mas a autenticação precisa ser feita por um proxy.",
        "pt": "This is similar to '401 Unauthorized' but the authentication needs to be done by a proxy."
    },
    408: {
        "name": "REQUEST TIMEOUT",
        "en": ("This response is sent on an idle or unused connection "
               "by the server, whenever it feels the need to shut it down."),
        "pt": ("Esta resposta é enviada pelo servidor em uma conexão ociosa ou "
               "não utilizada, sempre que seu desligamento se fizer necessário.")
    },
    409: {
        "name": "CONFLICT",
        "en": "This response is sent when a request conflicts with the current state of the server.",
        "pt": "Esta resposta é enviada quando uma requisição conflitar com o estado atual do servidor."
    },
    410: {
        "name": "GONE",
        "en": ("This response is sent when the requested content "
               "has been permanently deleted from server, with no forwarding address."),
        "pt": ("Esta resposta é enviada quando o conteúdo solicitado "
               "foi excluído permanentemente do servidor, sem endereço de encaminhamento.")
    },
    411: {
        "name": "LENGTH REQUIRED",
        "en": ("The server rejected the request because the 'Content-Length' "
               "header field is not defined, and the server requires it."),
        "pt": ("O servidor rejeitou a solicitação porque o campo de cabeçalho "
               "'Content-Length' não está definido, e o servidor o exige.")
    },
    412: {
        "name": "PRECONDITION FAILED",
        "en": "The client has indicated preconditions in its headers which the server does not meet.",
        "pt": "O cliente indicou nos seus cabeçalhos pré-condições que o servidor não atende."
    },
    413: {
        "name": "PAYLOAD TOO LARGE",
        "en": ("The request entity is larger than limits defined by server. "
               "The server might close the connection or return a 'Retry-After' header field."),
        "pt": ("A entidade requisição é maior do que os limites definidos pelo servidor. "
               "O servidor pode fechar a conexão ou retornar um campo de cabeçalho 'Retry-After'.")
    },
    414: {
        "name": "URI TOO LONG",
        "en": "The URI requested by the client is longer than the server is willing to interpret.",
        "pt": "A URI solicitada pelo cliente é mais longa do que o servidor está disposto a interpretar."
    },
    415: {
        "name": "UNSUPPORTED MEDIA TYPE",
        "en": ("The media format of the requested data is not supported by the server, "
               "so the server is rejecting the request."),
        "pt": ("O formato de mídia dos dados requisitados não é suportado pelo servidor, "
               "que portanto está rejeitando a requisição.")
    },
    416: {
        "name": "RANGE NOT SATISFIABLE",
        "en": "",
        "pt": ""
    },
    417: {
        "name": "EXPECTATION FAILED",
        "en": "",
        "pt": ""
    },
    418: {
        "name": "I'M A TEAPOT",
        "en": "The server refuses the attempt to brew coffee with a teapot. "
              "This was an April Fools joke from 1998, kept in the official standard by popular demand.",
        "pt": "O servidor recusa a tentativa de coar café num bule de chá. "
              "Essa foi uma brincadeira de 1o. de Abril em 1998, mantida no padrão oficial por clamor popular."
    },
    421: {
        "name": "MISDIRECTED REQUEST",
        "en": "",
        "pt": ""
    },
    422: {
        "name": "UNPROCESSABLE CONTENT",
        "en": "",
        "pt": ""
    },
    423: {
        "name": "LOCKED",
        "en": "",
        "pt": ""
    },
    424: {
        "name": "FAILED DEPENDENCY",
        "en": "",
        "pt": ""
    },
    425: {
        "name": "TOO EARLY",
        "en": "",
        "pt": ""
    },
    426: {
        "name": "UPGRADE REQUIRED",
        "en": "",
        "pt": ""
    },
    428: {
        "name": "PRECONDITION REQUIRED",
        "en": "",
        "pt": ""
    },
    429: {
        "name": "TOO MANY REQUESTS",
        "en": "",
        "pt": ""
    },
    431: {
        "name": "REQUEST HEADER FIELDS TOO LARGE",
        "en": "",
        "pt": ""
    },
    451: {
        "name": "UNAVAILABLE FOR LEGAL REASONS",
        "en": "",
        "pt": ""
    },
    # Server error responses
    500: {
        "name": "INTERNAL SERVER ERROR",
        "en": "The server has encountered a situation it does not know how to handle.",
        "pt": "O servidor encontrou uma situação com a qual não sabe lidar."
    },
    501: {
        "name": "NOT IMPLEMENTED",
        "en": "The request method is not supported by the server and cannot be handled. "
              "The only methods that servers are required to support are 'GET' and 'HEAD'.",
        "pt": "O método da requisição não é suportado pelo servidor e não pode ser manipulado. "
              "Os únicos métodos que servidores são obrigados a suportar são 'GET' e 'HEAD'."
    },
    502: {
        "name": "BAD GATEWAY",
        "en": ("The server, while working as a gateway to get a response "
               "needed to handle the request, got an invalid response."),
        "pt": ("O servidor, enquanto trabalhava como um gateway para obter uma resposta "
               "necessária para lidar com a solicitação, obteve uma resposta inválida.")
    },
    503: {
        "name": "SERVICE UNAVAILABLE",
        "en": ("The server is not ready to handle the request. "
               "Common causes are a server that is down for maintenance or is overloaded."),
        "pt": ("O servidor não está pronto para manipular a requisição. "
               "Causas comuns são um servidor em manutenção ou sobrecarregado.")
    },
    504: {
        "name": "GATEWAY TIMEOUT",
        "en": "The server is acting as a gateway and cannot get a response in time.",
        "pt": "O servidor está atuando como um gateway e não consegue obter uma resposta a tempo."
    },
    505: {
        "name": "HTTP VERSION NOT SUPPORTED",
        "en": "The HTTP version used in the request is not supported by the server.",
        "pt": "A versão HTTP usada na requisição não é suportada pelo servidor."
    },
    506: {
        "name": "VARIANT ALSO NEGOTIATES",
        "en": ("The chosen variant resource is configured to engage in transparent content negotiation itself, "
               "and is therefore not a proper end point in the negotiation process."),
        "pt": ("O recurso variante escolhido está configurado para se envolver em negociação "
               "de conteúdo transparente, e portanto, não é um 'endpoint' adequado no processo de negociação.")
    },
    507: {
        "name": "INSUFFICIENT STORAGE",
        "en": ("The method could not be performed on the resource, because the server "
               "is unable to store the representation needed to successfully complete the request."),
        "pt": ("O método não pôde ser executado no recurso porque o servidor "
               "não pode armazenar a representação necessária para concluir a solicitação com êxito.")
    },
    508: {
        "name": "LOOP DETECTED",
        "en": "The server detected an infinite loop while processing the request.",
        "pt": "O servidor detectou um loop infinito ao processar a solicitação."
    },
    510: {
        "name": "NOT EXTENDED",
        "en": "Further extensions to the request are required for the server to fulfill it.",
        "pt": "Extensões adicionais à solicitação são necessárias para que o servidor a atenda."
    },
    511: {
        "name": "NETWORK AUTHENTICATION REQUIRED",
        "en": "Indicates that the client needs to authenticate to gain network access.",
        "pt": "Indica que o cliente precisa se autenticar para obter acesso à rede."
    }
}
