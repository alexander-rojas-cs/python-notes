FROM python:3.14-rc-slim

# Instalar Git, bash-completion y los scripts de autocompletado específicos de Git
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    bash-completion \
    && rm -rf /var/lib/apt/lists/*

# Configurar un prompt corto y claro para la terminal
RUN echo 'PS1="🐳 [docker: \w]\$ "' >> /root/.bashrc
RUN echo 'PS1="🐳 [docker: \w]\$ "' >> /etc/bash.bashrc

# Habilitar el autocompletado general y el de Git en el sistema
RUN echo "if [ -f /etc/bash_completion ]; then . /etc/bash_completion; fi" >> /etc/bash.bashrc
RUN echo "if [ -f /usr/share/bash-completion/completions/git ]; then . /usr/share/bash-completion/completions/git; fi" >> /etc/bash.bashrc

WORKDIR /app