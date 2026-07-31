# Generated from /home/pizetta/Downloads/compila/cmm/parser/cmm.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cmmParser import cmmParser
else:
    from cmmParser import cmmParser

# This class defines a complete generic visitor for a parse tree produced by cmmParser.

class cmmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cmmParser#start.
    def visitStart(self, ctx:cmmParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#func.
    def visitFunc(self, ctx:cmmParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#args.
    def visitArgs(self, ctx:cmmParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#statms.
    def visitStatms(self, ctx:cmmParser.StatmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#assign.
    def visitAssign(self, ctx:cmmParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#print.
    def visitPrint(self, ctx:cmmParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#if.
    def visitIf(self, ctx:cmmParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#while.
    def visitWhile(self, ctx:cmmParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#for.
    def visitFor(self, ctx:cmmParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#switch.
    def visitSwitch(self, ctx:cmmParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#return.
    def visitReturn(self, ctx:cmmParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#switchStatms.
    def visitSwitchStatms(self, ctx:cmmParser.SwitchStatmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#call.
    def visitCall(self, ctx:cmmParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#exprs.
    def visitExprs(self, ctx:cmmParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#expr.
    def visitExpr(self, ctx:cmmParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#summ.
    def visitSumm(self, ctx:cmmParser.SummContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#mult.
    def visitMult(self, ctx:cmmParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmmParser#atom.
    def visitAtom(self, ctx:cmmParser.AtomContext):
        return self.visitChildren(ctx)



del cmmParser