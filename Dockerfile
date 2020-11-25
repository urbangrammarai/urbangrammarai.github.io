FROM darribas/gds_py:5.0

# Local docs
RUN rm -R work/
COPY . ${HOME}

# Fix permissions
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

