FROM dragoncrafted87/alpine:latest

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DragonCrafted87 NFS Server" \
      org.label-schema.description="Alpine NFS Server." \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/DragonCrafted87/docker-alpine-nfs-server" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

COPY root/. /

RUN apk add --update nfs-utils && \
    rm  -rf /tmp/* /var/cache/apk/* && \
    chmod +x /docker_service_init && \
    chmod +x /scripts/*

EXPOSE 111/tcp 111/udp
EXPOSE 2049/tcp 2049/udp
EXPOSE 32765/tcp 32765/udp
EXPOSE 32766/tcp 32766/udp
EXPOSE 32767/tcp 32767/udp

CMD ["/docker_service_init"]
