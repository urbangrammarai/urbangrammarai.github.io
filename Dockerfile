FROM darribas/gds_py:5.0

# Fix permissions
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

