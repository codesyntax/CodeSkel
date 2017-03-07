server {
    listen       80;
    server_name  ${servername};
    access_log  ${logpath}/${servername}_access.log;
    error_log  ${logpath}/${servername}_error.log;

    gzip            on;
    gzip_min_length 1000;
    gzip_proxied    expired no-cache no-store private auth;
    gzip_types      text/html text/plain application/xml text/css application/x-javascript text/javascript;

    location / {
        proxy_pass  http://unix:${buildout:directory}/gunicorn.sock;
        proxy_redirect              off;
        proxy_set_header            Host $host;
        proxy_set_header            X-Real-IP $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size        10m;
        client_body_buffer_size     128k;
        proxy_connect_timeout       90;
        proxy_send_timeout          90;
        proxy_read_timeout          90;
        proxy_buffer_size           4k;
        proxy_buffers               4 32k;
        proxy_busy_buffers_size     64k;
        proxy_temp_file_write_size  64k;
    }

    location /favicon.ico {
        root ${buildout:directory}/../static/img;
    }

    location /static  {
        alias ${buildout:directory}/../static;
        expires max;

       }
    location /media  {
        alias ${buildout:directory}/../media;
        expires max;
       }

    location /robots.txt {
        return 200 "User-agent: *\nDisallow: ";
    }


    error_page   500 502  503 504  /50x.html;
    location =  /50x.html {
        root    html;
      }
}

server {
    listen 80;
    server_name www.${servername};
    return 301 http://${servername}$request_uri;
}
