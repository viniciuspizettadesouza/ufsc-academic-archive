from sys import modules
from .parser.vjjParser import vjjParser
from .parser.vjjVisitor import vjjVisitor
from typing import List
import ast

class astVisitor(vjjVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.func_table = {}

    def visitStart(self, ctx:vjjParser.StartContext):
        main_call = ast.Call(func=ast.Name(id='main', ctx=ast.Load()), args=[], keywords=[]) 
        main = ast.Expr(value=main_call)
        body = [self.visit(func) for func in ctx.func()]
        body.append(main)
        module = ast.Module(body=body, type_ignores=[])
        ast.fix_missing_locations(module)
        return module
    
    def visitFunc(self, ctx:vjjParser.FuncContext):
        name = ctx.name.text
        args = self.visit(ctx.args()) if ctx.args() else [] # List or arguments

        self.func_table[name] = ast.Name(id=name, ctx=ast.Load())

        self.id_table = {} # Function id table
        for arg in args:
            self.id_table[arg.arg] = ast.Name(id=arg.arg, ctx=ast.Load())


        body = self.visit(ctx.statms())

        return ast.FunctionDef(name=name, args=ast.arguments(posonlyargs=[], args=args,
                                                             kwonlyargs=[],
                                                             kw_defaults=[],
                                                             defaults=[]),
                              body=body, decorator_list=[])

    def visitStatms(self, ctx:vjjParser.StatmsContext):
        return [self.visit(stmt) for stmt in ctx.statm()]

    def visitWhile(self, ctx:vjjParser.WhileContext):
        test = self.visit(ctx.cond)
        body = self.visit(ctx.statms())
        return ast.While(test=test, body=body, orelse=[])

    def visitIf(self, ctx:vjjParser.IfContext):
        test = self.visit(ctx.cond)
        body = self.visit(ctx.then)
        orelse = self.visit(ctx.otherwise) if ctx.ELSE() else []
        return ast.If(test=test, body=body, orelse=orelse)
        
    def visitArgs(self, ctx:vjjParser.ArgsContext):
        return [ast.arg(arg=str(id)) for id in ctx.ID()]

    def visitCall(self, ctx:vjjParser.CallContext):
        id = ctx.name.text
        if id not in self.func_table:
            raise KeyError(self.file_name+':'+str(ctx.name.line)+':'+str(ctx.name.column)+' function '+id+' is not defined')
        return ast.Call(func=self.func_table[id], 
                        args=self.visit(ctx.exprs()), keywords=[])

    def visitExprs(self, ctx:vjjParser.ExprsContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitAssign(self, ctx:vjjParser.AssignContext):
        expr = self.visit(ctx.expr())
        id = str(ctx.ID())
        if id not in self.id_table: # Create table entry if variable is not defined
            self.id_table[id] = ast.Name(id=id, ctx=ast.Load())
        return ast.Assign(targets=[ast.Name(id=id, ctx=ast.Store())], value=expr)

    def visitReturn(self, ctx:vjjParser.ReturnContext):
        return ast.Return(value=self.visit(ctx.expr()))

    def visitAtom(self, ctx:vjjParser.AtomContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ID():
            id = str(ctx.ID())
            if id not in self.id_table:
                symbol = ctx.ID().getSymbol()
                raise KeyError(self.file_name+':'+str(symbol.line)+':'+str(symbol.column)+' variable '+id+' is not defined')
            return ast.Name(id=id, ctx=ast.Load())
        elif ctx.INT():
            return ast.Constant(value=int(str(ctx.INT())))
        elif ctx.FLOAT():
            return ast.Constant(value=int(str(ctx.FLOAT())))
        elif ctx.NULL():
            return ast.Constant(value=int(str(ctx.NULL())))
        elif ctx.BOOLEAN():
            return ast.Constant(value=int(str(ctx.BOOLEAN())))
        elif ctx.call():
            return self.visit(ctx.call())
        elif ctx.INPUT():
            input_call = ast.Call(func=ast.Name(id='input', ctx=ast.Load()), 
                                  args=[], keywords=[])
            return ast.Call(func=ast.Name(id='int', ctx=ast.Load()), 
                            args=[input_call], keywords=[])

    def visitExpr(self, ctx:vjjParser.ExprContext):
        left = self.visit(ctx.left)
        if ctx.right: # >, <, >=, <=, ==, != 
            right = self.visit(ctx.right)

            op_map = {
                      '>' : ast.Gt,
                      '<' : ast.Lt,
                      '<=': ast.GtE,
                      '>=': ast.LtE,
                      '==': ast.Eq,
                      '!=': ast.NotEq}

            op = op_map[ctx.op.text]()
            
            return ast.Compare(left=left, ops=[op], comparators=[right])
        else: # higher priority expsetion 
             return left 

    def visitSumm(self, ctx:vjjParser.SummContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '+':
                op = ast.Add()
            elif ctx.op.text == '-':
                op = ast.Sub()
            
            return ast.BinOp(left=left, op=op, right=right)
        return left

    def visitMult(self, ctx:vjjParser.MultContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '*':
                op = ast.Mult()
            elif ctx.op.text == '/':
                op = ast.FloorDiv()
            
            return ast.BinOp(left=left, op=op, right=right)
        return left

    def visitPrint(self, ctx:vjjParser.PrintContext):
        print_call = ast.Call(func=ast.Name(id='print', ctx=ast.Load()),
                              args=[self.visit(ctx.expr())], keywords=[])
        return ast.Expr(value=print_call)

    def visitFor(self, ctx:vjjParser.ForContext):
        return self.visitChildren(ctx)

    def visitSwitch(self, ctx:vjjParser.SwitchContext):
        return self.visitChildren(ctx)
         
    def visitClass(self, ctx:vjjParser.ClassContext):
        return self.visitChildren(ctx)

    def visitWhileStatement(self, ctx:vjjParser.WhileStatementContext):
        return [self.visit(stmt) for stmt in ctx.statm()]

    def visitSwitchStatms(self, ctx:vjjParser.SwitchStatmsContext):
        return self.visitChildren(ctx)

    def visitTypes(self, ctx:vjjParser.TypesContext):
        return self.visitChildren(ctx)

    def visitClassdef(self, ctx:vjjParser.ClassdefContext):
        return self.visitChildren(ctx)