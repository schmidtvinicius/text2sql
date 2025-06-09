grammar text2sql;

options {
    language = Python;
}

prog: (table columnList?|columnList table?) comparison?
    | aggregator column
    | INT? table ordering
    | INT? ordering table
    ;

table: vulnerability;

columnList: column ( column)*;

vulnerability: ('kwetsbaarheid'|'kwetsbaarheden');

aggregator: max|min|avg;
max: 'maximale'|'maximaal'|'max';
min: 'minimale'|'minimaal'|'min';
avg: 'gemiddeld'|'gemiddelde';

column: cve|title|confidence|severity|cvss|epss|age|kev|cwe;
cve: 'cve'|'cve\'s'|'cves'|'CVE'|'CVE\'s'|'CVEs';
title: 'title'|'titel';
confidence: 'confidence'|'zekerheid';
severity: ('ernst'|'severity');
cvss: 'cvss'|'cvss-score'|'cvss score'|'CVSS'|'CVSS-score'|'CVSS score';
epss: 'epss'|'epss-score'|'epss score'|'EPSS'|'EPSS-score'|'EPSS score';
age: ('leeftijd'|'age');
cwe: 'cwe'|'cwe\'s'|'cwes'|'CWE'|'CWE\'s'|'CWEs';
kev: 'kev'|'cisa-kev'|'cisa kev'|'CISA KEV'|'KEV'|'CISA-KEV';

comparison: number_comparison|bool_comparison|text_comparison;
number_comparison: (numeric_column|INT|FLOAT) (gt|lt|eq) (numeric_column|INT|FLOAT);
bool_comparison: kev (eq bool|bool)?;
text_comparison: (severity|cve|cwe|title) (eq|like) (severity_scale|STRING);

numeric_column: (cvss|epss|age|confidence);

operator: gt|lt|eq|like;
gt: ('groter'|'hoger'|'ouder'|'meer') 'dan'?;
lt: ('kleiner'|'lager'|'jonger'|'minder') 'dan'?;
eq: 'gelijk'?;
like: 'bevat'|'heeft';

ordering: order column?;

order: asc|desc;
desc: ('grootste'|'hoogste'|'aflopend'|'descending'|'oudste');
asc: ('kleinste'|'laagste'|'oplopend'|'ascending'|'jongste'|'nieuwste');

value: INT|severity_scale|bool|STRING;
INT: '0'|[1-9][0-9]*;
FLOAT: ([0-9]'.'[0-9]{1,2}|'10.0');
bool: true|false;
true: ('true'|'waar'|'bestaat');
false: ('false'|'onwaar'|'niet bestaat');
severity_scale: ('informational'|'low'|'medium'|'high'|'critical');
STRING: '\'' (~'\'' .)* '\'';

WS : [ \t\r\n]+ -> skip;