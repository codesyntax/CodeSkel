# SSL Reference: https://mozilla.github.io/server-side-tls/ssl-config-generator/

<VirtualHost *:443>
    ServerName ${configuration:server-name}

    SSLEngine on
    SSLCertificateFile      ${configuration:ssl-certificate-path}
    SSLCertificateChainFile ${configuration:ssl-certificate-chain-path}
    SSLCertificateKeyFile   ${configuration:ssl-private-key-path}
    SSLCACertificateFile    ${configuration:ssl-ca-certificate-path}

    # modern configuration, tweak to your needs
    SSLProtocol             all -SSLv2 -SSLv3 -TLSv1
    SSLCipherSuite          ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK
    SSLHonorCipherOrder     on

    # HSTS (mod_headers is required) (15768000 seconds = 6 months)
    Header always add Strict-Transport-Security "max-age=15768000"

    # Zope directly
    RewriteRule ^/(.*) http://127.0.0.1:${ports:instance}/VirtualHostBase/http/%{HTTP_HOST}:443/Plone/VirtualHostRoot/$1 [L,P]
    # Varnish
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:varnish}/VirtualHostBase/http/%{HTTP_HOST}:443/Plone/VirtualHostRoot/$1 [L,P]
    # HAProxy
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:haproxy}/VirtualHostBase/http/%{HTTP_HOST}:443/Plone/VirtualHostRoot/$1 [L,P]

    ErrorLog ${configuration:apache-log-path}/${configuration:server-name}.error.log
    CustomLog ${configuration:apache-log-path}/${configuration:server-name}.access.log combined

</VirtualHost>

<VirtualHost *:80>
    ServerName ${configuration:server-name}
    ServerAlias ${configuration:additional-names}

    RewriteEngine On
    RewriteRule ^/(.*) https://${configuration:server-name}$1 [L, R=301]

</VirtualHost>
