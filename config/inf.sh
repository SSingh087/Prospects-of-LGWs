#!/bin/sh

PRIOR_CONFIG=prior.ini
INJ_FILES=./injections/inj_0.ini

pycbc_inference --verbose \
--config-file  ${PRIOR_CONFIG} ${INJ_FILES} \
--nprocesses=4 \
--output-file relative.hdf \
--seed 0 \
--force


