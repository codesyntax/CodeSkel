<VirtualHost *:80>
    ServerName ${configuration:server-name}
    ServerAlias ${configuration:additional-names}

    RewriteEngine On


    RewriteEngine On
    RewriteCond %{HTTP_COOKIE} "__ac="
    RewriteRule ^(.*) http://${configuration:edit-server-name}:80$1 [L]
    RewriteRule (.*)(/login|/require_login|/failsafe_login_form)(.*) http://${configuration:edit-server-name}:80$1$2$3 [R]

    # Zope directly
    RewriteRule ^/(.*) http://127.0.0.1:${ports:zope}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]
    # Varnish
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:varnish}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]



    ErrorLog /var/log/apache2/${configuration:server-name}.error.log
    CustomLog /var/log/apache2/${configuration:server-name}.access.log combined

</VirtualHost>

<VirtualHost *:80>
    ServerName ${configuration:edit-server-name}

    RewriteEngine On

    RewriteCond %{HTTP_COOKIE} "__ac=" [OR]
    RewriteCond %{REQUEST_URI} ^.*(/login|/login_form|/require_login|/failsafe_login_form|logged_out)$
    RewriteRule ^/(.*) http://127.0.0.1:${ports:editzope}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]

    RewriteRule ^/(.*) http://${configuration:server-name}/$1 [C]

    ErrorLog /var/log/apache2/${configuration:edit-server-name}.error.log
    CustomLog /var/log/apache2/${configuration:edit-server-name}.access.log combined

</VirtualHost>
