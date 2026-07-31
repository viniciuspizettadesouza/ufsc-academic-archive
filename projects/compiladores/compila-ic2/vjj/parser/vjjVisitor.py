# Generated from /home/pizetta/git/compiladores/compila-ic2/vjj/parser/vjj.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .vjjParser import vjjParser
else:
    from .vjjParser import vjjParser

# This class defines a complete generic visitor for a parse tree produced by vjjParser.

class vjjVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by vjjParser#start.
    def visitStart(self, ctx:vjjParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#func.
    def visitFunc(self, ctx:vjjParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#args.
    def visitArgs(self, ctx:vjjParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#statms.
    def visitStatms(self, ctx:vjjParser.StatmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#assign.
    def visitAssign(self, ctx:vjjParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#print.
    def visitPrint(self, ctx:vjjParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#if.
    def visitIf(self, ctx:vjjParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#while.
    def visitWhile(self, ctx:vjjParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#for.
    def visitFor(self, ctx:vjjParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#switch.
    def visitSwitch(self, ctx:vjjParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#class.
    def visitClass(self, ctx:vjjParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#return.
    def visitReturn(self, ctx:vjjParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#whileStatement.
    def visitWhileStatement(self, ctx:vjjParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#switchStatms.
    def visitSwitchStatms(self, ctx:vjjParser.SwitchStatmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#types.
    def visitTypes(self, ctx:vjjParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#classdef.
    def visitClassdef(self, ctx:vjjParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#arglist.
    def visitArglist(self, ctx:vjjParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#argument.
    def visitArgument(self, ctx:vjjParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#test.
    def visitTest(self, ctx:vjjParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#or_test.
    def visitOr_test(self, ctx:vjjParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#and_test.
    def visitAnd_test(self, ctx:vjjParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#not_test.
    def visitNot_test(self, ctx:vjjParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#comparison.
    def visitComparison(self, ctx:vjjParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#call.
    def visitCall(self, ctx:vjjParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#exprs.
    def visitExprs(self, ctx:vjjParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#expr.
    def visitExpr(self, ctx:vjjParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#summ.
    def visitSumm(self, ctx:vjjParser.SummContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#mult.
    def visitMult(self, ctx:vjjParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vjjParser#atom.
    def visitAtom(self, ctx:vjjParser.AtomContext):
        return self.visitChildren(ctx)



del vjjParser