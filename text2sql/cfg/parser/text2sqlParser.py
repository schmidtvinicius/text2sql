# Generated from text2sql/cfg/parser/text2sql.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,86,250,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,3,0,77,8,0,1,0,1,0,3,
        0,81,8,0,3,0,83,8,0,1,0,3,0,86,8,0,1,0,1,0,1,0,1,0,3,0,92,8,0,1,
        0,1,0,1,0,1,0,3,0,98,8,0,1,0,1,0,1,0,3,0,103,8,0,1,1,1,1,1,2,1,2,
        5,2,109,8,2,10,2,12,2,112,9,2,1,3,1,3,1,4,1,4,1,4,3,4,119,8,4,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,136,
        8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,
        15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,3,18,159,8,18,1,19,1,
        19,1,19,3,19,164,8,19,1,19,1,19,1,19,3,19,169,8,19,1,19,1,19,1,19,
        3,19,174,8,19,1,20,1,20,1,20,1,20,1,20,3,20,181,8,20,1,21,1,21,1,
        21,1,21,3,21,187,8,21,1,21,1,21,3,21,191,8,21,1,21,1,21,3,21,195,
        8,21,1,22,1,22,1,22,1,22,3,22,201,8,22,1,23,1,23,1,23,1,23,3,23,
        207,8,23,1,24,1,24,3,24,211,8,24,1,25,1,25,3,25,215,8,25,1,26,3,
        26,218,8,26,1,27,1,27,1,28,1,28,3,28,224,8,28,1,29,1,29,3,29,228,
        8,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,32,3,32,238,8,32,1,33,
        1,33,3,33,242,8,33,1,34,1,34,1,35,1,35,1,36,1,36,1,36,0,0,37,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,0,21,1,0,1,2,1,0,3,5,1,0,6,8,
        1,0,9,10,1,0,11,16,1,0,17,18,1,0,19,20,1,0,21,22,1,0,23,28,1,0,29,
        34,1,0,35,36,1,0,37,42,1,0,43,48,1,0,49,52,1,0,54,57,1,0,59,60,1,
        0,61,65,1,0,66,71,1,0,72,74,1,0,75,77,1,0,78,82,262,0,102,1,0,0,
        0,2,104,1,0,0,0,4,106,1,0,0,0,6,113,1,0,0,0,8,118,1,0,0,0,10,120,
        1,0,0,0,12,122,1,0,0,0,14,124,1,0,0,0,16,135,1,0,0,0,18,137,1,0,
        0,0,20,139,1,0,0,0,22,141,1,0,0,0,24,143,1,0,0,0,26,145,1,0,0,0,
        28,147,1,0,0,0,30,149,1,0,0,0,32,151,1,0,0,0,34,153,1,0,0,0,36,158,
        1,0,0,0,38,163,1,0,0,0,40,175,1,0,0,0,42,186,1,0,0,0,44,200,1,0,
        0,0,46,206,1,0,0,0,48,208,1,0,0,0,50,212,1,0,0,0,52,217,1,0,0,0,
        54,219,1,0,0,0,56,221,1,0,0,0,58,227,1,0,0,0,60,229,1,0,0,0,62,231,
        1,0,0,0,64,237,1,0,0,0,66,241,1,0,0,0,68,243,1,0,0,0,70,245,1,0,
        0,0,72,247,1,0,0,0,74,76,3,2,1,0,75,77,3,4,2,0,76,75,1,0,0,0,76,
        77,1,0,0,0,77,83,1,0,0,0,78,80,3,4,2,0,79,81,3,2,1,0,80,79,1,0,0,
        0,80,81,1,0,0,0,81,83,1,0,0,0,82,74,1,0,0,0,82,78,1,0,0,0,83,85,
        1,0,0,0,84,86,3,36,18,0,85,84,1,0,0,0,85,86,1,0,0,0,86,103,1,0,0,
        0,87,88,3,8,4,0,88,89,3,16,8,0,89,103,1,0,0,0,90,92,5,83,0,0,91,
        90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,0,93,94,3,2,1,0,94,95,3,56,
        28,0,95,103,1,0,0,0,96,98,5,83,0,0,97,96,1,0,0,0,97,98,1,0,0,0,98,
        99,1,0,0,0,99,100,3,56,28,0,100,101,3,2,1,0,101,103,1,0,0,0,102,
        82,1,0,0,0,102,87,1,0,0,0,102,91,1,0,0,0,102,97,1,0,0,0,103,1,1,
        0,0,0,104,105,3,6,3,0,105,3,1,0,0,0,106,110,3,16,8,0,107,109,3,16,
        8,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,
        0,0,111,5,1,0,0,0,112,110,1,0,0,0,113,114,7,0,0,0,114,7,1,0,0,0,
        115,119,3,10,5,0,116,119,3,12,6,0,117,119,3,14,7,0,118,115,1,0,0,
        0,118,116,1,0,0,0,118,117,1,0,0,0,119,9,1,0,0,0,120,121,7,1,0,0,
        121,11,1,0,0,0,122,123,7,2,0,0,123,13,1,0,0,0,124,125,7,3,0,0,125,
        15,1,0,0,0,126,136,3,18,9,0,127,136,3,20,10,0,128,136,3,22,11,0,
        129,136,3,24,12,0,130,136,3,26,13,0,131,136,3,28,14,0,132,136,3,
        30,15,0,133,136,3,34,17,0,134,136,3,32,16,0,135,126,1,0,0,0,135,
        127,1,0,0,0,135,128,1,0,0,0,135,129,1,0,0,0,135,130,1,0,0,0,135,
        131,1,0,0,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,
        17,1,0,0,0,137,138,7,4,0,0,138,19,1,0,0,0,139,140,7,5,0,0,140,21,
        1,0,0,0,141,142,7,6,0,0,142,23,1,0,0,0,143,144,7,7,0,0,144,25,1,
        0,0,0,145,146,7,8,0,0,146,27,1,0,0,0,147,148,7,9,0,0,148,29,1,0,
        0,0,149,150,7,10,0,0,150,31,1,0,0,0,151,152,7,11,0,0,152,33,1,0,
        0,0,153,154,7,12,0,0,154,35,1,0,0,0,155,159,3,38,19,0,156,159,3,
        40,20,0,157,159,3,42,21,0,158,155,1,0,0,0,158,156,1,0,0,0,158,157,
        1,0,0,0,159,37,1,0,0,0,160,164,3,44,22,0,161,164,5,83,0,0,162,164,
        5,84,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,0,164,168,
        1,0,0,0,165,169,3,48,24,0,166,169,3,50,25,0,167,169,3,52,26,0,168,
        165,1,0,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,173,1,0,0,0,170,
        174,3,44,22,0,171,174,5,83,0,0,172,174,5,84,0,0,173,170,1,0,0,0,
        173,171,1,0,0,0,173,172,1,0,0,0,174,39,1,0,0,0,175,180,3,34,17,0,
        176,177,3,52,26,0,177,178,3,66,33,0,178,181,1,0,0,0,179,181,3,66,
        33,0,180,176,1,0,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,41,1,0,
        0,0,182,187,3,24,12,0,183,187,3,18,9,0,184,187,3,32,16,0,185,187,
        3,20,10,0,186,182,1,0,0,0,186,183,1,0,0,0,186,184,1,0,0,0,186,185,
        1,0,0,0,187,190,1,0,0,0,188,191,3,52,26,0,189,191,3,54,27,0,190,
        188,1,0,0,0,190,189,1,0,0,0,191,194,1,0,0,0,192,195,3,72,36,0,193,
        195,5,85,0,0,194,192,1,0,0,0,194,193,1,0,0,0,195,43,1,0,0,0,196,
        201,3,26,13,0,197,201,3,28,14,0,198,201,3,30,15,0,199,201,3,22,11,
        0,200,196,1,0,0,0,200,197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,
        0,201,45,1,0,0,0,202,207,3,48,24,0,203,207,3,50,25,0,204,207,3,52,
        26,0,205,207,3,54,27,0,206,202,1,0,0,0,206,203,1,0,0,0,206,204,1,
        0,0,0,206,205,1,0,0,0,207,47,1,0,0,0,208,210,7,13,0,0,209,211,5,
        53,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,49,1,0,0,0,212,214,7,
        14,0,0,213,215,5,53,0,0,214,213,1,0,0,0,214,215,1,0,0,0,215,51,1,
        0,0,0,216,218,5,58,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,53,1,
        0,0,0,219,220,7,15,0,0,220,55,1,0,0,0,221,223,3,58,29,0,222,224,
        3,16,8,0,223,222,1,0,0,0,223,224,1,0,0,0,224,57,1,0,0,0,225,228,
        3,62,31,0,226,228,3,60,30,0,227,225,1,0,0,0,227,226,1,0,0,0,228,
        59,1,0,0,0,229,230,7,16,0,0,230,61,1,0,0,0,231,232,7,17,0,0,232,
        63,1,0,0,0,233,238,5,83,0,0,234,238,3,72,36,0,235,238,3,66,33,0,
        236,238,5,85,0,0,237,233,1,0,0,0,237,234,1,0,0,0,237,235,1,0,0,0,
        237,236,1,0,0,0,238,65,1,0,0,0,239,242,3,68,34,0,240,242,3,70,35,
        0,241,239,1,0,0,0,241,240,1,0,0,0,242,67,1,0,0,0,243,244,7,18,0,
        0,244,69,1,0,0,0,245,246,7,19,0,0,246,71,1,0,0,0,247,248,7,20,0,
        0,248,73,1,0,0,0,27,76,80,82,85,91,97,102,110,118,135,158,163,168,
        173,180,186,190,194,200,206,210,214,217,223,227,237,241
    ]

class text2sqlParser ( Parser ):

    grammarFileName = "text2sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'kwetsbaarheid'", "'kwetsbaarheden'", 
                     "'maximale'", "'maximaal'", "'max'", "'minimale'", 
                     "'minimaal'", "'min'", "'gemiddeld'", "'gemiddelde'", 
                     "'cve'", "'cve's'", "'cves'", "'CVE'", "'CVE's'", "'CVEs'", 
                     "'title'", "'titel'", "'confidence'", "'zekerheid'", 
                     "'ernst'", "'severity'", "'cvss'", "'cvss-score'", 
                     "'cvss score'", "'CVSS'", "'CVSS-score'", "'CVSS score'", 
                     "'epss'", "'epss-score'", "'epss score'", "'EPSS'", 
                     "'EPSS-score'", "'EPSS score'", "'leeftijd'", "'age'", 
                     "'cwe'", "'cwe's'", "'cwes'", "'CWE'", "'CWE's'", "'CWEs'", 
                     "'kev'", "'cisa-kev'", "'cisa kev'", "'CISA KEV'", 
                     "'KEV'", "'CISA-KEV'", "'groter'", "'hoger'", "'ouder'", 
                     "'meer'", "'dan'", "'kleiner'", "'lager'", "'jonger'", 
                     "'minder'", "'gelijk'", "'bevat'", "'heeft'", "'grootste'", 
                     "'hoogste'", "'aflopend'", "'descending'", "'oudste'", 
                     "'kleinste'", "'laagste'", "'oplopend'", "'ascending'", 
                     "'jongste'", "'nieuwste'", "'true'", "'waar'", "'bestaat'", 
                     "'false'", "'onwaar'", "'niet bestaat'", "'informational'", 
                     "'low'", "'medium'", "'high'", "'critical'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "STRING", "WS" ]

    RULE_prog = 0
    RULE_table = 1
    RULE_columnList = 2
    RULE_vulnerability = 3
    RULE_aggregator = 4
    RULE_max = 5
    RULE_min = 6
    RULE_avg = 7
    RULE_column = 8
    RULE_cve = 9
    RULE_title = 10
    RULE_confidence = 11
    RULE_severity = 12
    RULE_cvss = 13
    RULE_epss = 14
    RULE_age = 15
    RULE_cwe = 16
    RULE_kev = 17
    RULE_comparison = 18
    RULE_number_comparison = 19
    RULE_bool_comparison = 20
    RULE_text_comparison = 21
    RULE_numeric_column = 22
    RULE_operator = 23
    RULE_gt = 24
    RULE_lt = 25
    RULE_eq = 26
    RULE_like = 27
    RULE_ordering = 28
    RULE_order = 29
    RULE_desc = 30
    RULE_asc = 31
    RULE_value = 32
    RULE_bool = 33
    RULE_true = 34
    RULE_false = 35
    RULE_severity_scale = 36

    ruleNames =  [ "prog", "table", "columnList", "vulnerability", "aggregator", 
                   "max", "min", "avg", "column", "cve", "title", "confidence", 
                   "severity", "cvss", "epss", "age", "cwe", "kev", "comparison", 
                   "number_comparison", "bool_comparison", "text_comparison", 
                   "numeric_column", "operator", "gt", "lt", "eq", "like", 
                   "ordering", "order", "desc", "asc", "value", "bool", 
                   "true", "false", "severity_scale" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    INT=83
    FLOAT=84
    STRING=85
    WS=86

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table(self):
            return self.getTypedRuleContext(text2sqlParser.TableContext,0)


        def columnList(self):
            return self.getTypedRuleContext(text2sqlParser.ColumnListContext,0)


        def comparison(self):
            return self.getTypedRuleContext(text2sqlParser.ComparisonContext,0)


        def aggregator(self):
            return self.getTypedRuleContext(text2sqlParser.AggregatorContext,0)


        def column(self):
            return self.getTypedRuleContext(text2sqlParser.ColumnContext,0)


        def ordering(self):
            return self.getTypedRuleContext(text2sqlParser.OrderingContext,0)


        def INT(self):
            return self.getToken(text2sqlParser.INT, 0)

        def getRuleIndex(self):
            return text2sqlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = text2sqlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2]:
                    self.state = 74
                    self.table()
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 75
                        self.columnList()


                    pass
                elif token in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                    self.state = 78
                    self.columnList()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==1 or _la==2:
                        self.state = 79
                        self.table()


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953419264) != 0) or _la==83 or _la==84:
                    self.state = 84
                    self.comparison()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.aggregator()
                self.state = 88
                self.column()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 90
                    self.match(text2sqlParser.INT)


                self.state = 93
                self.table()
                self.state = 94
                self.ordering()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 96
                    self.match(text2sqlParser.INT)


                self.state = 99
                self.ordering()
                self.state = 100
                self.table()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vulnerability(self):
            return self.getTypedRuleContext(text2sqlParser.VulnerabilityContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = text2sqlParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.vulnerability()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(text2sqlParser.ColumnContext)
            else:
                return self.getTypedRuleContext(text2sqlParser.ColumnContext,i)


        def getRuleIndex(self):
            return text2sqlParser.RULE_columnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnList" ):
                listener.enterColumnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnList" ):
                listener.exitColumnList(self)




    def columnList(self):

        localctx = text2sqlParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columnList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.column()
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 107
                    self.column() 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VulnerabilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_vulnerability

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVulnerability" ):
                listener.enterVulnerability(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVulnerability" ):
                listener.exitVulnerability(self)




    def vulnerability(self):

        localctx = text2sqlParser.VulnerabilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vulnerability)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def max_(self):
            return self.getTypedRuleContext(text2sqlParser.MaxContext,0)


        def min_(self):
            return self.getTypedRuleContext(text2sqlParser.MinContext,0)


        def avg(self):
            return self.getTypedRuleContext(text2sqlParser.AvgContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_aggregator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregator" ):
                listener.enterAggregator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregator" ):
                listener.exitAggregator(self)




    def aggregator(self):

        localctx = text2sqlParser.AggregatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregator)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.max_()
                pass
            elif token in [6, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.min_()
                pass
            elif token in [9, 10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.avg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_max

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMax" ):
                listener.enterMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMax" ):
                listener.exitMax(self)




    def max_(self):

        localctx = text2sqlParser.MaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_max)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_min

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin" ):
                listener.enterMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin" ):
                listener.exitMin(self)




    def min_(self):

        localctx = text2sqlParser.MinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_min)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AvgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_avg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvg" ):
                listener.enterAvg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvg" ):
                listener.exitAvg(self)




    def avg(self):

        localctx = text2sqlParser.AvgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_avg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cve(self):
            return self.getTypedRuleContext(text2sqlParser.CveContext,0)


        def title(self):
            return self.getTypedRuleContext(text2sqlParser.TitleContext,0)


        def confidence(self):
            return self.getTypedRuleContext(text2sqlParser.ConfidenceContext,0)


        def severity(self):
            return self.getTypedRuleContext(text2sqlParser.SeverityContext,0)


        def cvss(self):
            return self.getTypedRuleContext(text2sqlParser.CvssContext,0)


        def epss(self):
            return self.getTypedRuleContext(text2sqlParser.EpssContext,0)


        def age(self):
            return self.getTypedRuleContext(text2sqlParser.AgeContext,0)


        def kev(self):
            return self.getTypedRuleContext(text2sqlParser.KevContext,0)


        def cwe(self):
            return self.getTypedRuleContext(text2sqlParser.CweContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = text2sqlParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_column)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.cve()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.title()
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.confidence()
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.severity()
                pass
            elif token in [23, 24, 25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.cvss()
                pass
            elif token in [29, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.epss()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.age()
                pass
            elif token in [43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.kev()
                pass
            elif token in [37, 38, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.cwe()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_cve

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCve" ):
                listener.enterCve(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCve" ):
                listener.exitCve(self)




    def cve(self):

        localctx = text2sqlParser.CveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cve)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)




    def title(self):

        localctx = text2sqlParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_title)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfidenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_confidence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfidence" ):
                listener.enterConfidence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfidence" ):
                listener.exitConfidence(self)




    def confidence(self):

        localctx = text2sqlParser.ConfidenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_confidence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeverityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_severity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeverity" ):
                listener.enterSeverity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeverity" ):
                listener.exitSeverity(self)




    def severity(self):

        localctx = text2sqlParser.SeverityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_severity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CvssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_cvss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvss" ):
                listener.enterCvss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvss" ):
                listener.exitCvss(self)




    def cvss(self):

        localctx = text2sqlParser.CvssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cvss)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EpssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_epss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpss" ):
                listener.enterEpss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpss" ):
                listener.exitEpss(self)




    def epss(self):

        localctx = text2sqlParser.EpssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_epss)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_age

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAge" ):
                listener.enterAge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAge" ):
                listener.exitAge(self)




    def age(self):

        localctx = text2sqlParser.AgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_age)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CweContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_cwe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCwe" ):
                listener.enterCwe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCwe" ):
                listener.exitCwe(self)




    def cwe(self):

        localctx = text2sqlParser.CweContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cwe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8658654068736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KevContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_kev

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKev" ):
                listener.enterKev(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKev" ):
                listener.exitKev(self)




    def kev(self):

        localctx = text2sqlParser.KevContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_kev)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 554153860399104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_comparison(self):
            return self.getTypedRuleContext(text2sqlParser.Number_comparisonContext,0)


        def bool_comparison(self):
            return self.getTypedRuleContext(text2sqlParser.Bool_comparisonContext,0)


        def text_comparison(self):
            return self.getTypedRuleContext(text2sqlParser.Text_comparisonContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = text2sqlParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparison)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 83, 84]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.number_comparison()
                pass
            elif token in [43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.bool_comparison()
                pass
            elif token in [11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 37, 38, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.text_comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_comparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(text2sqlParser.Numeric_columnContext)
            else:
                return self.getTypedRuleContext(text2sqlParser.Numeric_columnContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(text2sqlParser.INT)
            else:
                return self.getToken(text2sqlParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(text2sqlParser.FLOAT)
            else:
                return self.getToken(text2sqlParser.FLOAT, i)

        def gt(self):
            return self.getTypedRuleContext(text2sqlParser.GtContext,0)


        def lt(self):
            return self.getTypedRuleContext(text2sqlParser.LtContext,0)


        def eq(self):
            return self.getTypedRuleContext(text2sqlParser.EqContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_number_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_comparison" ):
                listener.enterNumber_comparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_comparison" ):
                listener.exitNumber_comparison(self)




    def number_comparison(self):

        localctx = text2sqlParser.Number_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_number_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
                self.state = 160
                self.numeric_column()
                pass
            elif token in [83]:
                self.state = 161
                self.match(text2sqlParser.INT)
                pass
            elif token in [84]:
                self.state = 162
                self.match(text2sqlParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49, 50, 51, 52]:
                self.state = 165
                self.gt()
                pass
            elif token in [54, 55, 56, 57]:
                self.state = 166
                self.lt()
                pass
            elif token in [19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 58, 83, 84]:
                self.state = 167
                self.eq()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
                self.state = 170
                self.numeric_column()
                pass
            elif token in [83]:
                self.state = 171
                self.match(text2sqlParser.INT)
                pass
            elif token in [84]:
                self.state = 172
                self.match(text2sqlParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_comparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kev(self):
            return self.getTypedRuleContext(text2sqlParser.KevContext,0)


        def eq(self):
            return self.getTypedRuleContext(text2sqlParser.EqContext,0)


        def bool_(self):
            return self.getTypedRuleContext(text2sqlParser.BoolContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_bool_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_comparison" ):
                listener.enterBool_comparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_comparison" ):
                listener.exitBool_comparison(self)




    def bool_comparison(self):

        localctx = text2sqlParser.Bool_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bool_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.kev()
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 176
                self.eq()
                self.state = 177
                self.bool_()

            elif la_ == 2:
                self.state = 179
                self.bool_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_comparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def severity(self):
            return self.getTypedRuleContext(text2sqlParser.SeverityContext,0)


        def cve(self):
            return self.getTypedRuleContext(text2sqlParser.CveContext,0)


        def cwe(self):
            return self.getTypedRuleContext(text2sqlParser.CweContext,0)


        def title(self):
            return self.getTypedRuleContext(text2sqlParser.TitleContext,0)


        def eq(self):
            return self.getTypedRuleContext(text2sqlParser.EqContext,0)


        def like(self):
            return self.getTypedRuleContext(text2sqlParser.LikeContext,0)


        def severity_scale(self):
            return self.getTypedRuleContext(text2sqlParser.Severity_scaleContext,0)


        def STRING(self):
            return self.getToken(text2sqlParser.STRING, 0)

        def getRuleIndex(self):
            return text2sqlParser.RULE_text_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_comparison" ):
                listener.enterText_comparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_comparison" ):
                listener.exitText_comparison(self)




    def text_comparison(self):

        localctx = text2sqlParser.Text_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_text_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22]:
                self.state = 182
                self.severity()
                pass
            elif token in [11, 12, 13, 14, 15, 16]:
                self.state = 183
                self.cve()
                pass
            elif token in [37, 38, 39, 40, 41, 42]:
                self.state = 184
                self.cwe()
                pass
            elif token in [17, 18]:
                self.state = 185
                self.title()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58, 78, 79, 80, 81, 82, 85]:
                self.state = 188
                self.eq()
                pass
            elif token in [59, 60]:
                self.state = 189
                self.like()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79, 80, 81, 82]:
                self.state = 192
                self.severity_scale()
                pass
            elif token in [85]:
                self.state = 193
                self.match(text2sqlParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_columnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cvss(self):
            return self.getTypedRuleContext(text2sqlParser.CvssContext,0)


        def epss(self):
            return self.getTypedRuleContext(text2sqlParser.EpssContext,0)


        def age(self):
            return self.getTypedRuleContext(text2sqlParser.AgeContext,0)


        def confidence(self):
            return self.getTypedRuleContext(text2sqlParser.ConfidenceContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_numeric_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_column" ):
                listener.enterNumeric_column(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_column" ):
                listener.exitNumeric_column(self)




    def numeric_column(self):

        localctx = text2sqlParser.Numeric_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_numeric_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 26, 27, 28]:
                self.state = 196
                self.cvss()
                pass
            elif token in [29, 30, 31, 32, 33, 34]:
                self.state = 197
                self.epss()
                pass
            elif token in [35, 36]:
                self.state = 198
                self.age()
                pass
            elif token in [19, 20]:
                self.state = 199
                self.confidence()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gt(self):
            return self.getTypedRuleContext(text2sqlParser.GtContext,0)


        def lt(self):
            return self.getTypedRuleContext(text2sqlParser.LtContext,0)


        def eq(self):
            return self.getTypedRuleContext(text2sqlParser.EqContext,0)


        def like(self):
            return self.getTypedRuleContext(text2sqlParser.LikeContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = text2sqlParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operator)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49, 50, 51, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.gt()
                pass
            elif token in [54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.lt()
                pass
            elif token in [-1, 58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.eq()
                pass
            elif token in [59, 60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.like()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_gt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGt" ):
                listener.enterGt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGt" ):
                listener.exitGt(self)




    def gt(self):

        localctx = text2sqlParser.GtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_gt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8444249301319680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 209
                self.match(text2sqlParser.T__52)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_lt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLt" ):
                listener.enterLt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLt" ):
                listener.exitLt(self)




    def lt(self):

        localctx = text2sqlParser.LtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270215977642229760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 213
                self.match(text2sqlParser.T__52)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_eq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)




    def eq(self):

        localctx = text2sqlParser.EqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_eq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 216
                self.match(text2sqlParser.T__57)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LikeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_like

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLike" ):
                listener.enterLike(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLike" ):
                listener.exitLike(self)




    def like(self):

        localctx = text2sqlParser.LikeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_like)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==59 or _la==60):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def order(self):
            return self.getTypedRuleContext(text2sqlParser.OrderContext,0)


        def column(self):
            return self.getTypedRuleContext(text2sqlParser.ColumnContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_ordering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdering" ):
                listener.enterOrdering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdering" ):
                listener.exitOrdering(self)




    def ordering(self):

        localctx = text2sqlParser.OrderingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ordering)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.order()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953419264) != 0):
                self.state = 222
                self.column()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asc(self):
            return self.getTypedRuleContext(text2sqlParser.AscContext,0)


        def desc(self):
            return self.getTypedRuleContext(text2sqlParser.DescContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_order

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder" ):
                listener.enterOrder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder" ):
                listener.exitOrder(self)




    def order(self):

        localctx = text2sqlParser.OrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_order)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66, 67, 68, 69, 70, 71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.asc()
                pass
            elif token in [61, 62, 63, 64, 65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.desc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_desc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesc" ):
                listener.enterDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesc" ):
                listener.exitDesc(self)




    def desc(self):

        localctx = text2sqlParser.DescContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_asc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsc" ):
                listener.enterAsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsc" ):
                listener.exitAsc(self)




    def asc(self):

        localctx = text2sqlParser.AscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_asc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(text2sqlParser.INT, 0)

        def severity_scale(self):
            return self.getTypedRuleContext(text2sqlParser.Severity_scaleContext,0)


        def bool_(self):
            return self.getTypedRuleContext(text2sqlParser.BoolContext,0)


        def STRING(self):
            return self.getToken(text2sqlParser.STRING, 0)

        def getRuleIndex(self):
            return text2sqlParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = text2sqlParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_value)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(text2sqlParser.INT)
                pass
            elif token in [78, 79, 80, 81, 82]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.severity_scale()
                pass
            elif token in [72, 73, 74, 75, 76, 77]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.bool_()
                pass
            elif token in [85]:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(text2sqlParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def true(self):
            return self.getTypedRuleContext(text2sqlParser.TrueContext,0)


        def false(self):
            return self.getTypedRuleContext(text2sqlParser.FalseContext,0)


        def getRuleIndex(self):
            return text2sqlParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)




    def bool_(self):

        localctx = text2sqlParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_bool)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [72, 73, 74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.true()
                pass
            elif token in [75, 76, 77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.false()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_true

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)




    def true(self):

        localctx = text2sqlParser.TrueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_true)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FalseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_false

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)




    def false(self):

        localctx = text2sqlParser.FalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_false)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Severity_scaleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return text2sqlParser.RULE_severity_scale

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeverity_scale" ):
                listener.enterSeverity_scale(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeverity_scale" ):
                listener.exitSeverity_scale(self)




    def severity_scale(self):

        localctx = text2sqlParser.Severity_scaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_severity_scale)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not(((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





