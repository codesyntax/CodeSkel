<VirtualHost *:80>
    ServerName ${configuration:server-name}
    ServerAlias ${configuration:additional-names}

    RewriteEngine On
    # Zope directly
    RewriteRule ^/(.*) http://127.0.0.1:${ports:instance}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]
    # Varnish
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:varnish}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]
    # HAProxy
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:haproxy}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]


    ErrorLog ${configuration:apache-log-path}/${configuration:server-name}.error.log
    CustomLog ${configuration:apache-log-path}/${configuration:server-name}.access.log combined

</VirtualHost>
