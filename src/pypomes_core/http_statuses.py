from typing import Final

# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

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
        "name": "MULTIPLE CHOICE",
        "en": "",
        "pt": ""
    },
    301: {
        "name": "MOVED PERMANENTLY",
        "en": "",
        "pt": ""
    },
    302: {
        "name": "FOUND",
        "en": "",
        "pt": ""
    },
    303: {
        "name": "SEE OTHER",
        "en": "",
        "pt": ""
    },
    304: {
        "name": "NOT MODIFIED",
        "en": "",
        "pt": ""
    },
    305: {
        "name": "USE PROXY",
        "en": "",
        "pt": ""
    },
    307: {
        "name": "TEMPORARY REDIRECT",
        "en": "",
        "pt": ""
    },
    308: {
        "name": "PERMANENT REDIRECT",
        "en": "",
        "pt": ""
    },
    # Client error responses
    400: {
        "name": "BAD REQUEST",
        "en": "",
        "pt": ""
    },
    401: {
        "name": "UNAUTHORIZED",
        "en": "",
        "pt": ""
    },
    403: {
        "name": "FORBIDDEN",
        "en": "",
        "pt": ""
    },
    404: {
        "name": "NOT FOUND",
        "en": "",
        "pt": ""
    },
    405: {
        "name": "METHOD NOT ALLOWED",
        "en": "",
        "pt": ""
    },
    406: {
        "name": "NOT ACCEPTABLE",
        "en": "",
        "pt": ""
    },
    407: {
        "name": "AUTHENTICATION REQUIRED",
        "en": "",
        "pt": ""
    },
    408: {
        "name": "REQUEST TIMEOUT",
        "en": "",
        "pt": ""
    },
    409: {
        "name": "CONFLICT",
        "en": "",
        "pt": ""
    },
    410: {
        "name": "GONE",
        "en": "",
        "pt": ""
    },
    411: {
        "name": "LENGTH REQUIRED",
        "en": "",
        "pt": ""
    },
    412: {
        "name": "PRECONDITION FAILED",
        "en": "",
        "pt": ""
    },
    413: {
        "name": "PAYLOAD TOO LARGE",
        "en": "",
        "pt": ""
    },
    414: {
        "name": "URI TOO LONG",
        "en": "",
        "pt": ""
    },
    # Server error responses
    500: {
        "name": "INTERNAL SERVER ERROR",
        "en": "",
        "pt": ""
    },
    501: {
        "name": "NOT IMPLEMENTED",
        "en": "",
        "pt": ""
    },
    502: {
        "name": "BAD GATEWAY",
        "en": "",
        "pt": ""
    },
    503: {
        "name": "SERVICE UNAVAILABLE",
        "en": "",
        "pt": ""
    },
    504: {
        "name": "GATEWAY TIMEOUT",
        "en": "",
        "pt": ""
    },
    505: {
        "name": "HTTP VERSION NOT SUPPORTED",
        "en": "",
        "pt": ""
    },
    506: {
        "name": "VARIANT ALSO NEGOTIATES",
        "en": "",
        "pt": ""
    },
    507: {
        "name": "INSUFFICIENT STORAGE",
        "en": "",
        "pt": ""
    },
    508: {
        "name": "LOOP DETECTED",
        "en": "",
        "pt": ""
    },
    510: {
        "name": "NOT EXTENDED",
        "en": "",
        "pt": ""
    },
    511: {
        "name": "NETWORK AUTHENTICATION REQUIRED",
        "en": "",
        "pt": ""
    }
}
