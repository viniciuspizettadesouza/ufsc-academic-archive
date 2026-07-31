# Generated from /home/pizetta/git/compiladores/compila-ic2/vjj/parser/vjj.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u0114\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\7\2\60\n")
        buf.write("\2\f\2\16\2\63\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3;\n\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\7\4C\n\4\f\4\16\4F\13\4\3\5\3\5")
        buf.write("\7\5J\n\5\f\5\16\5M\13\5\3\5\3\5\5\5Q\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6a\n\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\6\6v\n\6\r\6\16\6w\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0080\n\6\3\7\3\7\7\7\u0084\n\7\f\7\16")
        buf.write("\7\u0087\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\b\u0090\n")
        buf.write("\b\f\b\16\b\u0093\13\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u009d\n\n\3\n\5\n\u00a0\n\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\7\13\u00a8\n\13\f\13\16\13\u00ab\13\13\3\13\5\13")
        buf.write("\u00ae\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b8")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c0\n\r\3\16\3\16\3")
        buf.write("\16\7\16\u00c5\n\16\f\16\16\16\u00c8\13\16\3\17\3\17\3")
        buf.write("\17\7\17\u00cd\n\17\f\17\16\17\u00d0\13\17\3\20\3\20\3")
        buf.write("\20\5\20\u00d5\n\20\3\21\3\21\3\21\3\21\7\21\u00db\n\21")
        buf.write("\f\21\16\21\u00de\13\21\3\22\3\22\3\22\5\22\u00e3\n\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\7\23\u00ea\n\23\f\23\16\23\u00ed")
        buf.write("\13\23\3\24\3\24\3\24\7\24\u00f2\n\24\f\24\16\24\u00f5")
        buf.write("\13\24\3\25\3\25\3\25\7\25\u00fa\n\25\f\25\16\25\u00fd")
        buf.write("\13\25\3\26\3\26\3\26\7\26\u0102\n\26\f\26\16\26\u0105")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0112\n\27\3\27\2\2\30\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,\2\6\3\2\25\30\3\2\r\21\3")
        buf.write("\2\22\23\4\2\f\f\24\24\2\u0124\2\61\3\2\2\2\4\66\3\2\2")
        buf.write("\2\6?\3\2\2\2\bP\3\2\2\2\n\177\3\2\2\2\f\u0081\3\2\2\2")
        buf.write("\16\u008a\3\2\2\2\20\u0096\3\2\2\2\22\u0098\3\2\2\2\24")
        buf.write("\u00a4\3\2\2\2\26\u00b7\3\2\2\2\30\u00b9\3\2\2\2\32\u00c1")
        buf.write("\3\2\2\2\34\u00c9\3\2\2\2\36\u00d4\3\2\2\2 \u00d6\3\2")
        buf.write("\2\2\"\u00df\3\2\2\2$\u00e6\3\2\2\2&\u00ee\3\2\2\2(\u00f6")
        buf.write("\3\2\2\2*\u00fe\3\2\2\2,\u0111\3\2\2\2.\60\5\4\3\2/.\3")
        buf.write("\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64\3")
        buf.write("\2\2\2\63\61\3\2\2\2\64\65\7\2\2\3\65\3\3\2\2\2\66\67")
        buf.write("\7\31\2\2\678\7\'\2\28:\7\3\2\29;\5\6\4\2:9\3\2\2\2:;")
        buf.write("\3\2\2\2;<\3\2\2\2<=\7\4\2\2=>\5\b\5\2>\5\3\2\2\2?D\7")
        buf.write("\'\2\2@A\7\5\2\2AC\7\'\2\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2")
        buf.write("\2DE\3\2\2\2E\7\3\2\2\2FD\3\2\2\2GK\7\6\2\2HJ\5\n\6\2")
        buf.write("IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3")
        buf.write("\2\2\2NQ\7\7\2\2OQ\5\n\6\2PG\3\2\2\2PO\3\2\2\2Q\t\3\2")
        buf.write("\2\2RS\7\'\2\2ST\7\b\2\2TU\5&\24\2UV\7\t\2\2V\u0080\3")
        buf.write("\2\2\2WX\7\33\2\2XY\5&\24\2YZ\7\t\2\2Z\u0080\3\2\2\2[")
        buf.write("\\\7\35\2\2\\]\5&\24\2]`\5\b\5\2^_\7\36\2\2_a\5\b\5\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2a\u0080\3\2\2\2bc\7\37\2\2cd\5&\24")
        buf.write("\2de\5\b\5\2e\u0080\3\2\2\2fg\7 \2\2gh\7\3\2\2hi\5&\24")
        buf.write("\2ij\7\t\2\2jk\5&\24\2kl\7\t\2\2lm\5&\24\2mn\7\4\2\2n")
        buf.write("o\5\b\5\2o\u0080\3\2\2\2pq\7!\2\2qr\7\3\2\2rs\5,\27\2")
        buf.write("su\7\4\2\2tv\5\16\b\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx")
        buf.write("\3\2\2\2x\u0080\3\2\2\2yz\7%\2\2z\u0080\5\22\n\2{|\7\32")
        buf.write("\2\2|}\5&\24\2}~\7\t\2\2~\u0080\3\2\2\2\177R\3\2\2\2\177")
        buf.write("W\3\2\2\2\177[\3\2\2\2\177b\3\2\2\2\177f\3\2\2\2\177p")
        buf.write("\3\2\2\2\177y\3\2\2\2\177{\3\2\2\2\u0080\13\3\2\2\2\u0081")
        buf.write("\u0085\7\6\2\2\u0082\u0084\5\n\6\2\u0083\u0082\3\2\2\2")
        buf.write("\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3")
        buf.write("\2\2\2\u0086\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089")
        buf.write("\7\7\2\2\u0089\r\3\2\2\2\u008a\u008b\7\6\2\2\u008b\u008c")
        buf.write("\7\34\2\2\u008c\u008d\5,\27\2\u008d\u0091\7\n\2\2\u008e")
        buf.write("\u0090\5\16\b\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2")
        buf.write("\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7\7\2\2\u0095")
        buf.write("\17\3\2\2\2\u0096\u0097\t\2\2\2\u0097\21\3\2\2\2\u0098")
        buf.write("\u0099\7%\2\2\u0099\u009f\5,\27\2\u009a\u009c\7\3\2\2")
        buf.write("\u009b\u009d\5\24\13\2\u009c\u009b\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\7\4\2\2\u009f")
        buf.write("\u009a\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a2\7\n\2\2\u00a2\u00a3\5\b\5\2\u00a3\23\3\2")
        buf.write("\2\2\u00a4\u00a9\5\26\f\2\u00a5\u00a6\7\5\2\2\u00a6\u00a8")
        buf.write("\5\26\f\2\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ac\u00ae\7\5\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\25\3\2\2\2\u00af\u00b0")
        buf.write("\5\30\r\2\u00b0\u00b1\7\b\2\2\u00b1\u00b2\5\30\r\2\u00b2")
        buf.write("\u00b8\3\2\2\2\u00b3\u00b4\7\13\2\2\u00b4\u00b8\5\30\r")
        buf.write("\2\u00b5\u00b6\7\f\2\2\u00b6\u00b8\5\30\r\2\u00b7\u00af")
        buf.write("\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\27\3\2\2\2\u00b9\u00bf\5\32\16\2\u00ba\u00bb\7\35\2\2")
        buf.write("\u00bb\u00bc\5\32\16\2\u00bc\u00bd\7\36\2\2\u00bd\u00be")
        buf.write("\5\30\r\2\u00be\u00c0\3\2\2\2\u00bf\u00ba\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c6\5\34\17\2")
        buf.write("\u00c2\u00c3\7\"\2\2\u00c3\u00c5\5\34\17\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write("\u00ce\5\36\20\2\u00ca\u00cb\7#\2\2\u00cb\u00cd\5\36\20")
        buf.write("\2\u00cc\u00ca\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\35\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d1\u00d2\7$\2\2\u00d2\u00d5\5\36\20\2\u00d3")
        buf.write("\u00d5\5 \21\2\u00d4\u00d1\3\2\2\2\u00d4\u00d3\3\2\2\2")
        buf.write("\u00d5\37\3\2\2\2\u00d6\u00dc\5&\24\2\u00d7\u00d8\5&\24")
        buf.write("\2\u00d8\u00d9\5&\24\2\u00d9\u00db\3\2\2\2\u00da\u00d7")
        buf.write("\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd!\3\2\2\2\u00de\u00dc\3\2\2\2\u00df")
        buf.write("\u00e0\7\'\2\2\u00e0\u00e2\7\3\2\2\u00e1\u00e3\5$\23\2")
        buf.write("\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3")
        buf.write("\2\2\2\u00e4\u00e5\7\4\2\2\u00e5#\3\2\2\2\u00e6\u00eb")
        buf.write("\5&\24\2\u00e7\u00e8\7\5\2\2\u00e8\u00ea\5&\24\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00eb\3\2\2")
        buf.write("\2\u00ee\u00f3\5(\25\2\u00ef\u00f0\t\3\2\2\u00f0\u00f2")
        buf.write("\5&\24\2\u00f1\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\'\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00fb\5*\26\2\u00f7\u00f8\t\4\2\2")
        buf.write("\u00f8\u00fa\5(\25\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3")
        buf.write("\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc)")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0103\5,\27\2\u00ff")
        buf.write("\u0100\t\5\2\2\u0100\u0102\5*\26\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104+\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107")
        buf.write("\7\3\2\2\u0107\u0108\5&\24\2\u0108\u0109\7\4\2\2\u0109")
        buf.write("\u0112\3\2\2\2\u010a\u0112\7(\2\2\u010b\u0112\7)\2\2\u010c")
        buf.write("\u0112\7*\2\2\u010d\u0112\7+\2\2\u010e\u0112\7\'\2\2\u010f")
        buf.write("\u0112\7&\2\2\u0110\u0112\5\"\22\2\u0111\u0106\3\2\2\2")
        buf.write("\u0111\u010a\3\2\2\2\u0111\u010b\3\2\2\2\u0111\u010c\3")
        buf.write("\2\2\2\u0111\u010d\3\2\2\2\u0111\u010e\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0110\3\2\2\2\u0112-\3\2\2\2\34\61:DKP")
        buf.write("`w\177\u0085\u0091\u009c\u009f\u00a9\u00ad\u00b7\u00bf")
        buf.write("\u00c6\u00ce\u00d4\u00dc\u00e2\u00eb\u00f3\u00fb\u0103")
        buf.write("\u0111")
        return buf.getvalue()


class vjjParser ( Parser ):

    grammarFileName = "vjj.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'{'", "'}'", "'='", 
                     "';'", "':'", "'**'", "'*'", "'>'", "'<'", "'<='", 
                     "'>='", "'=='", "'+'", "'-'", "'/'", "'int'", "'float'", 
                     "'bool'", "'null'", "'def'", "'return'", "'print'", 
                     "'case'", "'if'", "'else'", "'while'", "'for'", "'switch'", 
                     "'or'", "'and'", "'not'", "'class'", "'input'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'None'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TYPE_INT", 
                      "TYPE_FLOAT", "TYPE_BOOLEAN", "TYPE_NULL", "DEF", 
                      "RETURN", "PRINT", "CASE", "IF", "ELSE", "WHILE", 
                      "FOR", "SWITCH", "OR", "AND", "NOT", "CLASS", "INPUT", 
                      "ID", "INT", "FLOAT", "NULL", "BOOLEAN", "WS" ]

    RULE_start = 0
    RULE_func = 1
    RULE_args = 2
    RULE_statms = 3
    RULE_statm = 4
    RULE_whileStatement = 5
    RULE_switchStatms = 6
    RULE_types = 7
    RULE_classdef = 8
    RULE_arglist = 9
    RULE_argument = 10
    RULE_test = 11
    RULE_or_test = 12
    RULE_and_test = 13
    RULE_not_test = 14
    RULE_comparison = 15
    RULE_call = 16
    RULE_exprs = 17
    RULE_expr = 18
    RULE_summ = 19
    RULE_mult = 20
    RULE_atom = 21

    ruleNames =  [ "start", "func", "args", "statms", "statm", "whileStatement", 
                   "switchStatms", "types", "classdef", "arglist", "argument", 
                   "test", "or_test", "and_test", "not_test", "comparison", 
                   "call", "exprs", "expr", "summ", "mult", "atom" ]

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
    TYPE_INT=19
    TYPE_FLOAT=20
    TYPE_BOOLEAN=21
    TYPE_NULL=22
    DEF=23
    RETURN=24
    PRINT=25
    CASE=26
    IF=27
    ELSE=28
    WHILE=29
    FOR=30
    SWITCH=31
    OR=32
    AND=33
    NOT=34
    CLASS=35
    INPUT=36
    ID=37
    INT=38
    FLOAT=39
    NULL=40
    BOOLEAN=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(vjjParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.FuncContext)
            else:
                return self.getTypedRuleContext(vjjParser.FuncContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = vjjParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.DEF:
                self.state = 44
                self.func()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(vjjParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def DEF(self):
            return self.getToken(vjjParser.DEF, 0)

        def statms(self):
            return self.getTypedRuleContext(vjjParser.StatmsContext,0)


        def ID(self):
            return self.getToken(vjjParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(vjjParser.ArgsContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = vjjParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(vjjParser.DEF)
            self.state = 53
            localctx.name = self.match(vjjParser.ID)
            self.state = 54
            self.match(vjjParser.T__0)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==vjjParser.ID:
                self.state = 55
                self.args()


            self.state = 58
            self.match(vjjParser.T__1)
            self.state = 59
            self.statms()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(vjjParser.ID)
            else:
                return self.getToken(vjjParser.ID, i)

        def getRuleIndex(self):
            return vjjParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = vjjParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(vjjParser.ID)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.T__2:
                self.state = 62
                self.match(vjjParser.T__2)
                self.state = 63
                self.match(vjjParser.ID)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.StatmContext)
            else:
                return self.getTypedRuleContext(vjjParser.StatmContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_statms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatms" ):
                return visitor.visitStatms(self)
            else:
                return visitor.visitChildren(self)




    def statms(self):

        localctx = vjjParser.StatmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statms)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [vjjParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(vjjParser.T__3)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.RETURN) | (1 << vjjParser.PRINT) | (1 << vjjParser.IF) | (1 << vjjParser.WHILE) | (1 << vjjParser.FOR) | (1 << vjjParser.SWITCH) | (1 << vjjParser.CLASS) | (1 << vjjParser.ID))) != 0):
                    self.state = 70
                    self.statm()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 76
                self.match(vjjParser.T__4)
                pass
            elif token in [vjjParser.RETURN, vjjParser.PRINT, vjjParser.IF, vjjParser.WHILE, vjjParser.FOR, vjjParser.SWITCH, vjjParser.CLASS, vjjParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.statm()
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


    class StatmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return vjjParser.RULE_statm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(vjjParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(vjjParser.FOR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.ExprContext)
            else:
                return self.getTypedRuleContext(vjjParser.ExprContext,i)

        def statms(self):
            return self.getTypedRuleContext(vjjParser.StatmsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(vjjParser.WHILE, 0)
        def statms(self):
            return self.getTypedRuleContext(vjjParser.StatmsContext,0)

        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.then = None # StatmsContext
            self.otherwise = None # StatmsContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(vjjParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)

        def statms(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.StatmsContext)
            else:
                return self.getTypedRuleContext(vjjParser.StatmsContext,i)

        def ELSE(self):
            return self.getToken(vjjParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ClassContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLASS(self):
            return self.getToken(vjjParser.CLASS, 0)
        def classdef(self):
            return self.getTypedRuleContext(vjjParser.ClassdefContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass" ):
                return visitor.visitClass(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(vjjParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(vjjParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class SwitchContext(StatmContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vjjParser.StatmContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(vjjParser.SWITCH, 0)
        def atom(self):
            return self.getTypedRuleContext(vjjParser.AtomContext,0)

        def switchStatms(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.SwitchStatmsContext)
            else:
                return self.getTypedRuleContext(vjjParser.SwitchStatmsContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch" ):
                return visitor.visitSwitch(self)
            else:
                return visitor.visitChildren(self)



    def statm(self):

        localctx = vjjParser.StatmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statm)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [vjjParser.ID]:
                localctx = vjjParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(vjjParser.ID)
                self.state = 81
                self.match(vjjParser.T__5)
                self.state = 82
                self.expr()
                self.state = 83
                self.match(vjjParser.T__6)
                pass
            elif token in [vjjParser.PRINT]:
                localctx = vjjParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(vjjParser.PRINT)
                self.state = 86
                self.expr()
                self.state = 87
                self.match(vjjParser.T__6)
                pass
            elif token in [vjjParser.IF]:
                localctx = vjjParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(vjjParser.IF)
                self.state = 90
                localctx.cond = self.expr()
                self.state = 91
                localctx.then = self.statms()
                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.match(vjjParser.ELSE)
                    self.state = 93
                    localctx.otherwise = self.statms()


                pass
            elif token in [vjjParser.WHILE]:
                localctx = vjjParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(vjjParser.WHILE)
                self.state = 97
                localctx.cond = self.expr()
                self.state = 98
                self.statms()
                pass
            elif token in [vjjParser.FOR]:
                localctx = vjjParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.match(vjjParser.FOR)
                self.state = 101
                self.match(vjjParser.T__0)
                self.state = 102
                localctx.cond = self.expr()
                self.state = 103
                self.match(vjjParser.T__6)
                self.state = 104
                localctx.cond = self.expr()
                self.state = 105
                self.match(vjjParser.T__6)
                self.state = 106
                self.expr()
                self.state = 107
                self.match(vjjParser.T__1)
                self.state = 108
                self.statms()
                pass
            elif token in [vjjParser.SWITCH]:
                localctx = vjjParser.SwitchContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.match(vjjParser.SWITCH)
                self.state = 111
                self.match(vjjParser.T__0)
                self.state = 112
                self.atom()
                self.state = 113
                self.match(vjjParser.T__1)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.switchStatms()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==vjjParser.T__3):
                        break

                pass
            elif token in [vjjParser.CLASS]:
                localctx = vjjParser.ClassContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 119
                self.match(vjjParser.CLASS)
                self.state = 120
                self.classdef()
                pass
            elif token in [vjjParser.RETURN]:
                localctx = vjjParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 121
                self.match(vjjParser.RETURN)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(vjjParser.T__6)
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


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.StatmContext)
            else:
                return self.getTypedRuleContext(vjjParser.StatmContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = vjjParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(vjjParser.T__3)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.RETURN) | (1 << vjjParser.PRINT) | (1 << vjjParser.IF) | (1 << vjjParser.WHILE) | (1 << vjjParser.FOR) | (1 << vjjParser.SWITCH) | (1 << vjjParser.CLASS) | (1 << vjjParser.ID))) != 0):
                self.state = 128
                self.statm()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(vjjParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(vjjParser.CASE, 0)

        def atom(self):
            return self.getTypedRuleContext(vjjParser.AtomContext,0)


        def switchStatms(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.SwitchStatmsContext)
            else:
                return self.getTypedRuleContext(vjjParser.SwitchStatmsContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_switchStatms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatms" ):
                return visitor.visitSwitchStatms(self)
            else:
                return visitor.visitChildren(self)




    def switchStatms(self):

        localctx = vjjParser.SwitchStatmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_switchStatms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(vjjParser.T__3)
            self.state = 137
            self.match(vjjParser.CASE)
            self.state = 138
            self.atom()
            self.state = 139
            self.match(vjjParser.T__7)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.T__3:
                self.state = 140
                self.switchStatms()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(vjjParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(vjjParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(vjjParser.TYPE_FLOAT, 0)

        def TYPE_BOOLEAN(self):
            return self.getToken(vjjParser.TYPE_BOOLEAN, 0)

        def TYPE_NULL(self):
            return self.getToken(vjjParser.TYPE_NULL, 0)

        def getRuleIndex(self):
            return vjjParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = vjjParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.TYPE_INT) | (1 << vjjParser.TYPE_FLOAT) | (1 << vjjParser.TYPE_BOOLEAN) | (1 << vjjParser.TYPE_NULL))) != 0)):
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


    class ClassdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(vjjParser.CLASS, 0)

        def atom(self):
            return self.getTypedRuleContext(vjjParser.AtomContext,0)


        def statms(self):
            return self.getTypedRuleContext(vjjParser.StatmsContext,0)


        def arglist(self):
            return self.getTypedRuleContext(vjjParser.ArglistContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_classdef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdef" ):
                return visitor.visitClassdef(self)
            else:
                return visitor.visitChildren(self)




    def classdef(self):

        localctx = vjjParser.ClassdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(vjjParser.CLASS)
            self.state = 151
            self.atom()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==vjjParser.T__0:
                self.state = 152
                self.match(vjjParser.T__0)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.T__0) | (1 << vjjParser.T__8) | (1 << vjjParser.T__9) | (1 << vjjParser.NOT) | (1 << vjjParser.INPUT) | (1 << vjjParser.ID) | (1 << vjjParser.INT) | (1 << vjjParser.FLOAT) | (1 << vjjParser.NULL) | (1 << vjjParser.BOOLEAN))) != 0):
                    self.state = 153
                    self.arglist()


                self.state = 156
                self.match(vjjParser.T__1)


            self.state = 159
            self.match(vjjParser.T__7)
            self.state = 160
            self.statms()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(vjjParser.ArgumentContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = vjjParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.argument()
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 163
                    self.match(vjjParser.T__2)
                    self.state = 164
                    self.argument() 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==vjjParser.T__2:
                self.state = 170
                self.match(vjjParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.TestContext)
            else:
                return self.getTypedRuleContext(vjjParser.TestContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = vjjParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [vjjParser.T__0, vjjParser.NOT, vjjParser.INPUT, vjjParser.ID, vjjParser.INT, vjjParser.FLOAT, vjjParser.NULL, vjjParser.BOOLEAN]:
                self.state = 173
                self.test()
                self.state = 174
                self.match(vjjParser.T__5)
                self.state = 175
                self.test()
                pass
            elif token in [vjjParser.T__8]:
                self.state = 177
                self.match(vjjParser.T__8)
                self.state = 178
                self.test()
                pass
            elif token in [vjjParser.T__9]:
                self.state = 179
                self.match(vjjParser.T__9)
                self.state = 180
                self.test()
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


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.Or_testContext)
            else:
                return self.getTypedRuleContext(vjjParser.Or_testContext,i)


        def IF(self):
            return self.getToken(vjjParser.IF, 0)

        def ELSE(self):
            return self.getToken(vjjParser.ELSE, 0)

        def test(self):
            return self.getTypedRuleContext(vjjParser.TestContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_test

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest" ):
                return visitor.visitTest(self)
            else:
                return visitor.visitChildren(self)




    def test(self):

        localctx = vjjParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.or_test()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==vjjParser.IF:
                self.state = 184
                self.match(vjjParser.IF)
                self.state = 185
                self.or_test()
                self.state = 186
                self.match(vjjParser.ELSE)
                self.state = 187
                self.test()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.And_testContext)
            else:
                return self.getTypedRuleContext(vjjParser.And_testContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(vjjParser.OR)
            else:
                return self.getToken(vjjParser.OR, i)

        def getRuleIndex(self):
            return vjjParser.RULE_or_test

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_test" ):
                return visitor.visitOr_test(self)
            else:
                return visitor.visitChildren(self)




    def or_test(self):

        localctx = vjjParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_or_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.and_test()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.OR:
                self.state = 192
                self.match(vjjParser.OR)
                self.state = 193
                self.and_test()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.Not_testContext)
            else:
                return self.getTypedRuleContext(vjjParser.Not_testContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(vjjParser.AND)
            else:
                return self.getToken(vjjParser.AND, i)

        def getRuleIndex(self):
            return vjjParser.RULE_and_test

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_test" ):
                return visitor.visitAnd_test(self)
            else:
                return visitor.visitChildren(self)




    def and_test(self):

        localctx = vjjParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_and_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.not_test()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.AND:
                self.state = 200
                self.match(vjjParser.AND)
                self.state = 201
                self.not_test()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(vjjParser.NOT, 0)

        def not_test(self):
            return self.getTypedRuleContext(vjjParser.Not_testContext,0)


        def comparison(self):
            return self.getTypedRuleContext(vjjParser.ComparisonContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_not_test

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_test" ):
                return visitor.visitNot_test(self)
            else:
                return visitor.visitChildren(self)




    def not_test(self):

        localctx = vjjParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_not_test)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [vjjParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(vjjParser.NOT)
                self.state = 208
                self.not_test()
                pass
            elif token in [vjjParser.T__0, vjjParser.INPUT, vjjParser.ID, vjjParser.INT, vjjParser.FLOAT, vjjParser.NULL, vjjParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.comparison()
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


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.ExprContext)
            else:
                return self.getTypedRuleContext(vjjParser.ExprContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = vjjParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expr()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.T__0) | (1 << vjjParser.INPUT) | (1 << vjjParser.ID) | (1 << vjjParser.INT) | (1 << vjjParser.FLOAT) | (1 << vjjParser.NULL) | (1 << vjjParser.BOOLEAN))) != 0):
                self.state = 213
                self.expr()
                self.state = 214
                self.expr()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ID(self):
            return self.getToken(vjjParser.ID, 0)

        def exprs(self):
            return self.getTypedRuleContext(vjjParser.ExprsContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = vjjParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            localctx.name = self.match(vjjParser.ID)
            self.state = 222
            self.match(vjjParser.T__0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.T__0) | (1 << vjjParser.INPUT) | (1 << vjjParser.ID) | (1 << vjjParser.INT) | (1 << vjjParser.FLOAT) | (1 << vjjParser.NULL) | (1 << vjjParser.BOOLEAN))) != 0):
                self.state = 223
                self.exprs()


            self.state = 226
            self.match(vjjParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.ExprContext)
            else:
                return self.getTypedRuleContext(vjjParser.ExprContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = vjjParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expr()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==vjjParser.T__2:
                self.state = 229
                self.match(vjjParser.T__2)
                self.state = 230
                self.expr()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # SummContext
            self.op = None # Token
            self.right = None # ExprContext

        def summ(self):
            return self.getTypedRuleContext(vjjParser.SummContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.ExprContext)
            else:
                return self.getTypedRuleContext(vjjParser.ExprContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = vjjParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            localctx.left = self.summ()
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << vjjParser.T__10) | (1 << vjjParser.T__11) | (1 << vjjParser.T__12) | (1 << vjjParser.T__13) | (1 << vjjParser.T__14))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    localctx.right = self.expr() 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # MultContext
            self.op = None # Token
            self.right = None # SummContext

        def mult(self):
            return self.getTypedRuleContext(vjjParser.MultContext,0)


        def summ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.SummContext)
            else:
                return self.getTypedRuleContext(vjjParser.SummContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_summ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumm" ):
                return visitor.visitSumm(self)
            else:
                return visitor.visitChildren(self)




    def summ(self):

        localctx = vjjParser.SummContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_summ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            localctx.left = self.mult()
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 245
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==vjjParser.T__15 or _la==vjjParser.T__16):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    localctx.right = self.summ() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AtomContext
            self.op = None # Token
            self.right = None # MultContext

        def atom(self):
            return self.getTypedRuleContext(vjjParser.AtomContext,0)


        def mult(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vjjParser.MultContext)
            else:
                return self.getTypedRuleContext(vjjParser.MultContext,i)


        def getRuleIndex(self):
            return vjjParser.RULE_mult

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)




    def mult(self):

        localctx = vjjParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mult)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            localctx.left = self.atom()
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 253
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==vjjParser.T__9 or _la==vjjParser.T__17):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 254
                    localctx.right = self.mult() 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(vjjParser.ExprContext,0)


        def INT(self):
            return self.getToken(vjjParser.INT, 0)

        def FLOAT(self):
            return self.getToken(vjjParser.FLOAT, 0)

        def NULL(self):
            return self.getToken(vjjParser.NULL, 0)

        def BOOLEAN(self):
            return self.getToken(vjjParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(vjjParser.ID, 0)

        def INPUT(self):
            return self.getToken(vjjParser.INPUT, 0)

        def call(self):
            return self.getTypedRuleContext(vjjParser.CallContext,0)


        def getRuleIndex(self):
            return vjjParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = vjjParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atom)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(vjjParser.T__0)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(vjjParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(vjjParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(vjjParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(vjjParser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(vjjParser.BOOLEAN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.match(vjjParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.match(vjjParser.INPUT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





