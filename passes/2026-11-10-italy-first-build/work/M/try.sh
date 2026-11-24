T=../../../../tools
try(){ url="$1"; name="$2"; kind="$3"
  out=$(python $T/fetch.py "$url" "$name" 2>&1 | tail -1)
  if echo "$out" | grep -q "^OK"; then echo "DIRECT $name :: $out"; return; fi
  out2=$(python $T/wayback.py "$url" "$name" "$kind" 2>&1 | tail -1)
  echo "WAYBACK $name :: $out2"
}
try "https://ambdhaka.esteri.it/wp-content/uploads/2024/10/press-communique-16-October-2024-def.pdf" esteri-ambdhaka-press-communique-2024-10-16 official
try "https://www.interno.gov.it/it/temi/immigrazione-e-asilo/modalita-dingresso/decreto-flussi" interno-it-decreto-flussi official
try "https://www.interno.gov.it/it/sala-stampa/dati-e-statistiche/sbarchi-e-accoglienza-dei-migranti-tutti-i-dati" interno-sbarchi-tutti-i-dati official
try "https://prefettura.interno.gov.it/sites/default/files/75/2024-10/guida-pratica-per-i-richiedenti-protezione-internazionale.pdf" interno-guida-pratica-richiedenti-protezione-2024 official
try "https://www.interno.gov.it/it/notizie/stranieri-totalmente-digitale-procedura-ricongiungimento-familiare" interno-ricongiungimento-digitale official
try "https://www.lavoro.gov.it/documenti-e-norme/normativa/Circolare-8047-del-16102025" lavoro-gov-circolare-8047-2025 official
try "https://www.asianews.it/en/south-asia/bangladesh/dhaka-thousands-of-migrants-swindled-while-waiting-in-vain-for-visas-to-italy" news-asianews-dhaka-migrants-swindled-2024-05 news
try "https://www.bangladeshmonitor.com.bd/news-pdf/italy-to-approve-20000-visas-by-december-foreign-adviser" news-bdmonitor-italy-20000-visas news
try "https://missingmigrants.iom.int/region/mediterranean" iom-missing-migrants-mediterranean news
try "https://www.arabnews.pk/node/2641669/middle-east" news-arabnews-libya-zuwara-traffickers-jailed-2026-04 news
try "https://visa.vfsglobal.com/one-pager/italy/bangladesh/english/pdf/family_reunion_visa_checklist_new.pdf" vfs-italy-bd-family-reunion-checklist official
try "https://visa.vfsglobal.com/one-pager/italy/bangladesh/bangali/pdf/FAMILY-SUI_updated.pdf" vfs-italy-bd-family-sui-bn official
try "https://prefettura.interno.gov.it/sites/default/files/31/2024-01/vademecum_ricongiungimenti_familiari.docx" prefettura-vademecum-ricongiungimenti-2024 official
try "https://edotto.com/file-download/ministero-dellinterno-ministero-del-lavoro-e-delle-politiche-sociali-ministero-dellagricoltura-della-sovranita-alimentare-e-delle-foreste-ministero-del-turismo-circolare-congiunta-n-7185-del-1-ottobre-2026-pdf" interno-circolare-7185-2026-flussi-2027 official
try "https://rome.mofa.gov.bd/pages/static-pages/6952668435ce18e1c05a9baa" bdemb-rome-wewb-membership official
