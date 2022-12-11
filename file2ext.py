name2ext_dict = {
    'RasterImage': ['art', 'arw', 'bmp', 'cr2', 'crw', 'dcm', 'dds', 'djvu', 'dng', 'exr', 'fpx', 'gif', 'ico', 'jpg',
                    'jp2', 'jpeg', 'nef', 'orf', 'pcd', 'pcx', 'pef', 'pgm', 'pict', 'png', 'psd', 'raf', 'sfw', 'tga',
                    'tiff', 'wbmp', 'xcf', 'yuv', 'kdc', 'pct', 'sr2', 'tif', 'hdr', 'webp', 'nrw', 'plist', 'ithmb',
                    'thm', 'pspimage', 'mac', 'heic', 'rwl', 'flif', 'avif', 'raw', 'pictclipping', 'jxr'],

    'VectorImage': ['emf', 'eps', 'svg', 'wpg', 'ai', 'svgz', 'wmf', 'odg', 'cdr', 'vsd', 'std', 'pd', 'emz', 'mix',
                    'otg', 'cvs', 'gvdesign'],

    'Document': ['pdf', 'txt', 'doc', 'odt', 'xps', 'chm', 'rtf', 'sxw', 'docx', 'wpd', 'wps', 'docm', 'hwp', 'pub',
                 'xml', 'log', 'oxps', 'vnt', 'dot', 'pages', 'm3u', 'dotx', 'shs', 'msg', 'odm', 'pmd', 'vmg', 'eml',
                 'tex', 'wp5', 'csk', 'fdxt', 'pages.zip', 'adoc', 'afpub'],

    'Audio': ['mpc', 'aac', 'flac', 'm4a', 'mmf', 'mp3', 'ogg', 'wav', 'wma', 'mid', 'amr', 'ape', 'au', 'caf', 'gsm',
              'oma', 'qcp', 'vqf', 'ra', 'aif', 'mp2', 'm4p', 'awb', 'm4r', 'ram', 'asx', 'mpga', 'aiff', 'koz', 'm4b',
              'kar', 'iff', 'midi', '3ga', 'opus', 'aup', 'xspf', 'aifc', 'rta', 'cda', 'm3u8', 'mpa', 'aa', 'aax',
              'oga', 'nfa', 'adpcm', 'cdo', 'flp', 'aimppl', '4mp', 'mui'],

    'Video': ['avi', 'mpeg', 'm4v', 'mov', 'mp4', 'wmv', 'mpg', 'swf', '3gp', '3g2', 'mkv', 'ogv', 'webm', 'asf', 'ts',
              'mxf', 'rm', 'thp', 'mts', 'rmvb', 'f4v', 'mod', 'vob', 'h264', 'flv', '3gpp', 'divx', 'qt', 'amv',
              'dvsd', 'm2ts', 'ifo', 'mswmm', 'srt', 'cpi', 'wlmp', 'vpj', 'ced', 'vep', 'veg', '264', 'dav', 'pds',
              'dir', 'arf', 'mepx', 'xesc', 'bik', 'nfv', 'tvs', 'imoviemobile', 'rcproject', 'esp3', 'vproj', 'aep',
              'camproj', 'camrec', 'cmproj', 'cmrec', 'modd', 'mproj', 'osp', 'trec', 'g64', 'vro', 'braw', 'mse', 'pz'
              ],

    'Ebook': ['cbr', 'epub', 'fb2', 'lit', 'lrf', 'mobi', 'tcr', 'prc', 'azw3', 'azw', 'acsm', 'opf', 'mbp', 'cbz',
              'apnx', 'cbt', 'vbk', 'ibooks', 'kfx'],

    'Cad': ['dxf', 'dwg', '3dm', '3ds', 'max', 'obj', 'stp'],

    'Presentation': ['odp', 'ppt', 'pptx', 'pps', 'ppsx', 'pptm', 'key', 'flipchart', 'key.zip'],

    'Spreadsheet': ['ods', 'xls', 'xlsx', 'csv', 'wks', 'xlsm', 'xlsb', 'xlr', 'wk3', 'numbers'],

    'Database': ['pdb', 'dbf', 'bup', 'db', 'crypt', 'accdb', 'mdb', 'sql'],

    'Archive': ['zip', 'rar', '7z', 'bz2', 'gz', 'tar', 'snb', 'jar', 'apk', 'mht', 'tgz', 'gzip', 'crx', 'deb', 'rpm',
                'sitx', 'tar.gz', 'zipx', 'sit', 'ace', 'dd', 'r01', 'mpkg', 'pup', 'tbz'],

    'Website': ['html', 'htm', 'xhtml', 'aspx', 'php', 'js', 'nzb', 'json', 'do', 'css', 'webloc', 'xfdl', 'asp', 'cer',
                'cfm', 'csr', 'jsp', 'rss', 'cfml', 'mhtml', 'webarchive'],

    'Misc': ['ps', 'ttf', 'pes', 'otf', 'ass', 'rem', 'dmg', 'jad', 'tmp', 'url', 'cue', 'ics', 'img', 'bak', 'part',
             'tec', 'kmz', 'torrent', 'hqx', 'msi', 'crdownload', 'dem', 'fnt', 'fon', 'gam', 'gpx', 'iso', 'kml',
             'mdf', 'mim', 'nes', 'plugin', 'rom', 'sav', 'toast', 'uue', 'vcd', 'idx', 'epc', 'map', 'dbx', 'dic',
             'hex', 'qxp', 'grp', '8bi', 'cmf', 'ori', 'bfc', 'gho', 'mtb', 't65', 'xll', 'dao', 'flt', 'cff', 'bbl',
             'bib', 'bibtex', 'enl', 'ens', 'enw', 'marc', 'mrc', 'ris', 'enc', 'approj', 'mime', 'hht'],

    'Developer': ['rc', 'p', 'd', 'c', 'class', 'cpp', 'cs', 'dtd', 'fla', 'h', 'java', 'lua', 'm', 'pl', 'py', 'sh',
                  'sln', 'swift', 'vcxproj', 'xcodeproj', 'asc', 'bas', 'asm', 'cbl', 'vbp', 'iwb', 'pb', 'yml', 'pika',
                  's19', 'xt', 'suo', 'fsproj', 'pbj', 'pbxuser', 'pyw', 'xq', 'cd', 'sb', 'sb2', 'ise', 'kv', 'cod',
                  'nib', 'pwn', 'b', 'hpp', 'apa', 'bet', 'bluej', 'erb', 'fxc', 'm4', 'owl', 'sma', 'trx', 'vc', 'def',
                  'xap', 'o', 'pas', 'qpr', 'resources', 'vbproj', 'vbx', 'xib', 'md', 'ccc', 'wwp', 'ss'],

    'System': ['cur', 'ani', 'dvd', 'dat', 'lnk', 'dll', 'nfo', 'prop', 'bin', 'cab', 'cpl', 'deskthemepack', 'dmp',
               'drv', 'icns', 'sys', 'cat', 'hlp', 'icl', 'bud', 'dev', 'ffl', 'ffo', 'pol', 'ion', 'pnf', 'dit', 'htt',
               'nb0', 'mlc', 'bash_history', 'ebd', 'fota', 'reg', 'bashrc', 'hiv', 'bash_profile', 'nt', 'qvm',
               'iconpackage', 'iptheme', 'pck', 'hdmp', 'mdmp', 'sdt'],

    'Data': ['dif', 'vcf', 'itl', 'one', 'ged', 'keychain', 'sdf', 'tax2014', 'efx', 'clp', 'gbr', 'tax2012', 'mtw',
             'gms', 'ip', 'tax2016', 'quickendata', 'adt', 'cma', 'fcpevent', 'flo', 'gcw', 'i5z', 'qb2011', 'vcs',
             'cel', 'aae', 'nfs', 'nfi', 'xmind', 'bok', 'tax', 'ova', 'ovf', 'rte', 'rvt'],

    'Executables': ['scr', 'exe', 'ipa', 'app', 'bat', 'cgi', 'com', 'gadget', 'pif', 'vb', 'wsf', 'cmd', 'ds', 'air'],

    'PageLayout': ['mdi', 'indd', 'p65', 'qxd', 'dtp', 'rels', 'caj', 'eddx', 'lbl'],

    'Settings': ['act', 'inf', 'ini', 'cfg', 'pkg', 'cdt', 'icm', 'gid', 'api', 'dun', 'ht', 'prf', 'fm3', 'rdf', 'asw',
                 'mind', 'tscproj']
}
