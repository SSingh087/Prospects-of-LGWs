#cp /home/ss/Prospects-of-LGWs/unlens/injection.hdf ./ --verbose

/content/Prospects-of-LGWs/lens/evaluate_SNR \
--injection-file-lens-dir /content/Prospects-of-LGWs/lens/injection \
--injection-file-unlens-dir /content/Prospects-of-LGWs/unlens/injection \
--injection-file /content/Prospects-of-LGWs/lens/injection.hdf \
--inference-config /content/Prospects-of-LGWs/lens/prior.ini \
--instruments E1 E2 E3 \

