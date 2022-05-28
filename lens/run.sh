#cp /home/ss/Prospects-of-LGWs/unlens/injection.hdf ./ --verbose

/home/ss/Prospects-of-LGWs/lens/evaluate_SNR \
--injection-file-lens-dir /home/ss/Prospects-of-LGWs/lens/injection \
--injection-file-unlens-dir /home/ss/Prospects-of-LGWs/unlens/injection \
--injection-file /home/ss/Prospects-of-LGWs/lens/injection.hdf \
--inference-config /home/ss/Prospects-of-LGWs/lens/prior.ini \
--instruments E1 E2 E3 \

