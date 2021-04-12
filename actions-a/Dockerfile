FROM myoung34/github-runner:latest

ARG orgname="Bryant Org"
ARG reponame="bryantson-test-repo"

LABEL com.github.actions.name="Bryant Image" \
      com.github.actions.description="It is a build image" \
      com.github.actions.icon="code" \
      com.github.actions.color="red" \
      maintainer="Bryant Son <bryantson@github.com>" \
      org.opencontainers.image.authors="Bryant Son <bryantson@github.com>" \
      org.opencontainers.image.url="https://github.com/${orgname}/${reponame}" \
      org.opencontainers.image.source="https://github.com/${orgname}/${reponame}" \
      org.opencontainers.image.documentation="https://github.com/${orgname}/${reponame}" \
      org.opencontainers.image.vendor="GitHub" \
      org.opencontainers.image.description="Its a build image"
      
 # COPY dependencies/* /
 
 ########################
 # Make the directory ##
 ########################
 RUN mkdir -p /action/lib
 
 #######################
 # Copy scripts to container #
 #############################
 COPY actions-a/entrypoint.sh /action/lib
 
 #######################
 # Set the entrypoint #
 ######################
 ENTRYPOINT ["./entrypoint.sh"]
