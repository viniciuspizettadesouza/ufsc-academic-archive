// Generated from /home/pizetta/Downloads/compila/cmm/parser/cmm.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class cmmParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, INPUT=27, ELSE=28, ID=29, INT=30, FLOAT=31, NULL=32, 
		BOOLEAN=33, WS=34;
	public static final int
		RULE_start = 0, RULE_func = 1, RULE_args = 2, RULE_statms = 3, RULE_statm = 4, 
		RULE_switchStatms = 5, RULE_call = 6, RULE_exprs = 7, RULE_expr = 8, RULE_summ = 9, 
		RULE_mult = 10, RULE_atom = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "func", "args", "statms", "statm", "switchStatms", "call", "exprs", 
			"expr", "summ", "mult", "atom"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'def'", "'('", "')'", "','", "'{'", "'}'", "'='", "';'", "'print'", 
			"'if'", "'while'", "'for'", "'switch'", "'return'", "'case'", "':'", 
			"'>'", "'<'", "'<='", "'>='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", 
			"'input'", "'else'", null, null, null, "'None'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "INPUT", "ELSE", "ID", "INT", "FLOAT", "NULL", "BOOLEAN", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "cmm.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public cmmParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(cmmParser.EOF, 0); }
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(24);
				func();
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(30);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public Token name;
		public StatmsContext statms() {
			return getRuleContext(StatmsContext.class,0);
		}
		public TerminalNode ID() { return getToken(cmmParser.ID, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_func);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(T__0);
			setState(33);
			((FuncContext)_localctx).name = match(ID);
			setState(34);
			match(T__1);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(35);
				args();
				}
			}

			setState(38);
			match(T__2);
			setState(39);
			statms();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(cmmParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(cmmParser.ID, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(ID);
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(42);
				match(T__3);
				setState(43);
				match(ID);
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatmsContext extends ParserRuleContext {
		public List<StatmContext> statm() {
			return getRuleContexts(StatmContext.class);
		}
		public StatmContext statm(int i) {
			return getRuleContext(StatmContext.class,i);
		}
		public StatmsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statms; }
	}

	public final StatmsContext statms() throws RecognitionException {
		StatmsContext _localctx = new StatmsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statms);
		int _la;
		try {
			setState(58);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				match(T__4);
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << ID))) != 0)) {
					{
					{
					setState(50);
					statm();
					}
					}
					setState(55);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(56);
				match(T__5);
				}
				break;
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				statm();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatmContext extends ParserRuleContext {
		public StatmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statm; }
	 
		public StatmContext() { }
		public void copyFrom(StatmContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintContext extends StatmContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PrintContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class ForContext extends StatmContext {
		public ExprContext cond;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public StatmsContext statms() {
			return getRuleContext(StatmsContext.class,0);
		}
		public ForContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class WhileContext extends StatmContext {
		public ExprContext cond;
		public StatmsContext statms() {
			return getRuleContext(StatmsContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public WhileContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class IfContext extends StatmContext {
		public ExprContext cond;
		public StatmsContext then;
		public StatmsContext otherwise;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StatmsContext> statms() {
			return getRuleContexts(StatmsContext.class);
		}
		public StatmsContext statms(int i) {
			return getRuleContext(StatmsContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(cmmParser.ELSE, 0); }
		public IfContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class ReturnContext extends StatmContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class AssignContext extends StatmContext {
		public TerminalNode ID() { return getToken(cmmParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(StatmContext ctx) { copyFrom(ctx); }
	}
	public static class SwitchContext extends StatmContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<SwitchStatmsContext> switchStatms() {
			return getRuleContexts(SwitchStatmsContext.class);
		}
		public SwitchStatmsContext switchStatms(int i) {
			return getRuleContext(SwitchStatmsContext.class,i);
		}
		public SwitchContext(StatmContext ctx) { copyFrom(ctx); }
	}

	public final StatmContext statm() throws RecognitionException {
		StatmContext _localctx = new StatmContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_statm);
		int _la;
		try {
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				_localctx = new AssignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				match(ID);
				setState(61);
				match(T__6);
				setState(62);
				expr();
				setState(63);
				match(T__7);
				}
				break;
			case T__8:
				_localctx = new PrintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				match(T__8);
				setState(66);
				expr();
				setState(67);
				match(T__7);
				}
				break;
			case T__9:
				_localctx = new IfContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(69);
				match(T__9);
				setState(70);
				((IfContext)_localctx).cond = expr();
				setState(71);
				((IfContext)_localctx).then = statms();
				setState(74);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(72);
					match(ELSE);
					setState(73);
					((IfContext)_localctx).otherwise = statms();
					}
					break;
				}
				}
				break;
			case T__10:
				_localctx = new WhileContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(76);
				match(T__10);
				setState(77);
				((WhileContext)_localctx).cond = expr();
				setState(78);
				statms();
				}
				break;
			case T__11:
				_localctx = new ForContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(80);
				match(T__11);
				setState(81);
				match(T__1);
				setState(82);
				((ForContext)_localctx).cond = expr();
				setState(83);
				match(T__7);
				setState(84);
				((ForContext)_localctx).cond = expr();
				setState(85);
				match(T__7);
				setState(86);
				expr();
				setState(87);
				match(T__2);
				setState(88);
				statms();
				}
				break;
			case T__12:
				_localctx = new SwitchContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(90);
				match(T__12);
				setState(91);
				match(T__1);
				setState(92);
				atom();
				setState(93);
				match(T__2);
				setState(95); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(94);
					switchStatms();
					}
					}
					setState(97); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__4 );
				}
				break;
			case T__13:
				_localctx = new ReturnContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(99);
				match(T__13);
				setState(100);
				expr();
				setState(101);
				match(T__7);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwitchStatmsContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<SwitchStatmsContext> switchStatms() {
			return getRuleContexts(SwitchStatmsContext.class);
		}
		public SwitchStatmsContext switchStatms(int i) {
			return getRuleContext(SwitchStatmsContext.class,i);
		}
		public SwitchStatmsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatms; }
	}

	public final SwitchStatmsContext switchStatms() throws RecognitionException {
		SwitchStatmsContext _localctx = new SwitchStatmsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_switchStatms);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(T__4);
			setState(106);
			match(T__14);
			setState(107);
			atom();
			setState(108);
			match(T__15);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(109);
				switchStatms();
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(115);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public Token name;
		public TerminalNode ID() { return getToken(cmmParser.ID, 0); }
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			((CallContext)_localctx).name = match(ID);
			setState(118);
			match(T__1);
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << INPUT) | (1L << ID) | (1L << INT) | (1L << FLOAT) | (1L << NULL) | (1L << BOOLEAN))) != 0)) {
				{
				setState(119);
				exprs();
				}
			}

			setState(122);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprs; }
	}

	public final ExprsContext exprs() throws RecognitionException {
		ExprsContext _localctx = new ExprsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_exprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			expr();
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(125);
				match(T__3);
				setState(126);
				expr();
				}
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public SummContext left;
		public Token op;
		public ExprContext right;
		public SummContext summ() {
			return getRuleContext(SummContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expr);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			((ExprContext)_localctx).left = summ();
			setState(137);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(133);
					((ExprContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21))) != 0)) ) {
						((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(134);
					((ExprContext)_localctx).right = expr();
					}
					} 
				}
				setState(139);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SummContext extends ParserRuleContext {
		public MultContext left;
		public Token op;
		public SummContext right;
		public MultContext mult() {
			return getRuleContext(MultContext.class,0);
		}
		public List<SummContext> summ() {
			return getRuleContexts(SummContext.class);
		}
		public SummContext summ(int i) {
			return getRuleContext(SummContext.class,i);
		}
		public SummContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_summ; }
	}

	public final SummContext summ() throws RecognitionException {
		SummContext _localctx = new SummContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_summ);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			((SummContext)_localctx).left = mult();
			setState(145);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(141);
					((SummContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__22 || _la==T__23) ) {
						((SummContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(142);
					((SummContext)_localctx).right = summ();
					}
					} 
				}
				setState(147);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultContext extends ParserRuleContext {
		public AtomContext left;
		public Token op;
		public MultContext right;
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<MultContext> mult() {
			return getRuleContexts(MultContext.class);
		}
		public MultContext mult(int i) {
			return getRuleContext(MultContext.class,i);
		}
		public MultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mult; }
	}

	public final MultContext mult() throws RecognitionException {
		MultContext _localctx = new MultContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_mult);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			((MultContext)_localctx).left = atom();
			setState(153);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(149);
					((MultContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__24 || _la==T__25) ) {
						((MultContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(150);
					((MultContext)_localctx).right = mult();
					}
					} 
				}
				setState(155);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode INT() { return getToken(cmmParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(cmmParser.FLOAT, 0); }
		public TerminalNode NULL() { return getToken(cmmParser.NULL, 0); }
		public TerminalNode BOOLEAN() { return getToken(cmmParser.BOOLEAN, 0); }
		public TerminalNode ID() { return getToken(cmmParser.ID, 0); }
		public TerminalNode INPUT() { return getToken(cmmParser.INPUT, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_atom);
		try {
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				match(T__1);
				setState(157);
				expr();
				setState(158);
				match(T__2);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				match(INT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(161);
				match(FLOAT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(162);
				match(NULL);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(163);
				match(BOOLEAN);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(164);
				match(ID);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(165);
				match(INPUT);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(166);
				call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u00ac\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\3\2\7\2\34\n\2\f\2\16\2\37\13\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\3\5\3\'\n\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\5"+
		"\3\5\7\5\66\n\5\f\5\16\59\13\5\3\5\3\5\5\5=\n\5\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6M\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6b\n\6\r\6\16\6c"+
		"\3\6\3\6\3\6\3\6\5\6j\n\6\3\7\3\7\3\7\3\7\3\7\7\7q\n\7\f\7\16\7t\13\7"+
		"\3\7\3\7\3\b\3\b\3\b\5\b{\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u0082\n\t\f\t\16"+
		"\t\u0085\13\t\3\n\3\n\3\n\7\n\u008a\n\n\f\n\16\n\u008d\13\n\3\13\3\13"+
		"\3\13\7\13\u0092\n\13\f\13\16\13\u0095\13\13\3\f\3\f\3\f\7\f\u009a\n\f"+
		"\f\f\16\f\u009d\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00aa"+
		"\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\5\3\2\23\30\3\2\31\32"+
		"\3\2\33\34\2\u00b9\2\35\3\2\2\2\4\"\3\2\2\2\6+\3\2\2\2\b<\3\2\2\2\ni\3"+
		"\2\2\2\fk\3\2\2\2\16w\3\2\2\2\20~\3\2\2\2\22\u0086\3\2\2\2\24\u008e\3"+
		"\2\2\2\26\u0096\3\2\2\2\30\u00a9\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34"+
		"\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37\35\3\2\2\2 !\7"+
		"\2\2\3!\3\3\2\2\2\"#\7\3\2\2#$\7\37\2\2$&\7\4\2\2%\'\5\6\4\2&%\3\2\2\2"+
		"&\'\3\2\2\2\'(\3\2\2\2()\7\5\2\2)*\5\b\5\2*\5\3\2\2\2+\60\7\37\2\2,-\7"+
		"\6\2\2-/\7\37\2\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\7"+
		"\3\2\2\2\62\60\3\2\2\2\63\67\7\7\2\2\64\66\5\n\6\2\65\64\3\2\2\2\669\3"+
		"\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:=\7\b\2\2;=\5\n"+
		"\6\2<\63\3\2\2\2<;\3\2\2\2=\t\3\2\2\2>?\7\37\2\2?@\7\t\2\2@A\5\22\n\2"+
		"AB\7\n\2\2Bj\3\2\2\2CD\7\13\2\2DE\5\22\n\2EF\7\n\2\2Fj\3\2\2\2GH\7\f\2"+
		"\2HI\5\22\n\2IL\5\b\5\2JK\7\36\2\2KM\5\b\5\2LJ\3\2\2\2LM\3\2\2\2Mj\3\2"+
		"\2\2NO\7\r\2\2OP\5\22\n\2PQ\5\b\5\2Qj\3\2\2\2RS\7\16\2\2ST\7\4\2\2TU\5"+
		"\22\n\2UV\7\n\2\2VW\5\22\n\2WX\7\n\2\2XY\5\22\n\2YZ\7\5\2\2Z[\5\b\5\2"+
		"[j\3\2\2\2\\]\7\17\2\2]^\7\4\2\2^_\5\30\r\2_a\7\5\2\2`b\5\f\7\2a`\3\2"+
		"\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2dj\3\2\2\2ef\7\20\2\2fg\5\22\n\2gh\7"+
		"\n\2\2hj\3\2\2\2i>\3\2\2\2iC\3\2\2\2iG\3\2\2\2iN\3\2\2\2iR\3\2\2\2i\\"+
		"\3\2\2\2ie\3\2\2\2j\13\3\2\2\2kl\7\7\2\2lm\7\21\2\2mn\5\30\r\2nr\7\22"+
		"\2\2oq\5\f\7\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2"+
		"\2\2uv\7\b\2\2v\r\3\2\2\2wx\7\37\2\2xz\7\4\2\2y{\5\20\t\2zy\3\2\2\2z{"+
		"\3\2\2\2{|\3\2\2\2|}\7\5\2\2}\17\3\2\2\2~\u0083\5\22\n\2\177\u0080\7\6"+
		"\2\2\u0080\u0082\5\22\n\2\u0081\177\3\2\2\2\u0082\u0085\3\2\2\2\u0083"+
		"\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\21\3\2\2\2\u0085\u0083\3\2\2"+
		"\2\u0086\u008b\5\24\13\2\u0087\u0088\t\2\2\2\u0088\u008a\5\22\n\2\u0089"+
		"\u0087\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2"+
		"\2\2\u008c\23\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u0093\5\26\f\2\u008f\u0090"+
		"\t\3\2\2\u0090\u0092\5\24\13\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2"+
		"\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\25\3\2\2\2\u0095\u0093"+
		"\3\2\2\2\u0096\u009b\5\30\r\2\u0097\u0098\t\4\2\2\u0098\u009a\5\26\f\2"+
		"\u0099\u0097\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c"+
		"\3\2\2\2\u009c\27\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7\4\2\2\u009f"+
		"\u00a0\5\22\n\2\u00a0\u00a1\7\5\2\2\u00a1\u00aa\3\2\2\2\u00a2\u00aa\7"+
		" \2\2\u00a3\u00aa\7!\2\2\u00a4\u00aa\7\"\2\2\u00a5\u00aa\7#\2\2\u00a6"+
		"\u00aa\7\37\2\2\u00a7\u00aa\7\35\2\2\u00a8\u00aa\5\16\b\2\u00a9\u009e"+
		"\3\2\2\2\u00a9\u00a2\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9\u00a4\3\2\2\2\u00a9"+
		"\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2"+
		"\2\2\u00aa\31\3\2\2\2\21\35&\60\67<Lcirz\u0083\u008b\u0093\u009b\u00a9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}