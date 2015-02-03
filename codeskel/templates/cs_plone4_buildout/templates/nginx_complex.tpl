\# Reference: http://www.starzel.de/blog/securing-plone-sites-with-https-and-nginx

upstream \${buildout:projectname}plone {
       server 127.0.0.1:${ports:zope};
}

upstream \${buildout:projectname}varnish {
    server 127.0.0.1:${ports:varnish};
}

upstream \${buildout:projectname}haproxy {
    server 127.0.0.1:${ports:haproxy};
}

upstream \${buildout:projectname}editplone {
    server 127.0.0.1:${ports:editzope};
}

server {

    listen 80;
    server_name ${configuration:server-name} ${configuration:additional-names};
    access_log \${configuration:nginx-log-path}/\${configuration:server-name}.log;
    error_log  \${configuration:nginx-log-path}/\${configuration:server-name}.log;

    gzip            on;
    gzip_min_length 1000;


    rewrite ^(.*)(/login|/require_login|/failsafe_login_form)(.*) http://\${configuration:edit-server-name}$1$2$3 redirect;

    if ($http_cookie ~* "__ac=([^;]+)(?:;|$)" ) {
      rewrite ^/(.*) http://\${configuration:edit-server-name}/$1 redirect;
    }

    location /robots.txt {
       return 200 "User-agent: *\n Disallow: /";
    }

    location / {
        rewrite ^/(.*)$ /VirtualHostBase/http/$host:80/Plone/VirtualHostRoot/$1 break;
        \# Directly Zope
        proxy_pass http://\${buildout:projectname}plone;
        \# Varnish
        \#proxy_pass http://\${buildout:projectname}varnish;
        \# HAProxy
        \#proxy_pass http://\${buildout:projectname}haproxy;

    }
}

server {
       # VirtualHost berezia, editoreek katxeatu gabe ikusteko
       listen 80;
       server_name ${configuration:edit-server-name};
       access_log \${configuration:nginx-log-path}/${configuration:edit-server-name}_access.log;
       error_log  \${configuration:nginx-log-path}/${configuration:edit-server-name}_error.log;

       client_max_body_size 20M;


       location /robots.txt {
           return 200 "User-agent: *\nDisallow: /";
       }


       if ($http_cookie ~* "__ac=([^;]+)(?:;|$)" ) {
           # prevent infinite recursions between http and https
       break;
       }
       rewrite ^(.*)(/logged_out)(.*) http://${configuration:server-name}$1$2$3 redirect;

       location / {
            rewrite ^/(.*)$ /VirtualHostBase/http/$host:80/codesyntax/VirtualHostRoot/$1 break;
            # Egoeraren arabera aldatzeko, Varnish-ekin ala Varnish gabe
            proxy_pass http://${buildout:projectname}editplone;
            #proxy_pass http://${buildout:projectname}varnish;
       }

       set $redirect_to_http "1";
       if ($http_cookie ~* "__ac=([^;]+)(?:;|$)" ) {
          set $redirect_to_http "";
       }
       if ($uri ~* "(/login|/login_form|/require_login|/failsafe_login_form|logged_out)" ) {
          set $redirect_to_http "";
       }
       if ($redirect_to_http = "1") {
          rewrite ^(.*) http://${configuration:server-name}$1 redirect;
       }


}
